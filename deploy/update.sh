#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/Profiles-RestAPI'

git pull
$PROJECT_BASE_PATH/ py manage.py migrate
$PROJECT_BASE_PATH/ py manage.py collectstatic --noinput
supervisorctl restart Profiles_api

echo "DONE! :)"
