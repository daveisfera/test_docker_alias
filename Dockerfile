FROM python:3.9.25-slim-trixie

WORKDIR /usr/src/app

COPY main.py test.py /usr/src/app/

CMD ["python3", "main.py"]
