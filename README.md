# Casting Agency API Read Me

## Introduction
    Hello, and welcome to my Casting Agency API, which is the capstone
    project for the Udacity Full Stack Nanodegree Program. I hope you have
    fun trying out the different endpoints and functionality.

### Motivation for project
    I completed this project as a way to learn more about SQLAlchemy 
    database backends, API building, third-party authorization, and heroku
    deployment. This API was designed to help people in the film industry
    view, edit, create, and delete data about actors and movies. These
    features can aid them in designing new film projects and organizing
    information about previous projects. 

## How to Use

    -Set up the virtual environment for Python by running pip install env 
    
    -Run the activate script for the virtual environment (see this guide: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/ for more help) 

### Project dependencies 
    -Install project dependencies by running `pip install requests`
    -The project dependencies include SQLAlchemy, Flask, Postman 
    and more.
    -Authorization is handled by the third-party service Auth0 and utilizes JWTs. There are three roles: Assistant, Director, and Executive.

### Hosting Instructions
    In order to run the local development server, just input `python app.py` in a terminal while in the root directory of this project.

### Documentation of API behavior and RBAC controls

#### Error Handling

    If an error occurs, it will be returned as a JSON object in this format:

            {
                'success': False,
                'error': 400,
                'message': 'bad request'
            }

    There are five error types: 
        -400: Bad Request
        -401: Unauthorized
        -403: Forbidden
        -404: Resource Not Found 
        -405: Method Not Allowed 
        -422: Not Processable

#### API Endpoints

##### GET /
    -General:
        Used as a way to check the status of the API. No 
        authorization required.
    -Sample
        `curl http://0.0.0.0:8080/movies`
    -Example Return Data
        '{healthy}'    

##### GET /movies
    -General:
        Requires 'get:movies' permissions, which all roles have. Returns a formatted list of all the movies in the
        database, including name, release date, and actors.
        Movies are paginated by 10 and the page number can 
        be changed using queries like `curl http://0.0.0.0:8080/movies?page=2`
    -Sample
        `curl http://0.0.0.0:8080/movies -H "Authorization: Bearer <token>"` (Token value omitted here for confidentiality) 
    -Example Return Data
        {
            "movies": [
                {
                "actors": [
                    "Kate Winslet",
                    "Leonardo DiCaprio"
                ],
                "id": 15,
                "name": "Titanic",
                "release_date": 1999
                },
                {
                "actors": [
                    "Issa Rae",
                    "K. Nanjiani"
                ],
                "id": 25,
                "name": "The Lovebirds",
                "release_date": 2020
                },
                {
                "actors": [
                    "Joseph Gordon-Levitt",
                    "Ellen Page",
                    "Leonardo DiCaprio"
                ],
                "id": 26,
                "name": "Inception",
                "release_date": 2010
                },
                {
                "actors": [
                    "Claire Danes",
                    "Leonardo DiCaprio"
                ],
                "id": 27,
                "name": "Romeo + Juliet",
                "release_date": 1996
                },
                {
                "actors": [
                    "Sergi López",
                    "Maribel Verdú",
                    "Ivana Baquero"
                ],
                "id": 28,
                "name": "El laberinto del fauno",
                "release_date": 2006
                }
            ],
            "success": true,
            "total_movies": 5
            }
##### POST /movies
    -General:
        Requires 'post:movies' permission, which only executives have. Allows the user to create a new movie, with required fields of name, release date, and actors. 
    -Sample
        `curl http://0.0.0.0:8080/movies -H "Authorization: Bearer <token>", "Content-Type: application/json" -X POST -d '{'name': 'Catch Me If You Can', 'release_date': 2002, 'actors': ['Leonardo DiCaprio']}'`     
    -Example Return Data    
        {
            'success': True,
            'created': 40,
            'total_actors': 6
        }

##### PATCH /movies
    -General
        Requires 'patch:movies' permission, which directors and execs have. Allows the user to edit one or all parts of the movie entry. Use the endpoint /movies with the movie id as an argument (see below).
    -Sample
        `curl http://0.0.0.0:8080/movies/25 -H "Authorization: Bearer <token>", "Content-Type: application/json" -X PATCH -d '{'actors': ['Leonardo DiCaprio', 'Tom Hanks']}'`                  
    -Example Return Data
        {
            "edited": 28,
            "success": true,
            "total_movies": 5
        }

##### DELETE /movies
    -General
        Requires 'delete:movies' permission, which only executives have. Allows the user to completely delete an entry from the database.Use the endpoint /movies with the movie id as an argument (see below).
    -Sample
        `curl http://0.0.0.0:8080/movies/25 -H "Authorization: Bearer <token>", "Content-Type: application/json" -X DELETE'`                 
    -Example Return Data
        {
            'success': True,
            'deleted': 25,
            'total_movies': 11
        }

