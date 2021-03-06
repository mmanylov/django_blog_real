#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
# docker-compose exec app python manage.py flush --no-input
#python manage.py flush --no-input
# docker-compose exec app python manage.py migrate
#python manage.py migrate


exec "$@"