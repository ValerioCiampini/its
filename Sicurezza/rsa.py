n_nd = """00ab94fe512c1e9a863d920a5e47cb
    73fbd0386addaf1bb70eb516429867
    481d9288e81ffeb8aeab584a92261b
    3aeed2ccd6f461b8b76f1d146d6245
    9fd2dd85d3ad7d18f039ec4af1400f
    adffdb51d7d00d06948f7b3d29db91
    f07da05b76ee2479468b1eaa1c53e9
    05818d3e4844531959534c6e105f15
    c1c8caa6c4f1857aa1bf587f40e231
    47d977123accf3da352830e0243a4d
    4f64540dbda116595b7bc7ef8aa538
    dced70091a76d45f60d65d2c841d69
    3260a7d05058845f531d769f5ff671
    1a185622162953f599a1c281a21f46
    444fa15bd0e9a349c04b013534deec
    e766b9fc8f7e4721d57e969383e17c
    23ccb8717a15cbb17cfcdff505d059
    bbb1"""

d_nd = """1c98d50d875a6f165f98570fb6a1e8
    a9f8096724f2849e827383b5c41136
    af986c26afffc97271e40c6db10489
    d278777928baf41e9284d8bce5b645
    4dcf964df23f842809a761d2e0029c
    fff9e2f94d578118c2948a31a49852
    bf9ab9e927b0bee1172fc704b8a6d6
    4042350c0b632ee4388cbd02ba83a0
    4c21c6762840e9c559d710060b67ab
    8417915252ad9919b9a161b6dfed3a
    3ecb280c032782fbf6fc0b6cabeccd
    8c128304389132b04f4beb2cd1a4cf
    b0ce4765bb719144f763536a240df3
    52bacf7dc68002e24c4acfc39975b8
    ab589fb5f50b4df4bba3666f71d58f
    41db59cc49139412d6273e71e65681
    8b535d075bfd0706dfdfa86b03a14d
    13"""

n_sd = n_nd.replace("\n", "").replace(" ", "")
d_sd = d_nd.replace("\n", "").replace(" ", "")

N = int(n_sd, 16)
D = int(d_sd, 16)

M = "Corso Cyber"
Mi = int(M.encode("utf-8").hex(), 16)

e = 3

C = pow(Mi, e, N)

d = pow(C, D, N)

Messaggio = d.to_bytes((D.bit_length() + 7) // 8, "big")
print(Messaggio.decode("utf-8"))
