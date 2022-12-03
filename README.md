# Wordle Backend Project3 : API Endpoints

Group 1

Team members:
Vaibhav Rastogi [CWID:885190280]

Prashams Omprakash Daulath [CWID:885582262]


Steps followed to run the project:

1. Initialize the database and start the API:

   ./bin/init.sh

   (Disclaimer! If you do not have permission to execute any of the specified files use the $ chmod 755 (file name) command to change your permissions.) 
   (ex. $ chmod 755 ./bin/init.sh)

2. Populate the data base by running the python script:

   $ python3 dbpop.py

   (warning! If you do not have permission to execute any of the specified files use the $ chmod 755 (file name) command to change your permissions.) 
   (ex. $ chmod 755 ./dbpop.py)

3. Configure Nginx

   go to the directory /etc/nginx/sites-enabled
   create a new config file by typing $ sudo "${EDITOR:-vi}" config

   copy and paste the contents of config-nginx.txt into the file then type :wq

   restart Nginx by typing  $ sudo service nginx restart

4.


5. Start the API
   go back to the directory that holds our project and start the api by typing
   $foreman start --formation wordle=3,user=1





