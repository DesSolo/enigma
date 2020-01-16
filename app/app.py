from secrets import token_hex
import logging
from aiohttp import web
import aiohttp_jinja2
import jinja2
from core import settings, validators
from core.settings import cache


class IndexView(web.View):
    @aiohttp_jinja2.template('index.html')
    async def get(self):
        return {'days': settings.DAYS_RANGE}

    async def post(self):
        data = await self.request.post()
        if not data.get('msg') or (data.get('due') not in settings.DAYS_RANGE):
            return web.Response(status=405)
        token = token_hex(settings.TOKEN_BYTES)
        cache.set(token, data.get('msg'), data.get('due'))
        return web.Response(body=f'{settings.PROTOCOL}://{self.request.host}/get/{token}')


class SecretView(web.View):
    @aiohttp_jinja2.template('message.html')
    async def get(self):
        token = self.request.match_info['token']
        if len(token) != settings.TOKEN_BYTES * 2:
            return web.HTTPNotFound()
        if not validators.user_agent(self.request.headers["User-Agent"]):
            return web.HTTPForbidden()
        message = cache.get(token)
        if not message:
            return web.HTTPNotFound()
        return {'message': message}


if __name__ == "__main__":
    app = web.Application()
    logging.basicConfig(level=logging.INFO)
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader('templates')
    )
    app.add_routes([
        web.view('/', IndexView, name='index'),
        web.view(r'/get/{token:\w+}', SecretView, name='secret')
    ])
    web.run_app(
        app,
        access_log_format=settings.LOG_FORMAT,
        **settings.LISTEN
    )
