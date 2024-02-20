install:
	poetry install
	
gendiff:
	poetry run gendiff

test:
	poetry run pytest
	
test-coverage:
	poetry run pytest --cov

build:
	poetry build
	
publish:
	poetry publish --dry-run
		
package-install:
	python3 -m pip install --user dist/*.whl
	
make lint:
	poetry run flake8
