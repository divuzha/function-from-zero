# function-from-zero

[![Python application test with GitHub Actions](https://github.com/divuzha/function-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/divuzha/function-from-zero/actions/workflows/main.yml)

### To call Microservice

something like this
```bash
curl -X 'POST' \
  'https://ubiquitous-space-cod-qw7px45qg45f9v5r-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft",
  "length": 1
}'
```

### Build container

`docker build .`
`docker image ls`

### Run container

`docker run -p 127.0.0.1:8080:8080 ec34867a1962`

### Invoke

run `invoke.sh`