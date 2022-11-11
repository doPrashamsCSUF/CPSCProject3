PRAGMA foreign_KEYs=ON;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS game;
CREATE TABLE game(
    gameid INTEGER PRIMARY KEY AUTOINCREMENT,
    guesses INTEGER,
    gstate VARCHAR(12)
);


DROP TABLE IF EXISTS games;
CREATE TABLE games (
    gamesid INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(25),
    answerid INTEGER,
    gameid INTEGER,
    FOREIGN KEY (answerid) REFERENCES answer(answerid),
    FOREIGN KEY(gameid) REFERENCES game(gameid)
);

DROP TABLE IF EXISTS guess;
CREATE TABLE guess(
    guessid INTEGER PRIMARY KEY AUTOINCREMENT,
    gameid INTEGER,
    guessedword VARCHAR(5),
    accuracy VARCHAR(5),
    FOREIGN KEY(gameid) REFERENCES game(gameid)
);

DROP TABLE IF EXISTS answer;
CREATE TABLE answer(
    answerid INTEGER PRIMARY KEY AUTOINCREMENT,
    answord VARCHAR(5)
);

DROP TABLE IF EXISTS valid_word;
CREATE TABLE valid_word(
    valid_id INTEGER PRIMARY KEY AUTOINCREMENT,
    valword VARCHAR(5)
);
COMMIT;
