#!/bin/sh
python manage.py migrate
python manage.py collectstatic --link --no-input

echo "DJANGO_SUPERUSER_EMAIL: $DJANGO_SUPERUSER_EMAIL"

if [ "$DJANGO_SUPERUSER_EMAIL" ] && [ "$DJANGO_SUPERUSER_PHONE_NUMBER" ]; then
    python manage.py createsuperuser \
        --noinput \
        --phone_number $DJANGO_SUPERUSER_PHONE_NUMBER \
        --email $DJANGO_SUPERUSER_EMAIL
    echo "Superuser with email: $DJANGO_SUPERUSER_EMAIL and phone:$DJANGO_SUPERUSER_PHONE_NUMBER created"
fi

exec "$@"