#!/usr/bin/env python
import os
import shutil
from pathlib import Path

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    if "{{cookiecutter.include_github_actions}}" != "y":
        remove_dir(".github")

    if "{{cookiecutter.mkdocs}}" != "y":
        remove_dir("docs")
        remove_file("mkdocs.yml")
        remove_file(str(Path("script") / "gen_ref_pages.py"))

    if "{{cookiecutter.dockerfile}}" != "y":
        remove_file("Dockerfile")
        if "{{cookiecutter.include_github_actions}}" == "y":
            remove_file(str(Path(".github") / "workflows" / "deploy_dev.yml"))
            remove_file(str(Path("script") / "versioning_script.sh"))

    if "{{cookiecutter.codecov}}" != "y":
        remove_file("codecov.yaml")
        if "{{cookiecutter.include_github_actions}}" == "y":
            remove_file(str(Path(".github") / "workflows" / "validate-codecov-config.yml"))

    if "{{cookiecutter.devcontainer}}" != "y":
        remove_dir(".devcontainer")
    
    if "{{cookiecutter.tox}}" != "y":
        remove_file("tox.ini")
