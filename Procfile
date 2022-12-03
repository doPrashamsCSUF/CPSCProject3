primary:./bin/litefs -config ./etc/primary.yml
secondary1:./bin/litefs -config ./etc/secondary1.yml
secondary2:./bin/litefs -config ./etc/secondary2.yml
leaderBoard: hypercorn leaderBoard --reload --debug --bind leaderBoard.local.gd:$PORT --access-logfile - --error-logfile - --log-level DEBUG
