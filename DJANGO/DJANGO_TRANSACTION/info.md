1. run app:
   gunicorn DJANGO.wsgi --bind 0.0.0.0:5100 --workers 8

wrk -t8 -c20 -d20s -s create.lua http://127.0.0.1:5100/create_transaction
