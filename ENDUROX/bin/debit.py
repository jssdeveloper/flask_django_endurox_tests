#!/usr/bin/env python3

import sys
import endurox as e
import tx_fields as t

class Server:

    def tpsvrinit(self, args):
        e.tplog_info("Doing server init...");
        e.tpadvertise("DEBIT", "DEBIT", Server.DEBIT)
        return 0

    def tpsvrdone(self):
        e.tplog_info("Server shutdown")

    def DEBIT(self, args):
        args.data["data"][t.tx_debit]= "passed"
        return e.tpforward("CREDIT", args.data)
        # return e.tpreturn(e.TPSUCCESS, 0, args.data)

if __name__ == "__main__":
    e.tprun(Server(), sys.argv)
