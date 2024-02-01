RUN DJANGO_CREDIT gunicorn DJANGO_CREDIT.wsgi --bind 0.0.0.0:3001 --workers 8
RUN DJANGO_DEBIT gunicorn DJANGO_DEBIT.wsgi --bind 0.0.0.0:3002 --workers 8
RUN DJANGO_TRANSACTION gunicorn DJANGO.wsgi --bind 0.0.0.0:3000 --workers 8

1. test : Create Transsaction. RUN $ wrk -t8 -c20 -d20s -s create.lua http://127.0.0.1:3000/create_transaction

2. test : Send transaction to /creditdebit, connect to credit & debit api.
   RUN $ wrk -t8 -c20 -d20s -s creditdebit.lua http://127.0.0.1:3000/creditdebit
