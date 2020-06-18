#Casting Agency API Read Me

##Introduction
    Hello, and welcome to my Casting Agency API, which is the capstone
    project for the Udacity Full Stack Nanodegree Program. I hope you have
    fun trying out the different endpoints and functionality.

    ###Motivation for project
        I completed this project as a way to learn more about SQLAlchemy 
        database backends, API building, third-party authorization, and heroku
        deployment. This API was designed to help people in the film industry
        view, edit, create, and delete data about actors and movies. These
        features can aid them in designing new film projects and organizing
        information about previous projects. 

    ##How to Use

        -Set up the virtual environment for Python by running pip install env -Run the activate script for the virtual environment (see this guide: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/ for more help) 
  
    ###Project dependencies 
        -Install project dependencies by running `pip install requests`
        -The project dependencies include SQLAlchemy, Flask, Postman 
        and more.
        -Authorization is handled by the third-party service Auth0 and utilizes JWTs. There are three roles: Assistant, Director, and Executive.

    ###Hosting Instructions
       Detailed instructions for scripts to install any project dependencies, and to run the development server.

    ###Documentation of API behavior and RBAC controls

        ####Error Handling

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

        ####API Endpoints

            #####GET /
                -General:
                    Used as a way to check the status of the API. No 
                    authorization required.
                -Sample
                    `curl http://0.0.0.0:8080/movies`
                -Example Return Data
                    '{healthy}'    
            #####GET /movies
                -General:
                    Requires 'get:movies' permissions, which all roles have. Returns a formatted list of all the movies in the
                    database, including name, release date, and actors.
                    Movies are paginated by 10 and the page number can 
                    be changed using queries like `curl http://0.0.0.0:8080/movies?page=2`
                -Sample
                    `curl http://0.0.0.0:8080/movies -H "Authorization: Bearer <token>"` (Token value omitted here for confidentiality) 
                -Example Return Data

            #####POST /movies
                -General:
                    Requires 'post:movies' permission, which only executives have. Allows the user to create a new movie, with required fields of name, release date, and actors. 
                -Sample
                    `curl http://0.0.0.0:8080/movies -H "Authorization: Bearer <token>", "Content-Type: application/json" -X POST -d '{'name': 'Catch Me If You Can', 'release_date': 2002, 'actors': ['Leonardo DiCaprio']}'`     
                -Example Return Data    
            #####PATCH /movies
                -General
                    Requires 'patch:movies' permission, which directors and execs have. Allows the user to edit one or all parts of the movie entry. Use the endpoint /movies with the movie id as an argument (see below).
                -Sample
                    `curl http://0.0.0.0:8080/movies/25 -H "Authorization: Bearer <token>", "Content-Type: application/json" -X PATCH -d '{'actors': ['Leonardo DiCaprio', 'Tom Hanks']}'`                  
                -Example Return Data
            #####DELETE /movies
                -General
                    Requires 'delete:movies' permission, which only executives have. Allows the user to completely delete an entry from the database.Use the endpoint /movies with the movie id as an argument (see below).
                -Sample
                    `curl http://0.0.0.0:8080/movies/25 -H "Authorization: Bearer <token>", "Content-Type: application/json" -X DELETE'`                 
                -Example Return Data
            #####GET /actors
                -General
                    Requires 'get:actors' permissions, which all roles have. Returns a formatted list of all the actors in the
                    database, including name, age, gender, and movies.
                    Actor are paginated by 10 and the page number can 
                    be changed using queries like `curl http://0.0.0.0:8080/actors?page=2`
                -Sample
                    `curl http://0.0.0.0:8080/actors -H "Authorization: Bearer <token>"` (Token value omitted here for confidentiality)                     
                -Example Return Data
                
            #####POST /actors
                -General:
                    Requires 'post:actors' permission, which directors
                    and executives have. Allows the user to create a new actor, with required fields of name, age, gender, and movies. 
                -Sample
                    `curl http://0.0.0.0:8080/actors -H "Authorization: Bearer <token>", "Content-Type: application/json" -X POST -d '{'name': 'Tom Hanks, 'age': 64, 'gender': 'male', 'movies': ['Catch Me If You Can']}'`     
                -Example Return Data 
            #####PATCH /actors
                -General
                    Requires 'patch:actors' permission, which directors and execs have. Allows the user to edit one or all parts of the actor entry. Use the endpoint /actors with the actors id as an argument (see below).
                -Sample
                    `curl http://0.0.0.0:8080/actors/25 -H "Authorization: Bearer <token>", "Content-Type: application/json" -X PATCH -d '{'name': 'New Name'}'` 
                -Example Return Data
            #####DELETE /actors
                -General
                    Requires 'delete:actors' permission, which directors and executives have. Allows the user to completely delete an entry from the database. Use the endpoint /actors with the actor id as an argument (see below).
                -Sample
                    `curl http://0.0.0.0:8080/actors/25 -H "Authorization: Bearer <token>", "Content-Type: application/json" -X DELETE'`   
                -Example Return Data

        -The Postman tests have been exported in the Capstone.json file 
        with fresh tokens. 

        -Unittests can be run by executing `python test_app.py`

    ###Heroku Server Address:
        https://casting-api-for-fsnd.herokuapp.com/ | 
        https://git.heroku.com/casting-api-for-fsnd.git

        Using Heroku: 

