
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python3 -m pytest -v test.py

lint:
	pylint app.py --disable=missing-docstring,C0305

all: install lint test