# Simple Store Flask API with Jose

## How to Run
This app can be run via poetry or docker.

### Poetry
```commandline
poetry install
poetry run poe app
```

### Docker
#### Build
Build Docker Image.
```commandline
docker build -t simple_store .
```
#### Run (Simple)
Run self-contained container.
```commandline
docker run -p 5000:5000 simple_store
```
Requires the following Dockerfile:
```dockerfile
FROM python:3.10
EXPOSE 5000
WORKDIR /simple_store
COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry
RUN pip install poethepoet
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
COPY /src src
CMD ["poetry", "run", "poe", "app"]
```
#### Run (Mounted)
Run container with a mounted volume.
```commandline
docker run -p 5000:5000 -w /rest_with_flask -v ${PWD}/src:/rest_with_flask/src simple_store
```
Requires the following Dockerfile:
```dockerfile
FROM python:3.10
EXPOSE 5000
WORKDIR /rest_with_flask
COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry
RUN pip install poethepoet
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
CMD ["poetry", "run", "poe", "app"]
```
