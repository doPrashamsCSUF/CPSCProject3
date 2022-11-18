# Wordle Backend Project2 : API Endpoints

Group 1 team members:
Krishna Bhatia
Mohamed Habarneh
Sean McCarthy

Steps to run the project:

1. Initialize the database and start the API:

   ./bin/init.sh

   (warning! If you do not have permission to execute any of the specified files use the $ chmod 755 (file name) command to change your permissions.) 
   (ex. $ chmod 755 ./bin/init.sh)

2. Populate the data base by running the python script:

   ./dbpop.py

   (warning! If you do not have permission to execute any of the specified files use the $ chmod 755 (file name) command to change your permissions.) 
   (ex. $ chmod 755 ./dbpop.py)

3. Configure Nginx

   go to the directory /etc/nginx/sites-enabled
   create a new config file by typing $ sudo "${EDITOR:-vi}" config
   copy and paste the contents of config-nginx.txt into the file then type :wq
   restart Nginx by typing  $ sudo service nginx restart


4. Start the API
   go back to the directory that holds our project and start the api by typing
   $foreman start --formation wordle=3,user=1

Login 
   $ http --auth <username>:<password> GET http://tuffix-vm/login/ 

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

Create a new game
   $ http --auth <username>:<password> POST http://tuffix-vm/games/ username="syr" 

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

Create a new user
   $ http POST http://tuffix-vm/users/ first_name="<First name>" last_name="<Last name>" user_name="<user name>" password="<password>"

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

Make a guess
   $ http --auth jm:pass POST http://tuffix-vm/guess/ gameid="13" word="almes"

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

Look up a specific gamestate
   $ http --auth <username>:<password> GET http://tuffix-vm/games/ gameid="16" 
   
      HTTP/1.1 200 
      Connection: keep-alive
      Content-Length: 151
      Content-Type: application/json
      Date: Wed, 16 Nov 2022 03:32:52 GMT
      Server: nginx/1.18.0 (Ubuntu)

      [
         {
            "accuracy": "O✓XXX",
            "gameid": 16,
            "gstate": "In-progress",
            "guessedword": "almes",
            "guesses": 1,
            "guessid": 4
         }
      ]

Retrieve a list of active games for a user
   $ http --auth <username>:<password> GET http://tuffix-vm/games/all/ 
   
      HTTP/1.1 200 
      Connection: keep-alive
      Content-Length: 1015
      Content-Type: application/json
      Date: Wed, 16 Nov 2022 03:30:41 GMT
      Server: nginx/1.18.0 (Ubuntu)

      [
         {
            "gameid": 1,
            "gstate": "In-progress",
            "guesses": 0
         },
         {
            "gameid": 16,
            "gstate": "In-progress",
            "guesses": 0
         }
      ]