##### GET /actors
    -General
        Requires 'get:actors' permissions, which all roles have. Returns a formatted list of all the actors in the
        database, including name, age, gender, and movies.
        Actor are paginated by 10 and the page number can 
        be changed using queries like `curl http://0.0.0.0:8080/actors?page=2`
    -Sample
        `curl http://0.0.0.0:8080/actors -H "Authorization: Bearer <token>"` (Token value omitted here for confidentiality)                     
        -Example Return Data
                {
                "actors": [
                    {
                    "age": 56,
                    "gender": "male",
                    "id": 1,
                    "movies": [
                        "Titanic",
                        "Inception",
                        "Romeo + Juliet"
                    ],
                    "name": "Leonardo DiCaprio"
                    },
                    {
                    "age": 35,
                    "gender": "female",
                    "id": 3,
                    "movies": [
                        "The Lovebirds"
                    ],
                    "name": "Issa Rae"
                    },
                    {
                    "age": 42,
                    "gender": "male",
                    "id": 4,
                    "movies": [
                        "The Lovebirds"
                    ],
                    "name": "Kumail Nanjiani"
                    },
                    {
                    "age": 39,
                    "gender": "male",
                    "id": 5,
                    "movies": [
                        "Inception"
                    ],
                    "name": "Joseph Gordon-Levitt"
                    },
                    {
                    "age": 33,
                    "gender": "female",
                    "id": 6,
                    "movies": [
                        "Inception"
                    ],
                    "name": "Ellen Page"
                    },
                    {
                    "age": 45,
                    "gender": "female",
                    "id": 7,
                    "movies": [
                        "Titanic"
                    ],
                    "name": "Kate Winslet"
                    },
                    {
                    "age": 55,
                    "gender": "male",
                    "id": 9,
                    "movies": [
                        "Pan's Labyrinth"
                    ],
                    "name": "Sergi López"
                    },
                    {
                    "age": 50,
                    "gender": "female",
                    "id": 12,
                    "movies": [
                        "Pan's Labyrinth"
                    ],
                    "name": "Maribel Verdú"
                    },
                    {
                    "age": 41,
                    "gender": "female",
                    "id": 14,
                    "movies": [
                        "Romeo + Juliet"
                    ],
                    "name": "Claire Danes"
                    },
                    {
                    "age": 25,
                    "gender": "female",
                    "id": 19,
                    "movies": [
                        "Pan's Labyrinth"
                    ],
                    "name": "Ivana Baquero"
                    }
                ],
                "success": true,
                "total_actors": 10
                }

##### POST /actors
    -General:
        Requires 'post:actors' permission, which directors
        and executives have. Allows the user to create a new actor, with required fields of name, age, gender, and movies. 
    -Sample
        `curl http://0.0.0.0:8080/actors -H "Authorization: Bearer <token>", "Content-Type: application/json" -X POST -d '{'name': 'Tom Hanks, 'age': 64, 'gender': 'male', 'movies': ['Catch Me If You Can']}'`     
    -Example Return Data 
        {
            "created": 23,
            "success": true,
            "total_actors": 11
        }

##### PATCH /actors
    -General
        Requires 'patch:actors' permission, which directors and execs have. Allows the user to edit one or all parts of the actor entry. Use the endpoint /actors with the actors id as an argument (see below).
    -Sample
        `curl http://0.0.0.0:8080/actors/25 -H "Authorization: Bearer <token>", "Content-Type: application/json" -X PATCH -d '{'name': 'New Name'}'` 
    -Example Return Data
        {
            "edited": 4,
            "success": true,
            "total_actors": 11
        }

##### DELETE /actors
    -General
        Requires 'delete:actors' permission, which directors and executives have. Allows the user to completely delete an entry from the database. Use the endpoint /actors with the actor id as an argument (see below).
    -Sample
        `curl http://0.0.0.0:8080/actors/25 -H "Authorization: Bearer <token>", "Content-Type: application/json" -X DELETE'`   
    -Example Return Data
        {
            'success': True,
            'deleted': 25,
            'total_movies': 11
        }

### Testing
    -The Postman tests have been exported in the Capstone.json file 
    with fresh tokens. 

    -Unittests can be run by executing `python test_app.py`

### Heroku Server Address:
    The Heroku URL is:
    https://casting-api-for-fsnd.herokuapp.com/

#### Using Heroku: 
    -Log in to Heroku through the terminal or on the Heroku site.
    -Create requirements.txt file for the dependencies
    - Run `pip freeze > requirements` 
    -Set up environmental variables like database URL in setup.sh 
    -Run pip install gunicorn
    -Create a Procfile with the text `web: gunicorn app:app`
    -Use flask_script, flask_migrate, and psycopg2-binary after installing
        with the manage.py file to manage database migrations
    -Don't forget to pip freeze again after downloading new programs
    -Create a Heroku app with `heroku create app_name`
    -Add git remote for Heroku with `git remote add heroku heroku_git_url`
    -Add PostgreSQL with `heroku addons:create heroku-postgresql:hobby-dev
         --app name_of_your_application`
    -Change the database URI from the local one to the Heroku one 
        (found in `heroku config --app app_name)
    -Deploy to Heroku with `git push heroku master`
    -Open the site from the Heroku dashboard or from the CLI with 
        `heroku open`
    -Run migrations after deploying with `heroku run python manage.py db 
        upgrade --app name_of_your_application` Since this app has already 
        been deployed, this last step can be used to deploy changes. 

