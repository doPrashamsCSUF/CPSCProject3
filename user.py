from email.policy import HTTP
import databases
import dataclasses
import sqlite3

import databases

from quart import Quart, g, request, abort, Response
from quart_schema import QuartSchema, validate_request

app = Quart(__name__)
QuartSchema(app)

@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    user_name: str
    password: str

async def _get_db():
    db = getattr(g, "_sqlite_db", None)
    if db is None:
        db = g._sqlite_db = databases.Database('sqlite+aosqlite:/var/user.db')
        await db.connect()
    return db


@app.teardown_appcontext
async def close_connection(exception):
    db = getattr(g, "_sqlite_db", None)
    if db is not None:
        await db.disconnect()
        

@app.route("/users/", methods=["POST"])
@validate_request(User)
async def create_user(data):
    db = await _get_db()
    user = dataclasses.asdict(data)
    try:
        #Attempt to create new user in database
        id = await db.execute(
            """
            INSERT INTO user(fname, lname, username, passwrd)
            VALUES(:first_name, :last_name, :user_name, :password)
            """,
            user,
        )
    #Return 409 error if username is already in table
    except sqlite3.IntegrityError as e:
        abort(409, e)

    user["id"] = id
    return user, 201

# User authentication endpoint
@app.route("/login/", methods=["GET"])
#@validate_request(Credentials)
async def userAuth():
    db = await _get_db()
    info = request.authorization
    # Selection query with raw queries
    # Run the command
    if info:
        try:
            result = await db.fetch_one( "SELECT * FROM user WHERE username= :username AND passwrd= :password",info, )
            #app.logger.info( "SELECT * FROM user WHERE username= :username AND passwrd= :password",info, )
    # Is the user registered?
            if result is None:
                return Response(headers={'WWW-Authenticate':'Basic realm="Login Required"'},status=401) 
        except sqlite3.IntegrityError as e:
            abort(409,e)
        return Response(headers={'Authenticated' : True, 'WWW-Authenticate': 'Basic realm="User Visible Realm"', 'Username' : info['username'],'password': info['password']}, status=200)
    else:
        return Response(headers={'WWW-Authenticate':'Basic realm="Login Required"'},status=401) 