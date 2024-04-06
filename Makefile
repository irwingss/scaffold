install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
install-azure:
	pip install --upgrade pip &&\
		pip install -r requirements-azure.txt

lint:
	pylint --disable=R,C hello.py

test:
	python3 -m pytest -vv --cov=hello test_hello.py
	
all: install lint test