create transaction
wrk -t8 -c20 -d20s -s create_enduro.lua http://127.0.0.1:3100/create_transaction

wrk -t8 -c20 -d20s -s creditdebit_enduro.lua http://127.0.0.1:3100/creditdebit
