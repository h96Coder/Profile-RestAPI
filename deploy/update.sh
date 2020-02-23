#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/Profiles-RestAPI'

git pull
$PROJECT_BASE_PATH/ python manage.py migrate
$PROJECT_BASE_PATH/ python manage.py collectstatic --noinput
echo "manage done"
supervisorctl restart Profiles_api

echo "DONE! :)"
