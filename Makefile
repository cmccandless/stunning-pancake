init:
	@pip install -r requirements.txt

clean:
	@echo -n "Removing all __pycache__ directories..."
	@find . -name __pycache__ | xargs rm -rf
	@echo Done

lint:
	flake8

chmod:
	@chmod +x ./*/*/*.py
	@git update-index --chmod=+x ./*/*/*.py

test: clean
	@time find . -regex "\./[0-9]/[0-9]/[0-9]\.py" | xargs -n 1 python -m pytest -v

test-fast: clean
	@time find . -regex "\./[0-9]/[0-9]/[0-9]\.py" | xargs -n 1 -I % sh -c 'python -m pytest -vx --ff % || exit 255'

test-strict: clean
	@time make test-fast 2>&1 | python ./longer.py 1.0

validate: clean lint test-strict
