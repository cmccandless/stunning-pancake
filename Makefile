init:
	- pip install -r requirements.txt

lint:
	- flake8

chmod:
	- chmod +x ./*/*/*.py
	- git update-index --chmod=+x ./*/*/*.py
