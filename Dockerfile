FROM python:3.9-slim-buster

WORKDIR /tracker-api

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

# CMD ["flask", "run", "--host=0.0.0.0"]

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
