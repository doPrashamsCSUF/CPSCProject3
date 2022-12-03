#!/bin/sh

sqlite3 ./var/primary/mount/wordle.db < ./share/wordle.sql
sqlite3 ./var/user.db < ./share/user.sql
