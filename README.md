# Wordle Backend Project1 : API Endpoints

Group 4 team members:

Steps to run the project:

1. Initialize the database and start the API:

   ./bin/init.sh

2. Populate the data base by running the python script:

   dbpop.py

3. Start the API by running

   foreman start

4. Go to local.gd docs to view and test all the endpoints

   http://wordle.local.gd:5000/docs




spmccarthy4@mirdiland:~/cpsc449/Project2/449-proj-2$ http --auth jm:pass --auth-type basic GET http://mirdiland/login/ 

HTTP/1.1 200 
Connection: keep-alive
Content-Length: 23
Content-Type: application/json0
Date: Wed, 16 Nov 2022 00:24:13 GMT
Server: nginx/1.18.0 (Ubuntu)
password: pass
username: jm

{
    "authenticated": true
}


spmccarthy4@mirdiland:~/cpsc449/Project2/449-proj-2$ http --auth syr:pass --auth-type basic POST http://mirdiland/games/ username="syr" 

HTTP/1.1 201 
Connection: keep-alive
Content-Length: 59
Content-Type: application/json
Date: Wed, 16 Nov 2022 00:19:54 GMT
Server: nginx/1.18.0 (Ubuntu)

{
    "answerid": 1221,
    "gameid": 15,
    "username": "syr"
}

spmccarthy4@mirdiland:~/cpsc449/Project2/449-proj-2$ http POST http://mirdiland/users/ first_name="sean" last_name="yvesroy" user_name="syr" password="pass"

HTTP/1.1 201 
Connection: keep-alive
Content-Length: 107
Content-Type: application/json
Date: Wed, 16 Nov 2022 00:05:58 GMT
Server: nginx/1.18.0 (Ubuntu)

{
    "first_name": "sean",
    "id": 3,
    "last_name": "yvesroy",
    "password": "pass",
    "user_name": "syr"
}


spmccarthy4@mirdiland:~/cpsc449/Project2/449-proj-2$ http --auth jm:pass --auth-type basic POST http://mirdiland/guess/ gameid="13" word="almes"

HTTP/1.1 201 
Connection: keep-alive
Content-Length: 56
Content-Type: application/json
Date: Wed, 16 Nov 2022 00:04:01 GMT
Server: nginx/1.18.0 (Ubuntu)

{
    "Accuracy": "✓XXXX",
    "guessedWord": "almes"
}




