FROM python:3.6.4

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system

COPY . /app

CMD ["python", "main.py", "/input", "/output"]
