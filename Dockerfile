FROM python:3.9.23-slim-bookworm

WORKDIR /usr/src/app

COPY main.py test.py /usr/src/app/

CMD ["python3", "main.py"]
