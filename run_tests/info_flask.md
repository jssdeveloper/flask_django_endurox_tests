Run all instances in separate terminal window
RUN CREDIT $ gunicorn --bind 0.0.0.0:3001 -w 8 wsgi:app
RUN DEBIT $ gunicorn --bind 0.0.0.0:3002 -w 8 wsgi:app
RUN TRANSACTION $ gunicorn --bind 0.0.0.0:3000 -w 8 wsgi:app


1. test : Create Transsaction. RUN $ wrk -t8 -c20 -d20s -s create.lua http://127.0.0.1:3000/create_transaction

2. test : Send transaction to /creditdebit, connect to credit & debit api.
RUN $ wrk -t8 -c20 -d20s -s creditdebit.lua http://127.0.0.1:3000/creditdebit
