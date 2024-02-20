install:
	poetry install
	
gendiff:
	poetry run gendiff

build:
	poetry build
	
publish:
	poetry publish --dry-run
		
package-install:
	python3 -m pip install --user dist/*.whl
	
make check:
	poetry run flake8

make test:
        poetry run pytest

test-coverage:
	poetry run coverage report
