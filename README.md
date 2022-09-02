# weight-tracker-api

## Local Setup

1. clone the repo
1. create a new venv `python3 -m venv venv`
1. enter venv `. venv/bin/activate`
1. install dependencies from `pip install -r requirements.txt`
1. to leave the venv `deactivate`

Need to add a new package?

- install said package
- freeze requirements `pip freeze > requirements.txt`

Running the app

- from within the venv run `flask --app tracker --debug run`

Migrate

- initialize db/migrations folder `flask --app tracker db init`
- create a migration `flask --app tracker db migrate -m "Initial migration"`
- run migration `flask --app tracker db upgrade`

Docker

- `docker-compose up --build`
- `docker-compose up -d api`
- `docker-compose up -d db`
  The `-d` flag is optional.
  I leaned on [this article](https://www.tinystacks.com/blog-post/flask-crud-api-with-postgres/) pretty heavily for the docker setup
