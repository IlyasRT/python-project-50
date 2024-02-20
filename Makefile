install:
	poetry install
	
gendiff:
	poetry run gendiff
	
test-coverage:
	poetry run coverage report

build:
	poetry build
	
publish:
	poetry publish --dry-run
		
package-install:
	python3 -m pip install --user dist/*.whl
	
make check:
	poetry run flake8

test:
        poetry run pytest
