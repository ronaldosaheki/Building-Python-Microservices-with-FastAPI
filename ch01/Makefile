install-fastapi:
	python -m pip install --upgrade pip
	pip install fastapi
	pip install uvicorn[standard]
	pip install python-multipart

run-minimal: install-fastapi
	uvicorn minimal:app --reload

install-main-requirements:
	pip install -r requirements.txt

run-main: install-main-requirements
	uvicorn main:app --reload


