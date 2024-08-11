# Fast API Playground Repository

Welcome to my FastAPI Learning repository! This repository is dedicated to helping me learn and practice FastAPI. It contains a variety of exercises and tutorial codes designed to enhance my understanding of FastAPI.

## Topics

- Python Refresher

## Important Commands

- To run a FastAPI file using `uvicorn`, use the following command:

```bash
uvicorn <file_name>:<fastapi_app> --reload
```

`--reload` makes sure that after making the changes, the FastAPI app reloads automatically.

- To run a FastAPI file using `fastapi`, use the following command:

```bash
fastapi run <file_name> # This will run the app in production mode.
fastapi dev <file_name> # This will run the app in development mode.
```

> To see all the routes of an API, use `/docs` route.

## Sqlite Database Commands

- `sqlite3 <database_name.db>` to run the database in terminal.
- `.schema` to see the database schemas.
- Here, you can use SQL commands to insert, delete, update and see the data.
- Different `.mode` can be used to see the database in different formats.
  > .mode column <br />
  > .mode markdown <br />
  > .mode box <br />
  > .mode table <br />

## Alembic setup

- To setup alembic, use the command: `alembic init alembic`.
- To revise the database using alembic, use the command: `alembic revision -m '<Your_Message>'`
- To upgrade - write upgrade function to upgrade the database and run the command `alembic upgrade <revision_id>`. `revision_id` will be created in the previous step.
- To downgrade - write downgrade function to downgrade the database and run the command `alembic downgrade -1`.

## Pytest setup

- If you have only one test file, then you can run that test file using `pytest` command only.
- If you have multiple test files, then to run a test file, use the command: `pytest <file_name.py>`

## Credits

This repository follows the Udemy Course [FastAPI - The Complete Course 2024 (Beginner + Advanced)](https://www.udemy.com/course/fastapi-the-complete-course/) by [Eric Roby](https://www.udemy.com/user/ericroby2/) and [Chad Darby](https://www.udemy.com/user/chaddarby2/).
