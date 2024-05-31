install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip --user install dist/*.whl

lint:
	poetry run flake8 brain_games

full_install: install build publish package-install