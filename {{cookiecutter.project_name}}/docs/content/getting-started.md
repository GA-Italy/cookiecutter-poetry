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
