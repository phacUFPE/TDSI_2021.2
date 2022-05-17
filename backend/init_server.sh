#!/bin/sh

export FAILURE_PORT=5050
export BACKUP_PORT=5055

kill -9 `sudo lsof -t -i:$FAILURE_PORT`
kill -9 `sudo lsof -t -i:$BACKUP_PORT`

gnome-terminal -- bash -c "cd '$PROJECT_DIRECTORY' && flask run --port='$FAILURE_PORT'; exec bash"
gnome-terminal -- bash -c "cd '$PROJECT_DIRECTORY' && flask run --port='$BACKUP_PORT'; exec bash"
