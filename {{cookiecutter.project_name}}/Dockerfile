########## BUILDER STAGE ##########
FROM python:{{cookiecutter.target_python_version}}-alpine as builder

USER root

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION={{cookiecutter.poetry_version}}

COPY pyproject.toml /home/app/pyproject.toml
COPY poetry.lock /home/app/poetry.lock
COPY {{cookiecutter.project_slug}} /home/app/{{cookiecutter.project_slug}}

WORKDIR /home/app

RUN python3 -m venv venv && \
    source venv/bin/activate  && \
    pip install -U pip && \
    pip install "poetry==$POETRY_VERSION" && \
    poetry install --without dev

########## FINAL STAGE ##########
FROM python:{{cookiecutter.target_python_version}}-alpine

WORKDIR /home/app

ENV PATH="/home/app/venv/bin:$PATH"

COPY --from=builder /home/app/venv /home/app/venv
COPY --from=builder /home/app/{{cookiecutter.project_slug}} /home/app/{{cookiecutter.project_slug}}

RUN source /home/app/venv/bin/activate

ENTRYPOINT ["/bin/sh", "-c"]
