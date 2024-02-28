setup:
	python -m venv flask-ml-azure
	source flask-ml-azure/Scripts/activate
	
install:
	pip install -r requirements.txt

test:
	python -m pytest -v test.py

start:
	python app.py

lint:
	pylint app.py --disable=missing-docstring,C0305

docker-build:
	docker build -t my-python-flask-app .

docker-run:
	docker run -p 5000:5000 my-python-flask-app

docker-debug:
	#to debug inside the container
	docker run -d -p 5000:5000 --name my-flask-container my-python-flask-app
	docker exec -it my-flask-container bash

docker-clean:
	#remove all images locally
	if [ -n "$$(docker images -aq)" ]; then \
		docker rmi -f $$(docker images -aq); \
	fi
