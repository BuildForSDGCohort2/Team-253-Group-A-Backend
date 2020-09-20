FROM python:3.6.4

WORKDIR /app

RUN pip install pipenv

ADD Pipfile .
ADD Pipfile.lock .

RUN pipenv install --system

ADD . /app

CMD ["python", "main.py", "/input", "/output"]