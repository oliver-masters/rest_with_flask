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
COPY run.py run.py
CMD ["poetry", "run", "poe", "app"]
#CMD ["ping", "-t", "localhost"]
