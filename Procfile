web: daphne django_chatroom.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=django_chatroom.settings -v2