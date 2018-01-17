init:
	pip install -r requirements.txt

lint:
	flake8

chmod:
	chmod +x ./*/*/*.py
	git update-index --chmod=+x ./*/*/*.py

test:
	time find . -regex "\./[0-9]/[0-9]" | xargs -n 1 -I % sh -c 'cd %; pwd; python -m pytest -v'

clean:
	find . -name __pycache__ | xargs rm -rf
