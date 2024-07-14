{{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Table Of Contents

The documentation consists of the folowing parts:


1. [Getting started](./content/getting-started.md)
2. [Code Reference](./reference/SUMMARY.md)

Quickly find what you're looking for depending on
your use case by looking at the different pages.

## Project layout

    .
    ├── Makefile
    ├── README.md
    ├── codecov.yaml
    ├── {{cookiecutter.project_name}}
    │   ├── __init__.py
    │   └── foo.py
    ├── docs
    │   ├── reference
    │   ├── content
    │   │   └── getting-started.md
    │   └── index.md
    ├── mkdocs.yml
    ├── poetry.lock
    ├── poetry.toml
    ├── pyproject.toml
    ├── scripts
    │   └── gen_ref_pages.py
    └── tests
