########## BUILDER STAGE ##########
FROM python:{{cookiecutter.target_python_version}}-slim-bookworm as builder

USER root

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION={{cookiecutter.poetry_version}} \
    PYTHONUNBUFFERED=1

WORKDIR /home/app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy only necessary files
COPY pyproject.toml ./
COPY {{cookiecutter.project_slug}} ./{{cookiecutter.project_slug}}

# Install Python dependencies
RUN python -m pip install --upgrade pip setuptools wheel && \
    pip install "poetry==$POETRY_VERSION" && \
    poetry config virtualenvs.in-project true && \
    poetry install --without dev && \
    cd {{cookiecutter.project_slug}}

########## FINAL STAGE ##########
FROM python:{{cookiecutter.target_python_version}}-slim-bookworm

WORKDIR /home/app/{{cookiecutter.project_slug}}

ENV PATH="/home/app/.venv/bin:$PATH"

# Copy only necessary files from the builder stage
COPY --from=builder /home/app/.venv /home/app/.venv
COPY --from=builder /home/app/{{cookiecutter.project_slug}} /home/app/{{cookiecutter.project_slug}}

ENTRYPOINT ["/bin/sh", "-c"]
