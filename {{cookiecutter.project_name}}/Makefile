.PHONY: install
install: ## Install the poetry environment and install the pre-commit hooks
	@echo "🆕 Creating virtual environment using poetry"
	@poetry install --no-interaction
	@poetry run pre-commit install
	@poetry shell

.PHONY: install-only
install-only: ## Only install the poetry environment
	@echo "🆕 Creating virtual environment using poetry"
	@poetry install --no-interaction

.PHONY: update
update: ## Resolve all dependencies of the project and write the exact versions into poetry.lock
	@echo "🚀 Updating virtual environment and poetry.lock based on pyproject.toml"
	@poetry update

.PHONY: remove-env
remove-env: ## Remove the virtual enviroment created using poetry
	@echo "🗑️ Removing the virtual enviroment created using poetry"
	@poetry env remove --all

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Linting code: Running pre-commit"
	@poetry run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@poetry run mypy --install-types --non-interactive

.PHONY: poetry-lock
poetry-lock: ## Generate new poetry.lock file
	@echo "🚀 Generating new Poetry lock file consistent with 'pyproject.toml'"
	@poetry lock --no-update

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest tests -vv{%- if cookiecutter.codecov == 'y' %} --cov --cov-config=pyproject.toml --cov-report=xml{%- endif %}

.PHONY: build
build: clean-build ## Build wheel file using poetry
	@echo "🚀 Creating wheel file"
	@poetry build

.PHONY: clean-build
clean-build: ## clean build artifacts
	@rm -rf dist

{% if cookiecutter.mkdocs == 'y' -%}
.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@poetry run mkdocs build -s

.PHONY: docs
docs: ## Build and serve the documentation
	@poetry run mkdocs serve

.PHONY: docs-deploy
docs-deploy: ## Deploy the documentation on Github pages
	@poetry run mkdocs gh-deploy --force
{%- endif %}

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
