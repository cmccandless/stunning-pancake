init:
	pip install -r requirements.txt

lint:
	flake8

chmod:
	chmod +x ./*/*/*.py
	git update-index --chmod=+x ./*/*/*.py

test:
	time find . -regex "\./[0-9]/[0-9]" | xargs -n 1 -I % sh -c 'cd %; pwd; python -m pytest -v'

test-fast:
	time find . -regex "\./[0-9]/[0-9]" | xargs -n 1 -I % sh -c 'cd %; pwd; python -m pytest -vx --ff || exit 255'

clean:
	find . -name __pycache__ | xargs rm -rf
