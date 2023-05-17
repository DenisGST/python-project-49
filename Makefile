install: 
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain_even

brain-calc:
	poetry run brain_calc

brain-gcd:
	poetry run brain_gcd


build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl 

lint:
	poetry run flake8 brain_games