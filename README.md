## Enigma

A simple solution for sending one-time messages. The message can be read only once.
```
aiohttp
Redis
```
`docker run -d -p 80:8000 dessolo/enigma`

Docker-compose file [example](https://github.com/DesSolo/enigma/blob/master/docker-compose.yaml)

### Environment Variables
| Variable    | Default   | Description                      |
| ----------- | --------- | -------------------------------- |
| PROTOCOL    | http      | Used protocol ( http or https )  |
| PORT        | 8000      | Listen port                      |
| REDIS_HOST  | 127.0.0.1 | Redis server address or hostname |
| REDIS_PORT  | 6379      | Redis server port                |
| TOKEN_BYTES | 20        | Length of url token              |