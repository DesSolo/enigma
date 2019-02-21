import tornado.ioloop
from tornado.web import url, Application
from secrets import token_hex
from core import validators
from core import settings
from core.settings import CACHE as cache


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass


class IndexHandler(BaseHandler):
    def get(self):
        self.render("templates/index.html", days=settings.DAYS_RANGE)

    def post(self, *args, **kwargs):
        msg = self.get_argument('msg')
        due = self.get_argument('due')
        if not msg or (due not in settings.DAYS_RANGE):
            return self.send_error(405)
        token = token_hex(settings.TOKEN_BYTES)
        cache.set(token, msg, due)
        return self.write(f'{settings.PROTOCOL}://{self.request.host}/get/{token}')


class GetSecretHandler(BaseHandler):
    def get(self, token, *args, **kwargs):
        if not validators.user_agent(self.request.headers["User-Agent"]):
            return self.send_error(403)
        message = cache.get(token)
        if not message:
            return self.send_error(404)
        return self.render('templates/message.html', message=message)


def application():
    return Application([
        url(r"/", IndexHandler, name='index'),
        url(r'/get/(\w+)', GetSecretHandler, name='get_secret')
    ])


if __name__ == "__main__":
    app = application()
    app.listen(**settings.LISTEN)
    tornado.ioloop.IOLoop.current().start()
