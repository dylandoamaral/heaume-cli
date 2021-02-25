lint:
	@poetry run pylint heaume_cli tests

isort:
	@poetry run isort heaume_cli tests

format:
	@poetry run black heaume_cli tests

tidy: isort format

check: lint
	@poetry run black heaume_cli tests --check
	@poetry run isort heaume_cli tests --check

test:
	@poetry run pytest --cov=heaume_cli --cov-config .coveragerc --cov-report=xml --cov-report=term tests/