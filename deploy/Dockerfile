FROM python:3.11-slim-bookworm
# use root as workdir and set as python path
WORKDIR /code

# install poetry
RUN pip install poetry

# install requirements
COPY ../poetry.lock /code/poetry.lock
COPY ../pyproject.toml /code/pyproject.toml

RUN poetry config virtualenvs.create false
RUN poetry install --no-root

# copy both pipeline and server source code
COPY ../src /code/src
COPY ../cert /code/cert

CMD ["uvicorn", "src.client.fastAPI:app", "--host", "0.0.0.0", "--port", "80"]