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

## Credits

This repository follows the Udemy Course [FastAPI - The Complete Course 2024 (Beginner + Advanced)](https://www.udemy.com/course/fastapi-the-complete-course/) by [Eric Roby](https://www.udemy.com/user/ericroby2/) and [Chad Darby](https://www.udemy.com/user/chaddarby2/).
