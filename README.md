## Enigma
![Docker Cloud Automated build](https://img.shields.io/docker/cloud/automated/dessolo/enigma)
![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/dessolo/enigma)
![Docker Pulls](https://img.shields.io/docker/pulls/dessolo/enigma)
![Docker Image Version (latest by date)](https://img.shields.io/docker/v/dessolo/enigma)
![GitHub](https://img.shields.io/github/license/dessolo/enigma)

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