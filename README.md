# weight-tracker-api

## Local Setup

1. clone the repo
1. create a new venv `python3 -m venv venv`
1. enter venv `. venv/bin/activate`
1. install dependencies from `pip install -r requirements.txt`
1. to leave the venv `deactivate`

### Need to add a new package?

- install said package
- freeze requirements `pip freeze > requirements.txt`

### Running the app

- from within the venv run `flask --app tracker --debug run`

### Migrate

- initialize db/migrations folder `flask --app tracker db init`
- create a migration `flask --app tracker db migrate -m "Initial migration"`
- run migration `flask --app tracker db upgrade`
- migrate down `flask --app tracker db downgrade`

### Migrate inside Docker (this is the prefered way)

- make sure you imported the modle into the `__init__.py` file
- have docker containers running
- enter the api container `docker exec -it tracker-api bash`
- create the migration `flask --app tracker db migrate -m "migration_name"`
- restart the docker container `docker-compose up` (might not be nessessary)

### Enter psql inside Docker

- `docker exec -it tracker-db bash`
- `psql -U <POSTGRES_USER> <POSTGRES_DB>` you can get those from the docker-compose file
- list tables `\dt`
- describe table `\d <table_name>`
- to get users modify the query to be `select * from "user";`

### Docker

- `docker-compose up --build`
- `docker-compose up -d api`
- `docker-compose up -d db`
  The `-d` flag is optional.
  I leaned on [this article](https://www.tinystacks.com/blog-post/flask-crud-api-with-postgres/) pretty heavily for the docker setup

### Seed Database

1. Have docker Running
1. Enter the docker api container with: `docker exec -it tracker-api bash`
1. Run `flask seed_db`

### Swagger

- `http://localhost:5000/swagger-ui/`
- as you create new blueprints add their names to the `blueprints_to_add_to_swagger` list in `__init__.py`
- group endpoints with the `@doc(tags=[''])` decorator

## SQLAlchemy Notes

### Filter
Much more robust
`db.users.filter(db.users.name == 'Joe')`

### Filter_By
`db.users.filter_by(name='Joe')`