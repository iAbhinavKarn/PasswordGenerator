FROM python:3.9-alpine

RUN apk update

WORKDIR /code
COPY main.py /code
COPY requirements.txt /code

RUN pip install -r /code/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]