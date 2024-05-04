import re
import sys

PROJECT_NAME_REGEX = r"^[-a-zA-Z][-a-zA-Z0-9]+$"
project_name = "{{cookiecutter.project_name}}"
if not re.match(PROJECT_NAME_REGEX, project_name):
    print(
        "ERROR: The project name (%s) is not a valid Python module name. Please do not use a _ and use - instead"
        % project_name
    )
    # Exit to cancel project
    sys.exit(1)

PROJECT_SLUG_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
project_slug = "{{cookiecutter.project_slug}}"
if not re.match(PROJECT_SLUG_REGEX, project_slug):
    print(
        "ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead"
        % project_slug
    )
    # Exit to cancel project
    sys.exit(1)

TARGET_PYTHON_VERSION_REGEX = r"^3\.(8|9|10|11)$"
target_python_version = "{{cookiecutter.target_python_version}}"
if not re.match(TARGET_PYTHON_VERSION_REGEX, target_python_version):
    print(
        "ERROR: The target python version (%s) is not a valid Python version."
        % target_python_version
    )
    # Exit to cancel project
    sys.exit(1)