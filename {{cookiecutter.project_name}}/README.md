# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## 1. Getting Started

1. Clone the repository to your desired directory:

    ```bash
    cd <directory_in_which_repo_should_be_created>
    git clone https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}.git
    cd {{cookiecutter.project_name}}
    ```

2. Activate your Python environment (Python {{cookiecutter.target_python_version}} version is recommended).

3. Install Poetry for dependency management:

    ```bash
    python -m pip install --upgrade pip
    pip install poetry=={{cookiecutter.poetry_version}}
    ```

4. Install the project dependencies and set up pre-commit hooks:

    ```bash
    make install
    ```

Now, you are prepared to embark on the development of new features for the project.



## 2. Contributiong

1. **Branch Creation:**
    Start by creating a new branch from the `/main` branch using the following format:
    ```
    {% raw %}git checkout -b feature/DP-{{JiraTaskID}}-{{JiraTaskName}}{% endraw %}
    ```
    Proceed with the implementation of the new feature within this branch.

2. **Run Pre-commit Hooks:**
    Ensure adherence to coding best practices by running pre-commit hooks, which utilize `black` as a code formatter and `ruff` as a linter.
    To evaluate the code quality before committing your changes, execute the following command to trigger pre-commit hooks and perform static code analysis using `mypy`:

    ```bash
    make check
    ```

3. **Run Unit Tests:**
    Validate that your changes have not adversely affected existing code by running unit tests with `pytest`:

    ```bash
    make test
    ```

    Alternatively, execute a comprehensive test matrix with different Python versions using `tox`:

    ```bash
    tox
    ```

Once these steps are completed successfully, proceed to commit and push your changes. The CI/CD pipeline will automatically trigger upon the creation of a pull request, merging to the main branch, or the creation of a new release.

{% if cookiecutter.dockerfile == "y" -%}
## 3. CI/CD

In this project, Docker is employed to containerize the application and enhance deployment efficiency.
The CI/CD pipeline is responsible for automatically building the Docker image and pushing it to the Amazon Elastic Container Registry (ECR) with a given tag, based of the [development cycle](https://giorgioarmani.atlassian.net/wiki/spaces/DP/pages/2083717150/Development+Process#Development-cycle) described on Confluence.

For testing purposes, a docker image can be builted from any branch with a custom tag triggering the workflow declared by [Deploy dev - Workflow](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/deploy_dev.yml).

There is also a possibility to build a docker image in prod enviroment (only starting form a release branch) using the workflow declared by [Deploy prod - Workflow](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/actions/workflows/deploy_prod.yml).
{%- endif %}


---
### Credits
Repository initiated with [ga-data-strategy-analytics/cookiecutter-python-template](https://github.com/ga-data-strategy-analytics/cookiecutter-python-template).
