FROM python:3.10
EXPOSE 5000
WORKDIR /rest_with_flask
COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry
RUN pip install poethepoet
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
COPY app.py /rest_with_flask/app.py
CMD ["poetry", "run", "poe", "flask"]
#CMD ["sleep", "500"]
