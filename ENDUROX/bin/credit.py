#!/usr/bin/env python3

import sys
import endurox as e
import tx_fields as t

class Server:

    def tpsvrinit(self, args):
        e.tplog_info("Doing server init...");
        e.tpadvertise("CREDIT", "CREDIT", Server.CREDIT)
        return 0

    def tpsvrdone(self):
        e.tplog_info("Server shutdown")

    def CREDIT(self, args):
        args.data["data"][t.tx_credit]= "passed"
        return e.tpreturn(e.TPSUCCESS, 0, args.data)


if __name__ == "__main__":
    e.tprun(Server(), sys.argv)
