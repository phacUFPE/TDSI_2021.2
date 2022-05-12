#!/bin/sh

kill -9 `sudo lsof -t -i:$FAILURE_PORT`
kill -9 `sudo lsof -t -i:$BACKUP_PORT`

gnome-terminal -- bash -c "cd '$PROJECT_DIRECTORY' && flask run --port='$FAILURE_PORT'; exec bash"
gnome-terminal -- bash -c "cd '$PROJECT_DIRECTORY' && flask run --port='$BACKUP_PORT'; exec bash"
