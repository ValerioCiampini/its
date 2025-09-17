M = "ciao"
Mi = int(M.encode("utf-8").hex(), 16)
print(Mi)


messaggio =    "00a26971bd64407aa92b0d2f958d3e"+\
    "a91c3dec6c209cd2dbdf50873d0416"+\
    "7146eb93ba5ee75d03868529349522"+\
    "ce1a6254a9c9bd059133cfa753f061"+\
    "dfd6426b11fdbde7a719212a3c4bc7"+\
    "727418badf6a3ff4babdfb92bf20bf"+\
    "1f9a26252da93204766f2d9da778a0"+\
    "a8469a7ec8a654983b896fb3435e09"+\
    "4474f2927336760799e525702e1644"+\
    "586ea1e252bedf828ab9bb40703946"+\
    "a3471e68c6a4960c805487f12a26da"+\
    "43c566b19fafd52ea0f8a913e76c94"+\
    "5ca454f6e9c96fb8b6dda33094ad44"+\
    "0bd4eb5ad44308d34b1f4f7b58adf1"+\
    "2b3915a839ac5fc66f40182b17f836"+\
    "28b6ef72f7e49ef397ea21d250ce30"+\
    "79cc80eaa7ba5b1fb7a5f61270aa4c"+\
    "78ad"

decimale = int(messaggio, 16)

e = 3

print(pow(Mi, e, decimale))

m = "Ciao come va"

Mi1 = int(m.encode("utf-8").hex(), 16)

