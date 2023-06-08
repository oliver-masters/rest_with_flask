FROM python:3.10
EXPOSE 5000
WORKDIR /rest_with_flask
COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry
RUN pip install poethepoet
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
COPY run.py /rest_with_flask/run.py
CMD ["poetry", "run", "poe", "app"]
