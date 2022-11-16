#!/bin/sh

sqlite3 ./var/wordle.db < ./share/wordle.sql
sqlite3 ./var/user.db < ./share/user.sql