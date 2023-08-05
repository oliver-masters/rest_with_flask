# Simple Store Flask API with Jose

## How to Run
This app can be run via poetry or docker.

### Poetry
```commandline
poetry install
poetry run poe app
```

### Docker

#### Run Mounted (preferred)
Build Docker Image.
```commandline
docker build -t simple_store_mounted .
```

Run container with a mounted volume.
```commandline
docker run -p 5000:5000 -w /rest_with_flask -v ${PWD}/src:/rest_with_flask/src simple_store_mounted
```

#### Run Self Contained (exercise)
Build Docker Image.
```commandline
docker build -t simple_store . -f Dockerfile_without_mounting
```

Run self-contained container.
```commandline
docker run -p 5000:5000 simple_store
```