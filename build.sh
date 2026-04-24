#!/usr/bin/env bash

pip install -r requirements.txt

cd movie_project   # 👈 ADD THIS LINE

python manage.py collectstatic --noinput
python manage.py migrate