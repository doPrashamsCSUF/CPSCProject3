import dataclasses

import redis


# Necessary quart imports

from quart import Quart, request

from quart_schema import QuartSchema, validate_request


app = Quart(__name__)

QuartSchema(app)


# Initialize redis client

redisClient = redis.Redis(host='localhost', port=6379, db=0, charset='utf-8', decode_responses=True)


@dataclasses.dataclass

class LeaderInfo:

    result: str

    guesses: int

# Results endpoint

@app.route("/results/", methods=["POST"])

@validate_request(LeaderInfo)

async def Results(data: LeaderInfo):

    auth = request.authorization

    if auth and auth.username and auth.password:

        boardData = dataclasses.asdict(data)

        score = 0
        count = 1
        if boardData["result"] == "Win":

            if boardData["guesses"] == 1:
                score = 6
            elif boardData["guesses"] == 2:
                score = 5
            elif boardData["guesses"] == 3:
                score = 4
            elif boardData["guesses"] == 4:
                score = 3
            elif boardData["guesses"] == 5:
                score = 2
            elif boardData["guesses"] == 6:
                score = 1
            else:
                return {"Error": "Invalid Guesses."}, 404
        elif boardData["result"] == "Loss":
            score = 0
        else:
            return {"Error": "Invalid Result."}, 404

        if redisClient.hget('leaderboardGame', 'username') == auth.username:
            score = int(redisClient.hget('leaderboardGame', 'score')) + score
            count = int(redisClient.hget('leaderboardGame', 'gamecount')) + count
            averageScore = score / count

            result = redisClient.hset('leaderboardGame', 'averageScore', averageScore)
            result = redisClient.hset('leaderboardGame', 'result',boardData["result"])
            result = redisClient.hset('leaderboardGame', 'guesses',boardData["guesses"])
            result = redisClient.hset('leaderboardGame', 'score', score)
            result = redisClient.hset('leaderboardGame', 'gamecount', count)
            result2 = redisClient.zadd("leaderboardGame score ", {auth.username: averageScore})


        else:

            result = redisClient.hset('leaderboardGame', 'username' , auth.username)
            result = redisClient.hset('leaderboardGame', 'averageScore', score)
            result = redisClient.hset('leaderboardGame', 'result',boardData["result"])
            result = redisClient.hset('leaderboardGame', 'guesses',boardData["guesses"])
            result = redisClient.hset('leaderboardGame', 'score', score)
            result = redisClient.hset('leaderboardGame', 'gamecount', count)
            result2 = redisClient.zadd("leaderboardGamescore", {auth.username: score})


        return redisClient.hgetall('leaderboardGame'), 200

    else:
        return (
            {"error": "User not verified"},
            401,
            {"WWW-Authenticate": 'Basic realm = "Login required"'},
        )


@app.route("/top-scores/", methods=["GET"])

async def topScores():



    topScores = redisClient.zrange("leaderboardGamescore", 0, 9, desc = True, withscores = True)


    if topScores != []:

        return ('\n'.join(map(str, topScores))), 200

    else:

        return {"Error": "Database empty."}, 404

