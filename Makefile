install:
	poetry install
	
gendiff:
	poetry run gendiff
	
test-coverage:
        poetry run coverage run -m pytest
	poetry run coverage report

build:
	poetry build
	
publish:
	poetry publish --dry-run
		
package-install:
	python3 -m pip install --user dist/*.whl
	
make check:
	poetry run flake8
        poetry run pytest
