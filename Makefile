hello:
	echo "Test first Makefile"
test:
	python -m pytest -vv test_hello.py
install:
	pip install -r requirement.txt
