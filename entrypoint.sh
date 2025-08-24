#!/bin/sh

# Чекаємо базу
echo "Waiting for Postgres..."
while ! nc -z $HOST $PORT; do
  sleep 1
done
echo "Postgres started"

# Міграції
echo "Applying migrations..."
python manage.py migrate --noinput

# Створення суперкористувача (за змінними середовища)
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
  echo "Creating superuser..."
  python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL || true
fi

exec "$@"
