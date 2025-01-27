import base64

# Código Python criptografado em Base64 (substitua pelo seu)
encrypted_code = """
aW1wb3J0IGFyZ3BhcnNlCmltcG9ydCBvcwppbXBvcnQgc3VicHJvY2Vzcwpmcm9tIGdpdGh1YiBp
bXBvcnQgR2l0aHViCgojIERlcGVuZMOqbmNpYXMgZGUgaW5zdGFsYcOnw6NvCnRyeToKICAgIGZy
b20gZ2l0aHViIGltcG9ydCBHaXRodWIKZXhjZXB0IEltcG9ydEVycm9yOgogICAgc3VicHJvY2Vz
cy5jaGVja19jYWxsKFsicGlwIiwgImluc3RhbGwiLCAiUHlHaXRodWIiXSkKICAgIGZyb20gZ2l0
aHViIGltcG9ydCBHaXRodWIKCiMgRGVmaW5pw6fDtWVzCkdJVEhVQl9UT0tFTiA9ICJnaHBfNGtY
aFYzUlh6NDA4U2h2bDRtbWxjR1JiVnMzMFQ3MGpScDUyIgpSRVBPX05BTUUgPSAiZHowOXBsL2R6
MDlwbCIKCiMgRXh0ZW5zw7VlcyBwZXJtaXRpZGFzCkFMTE9XRURfRVhURU5TSU9OUyA9IHsnLmFw
aycsICcuemlwJywgJy5qYXInfQoKZGVmIGFsbG93ZWRfZmlsZShmaWxlbmFtZSk6CiAgICAiIiJD
aGVjayBpZiB0aGUgZmlsZSBoYXMgYW4gYWxsb3dlZCBleHRlbnNpb24uIiIiCiAgICByZXR1cm4g
YW55KGZpbGVuYW1lLmVuZHN3aXRoKGV4dCkgZm9yIGV4dCBpbiBBTExPV0VEX0VYVEVOU0lPTlMp
CgpkZWYgdXBsb2FkX2ZpbGUocmVwbywgZmlsZV9wYXRoLCB0YXJnZXRfcGF0aCk6CiAgICAiIiJV
cGxvYWQgYSBzaW5nbGUgZmlsZSB0byB0aGUgcmVwb3NpdG9yeS4iIiIKICAgIHdpdGggb3Blbihm
aWxlX3BhdGgsICJyYiIpIGFzIGZpbGU6CiAgICAgICAgY29udGVudCA9IGZpbGUucmVhZCgpCiAg
ICB0cnk6CiAgICAgICAgcmVwby5jcmVhdGVfZmlsZShwYXRoPXRhcmdldF9wYXRoLCBtZXNzYWdl
PWYiVXBsb2FkIG9mIHt0YXJnZXRfcGF0aH0iLCBjb250ZW50PWNvbnRlbnQpCiAgICAgICAgcHJp
bnQoZiJcbkZpbGUgJ3tmaWxlX3BhdGh9JyBzdWNjZXNzZnVsbHkgdXBsb2FkZWQhIikKICAgIGV4
Y2VwdCBFeGNlcHRpb24gYXMgZToKICAgICAgICBwcmludChmIkVycm9yIHVwbG9hZGluZyB0aGUg
ZmlsZToge2V9IikKCmRlZiB1cGxvYWRfZm9sZGVyKHJlcG8sIGZvbGRlcl9wYXRoLCB0YXJnZXRf
cGF0aD0iIik6CiAgICAiIiJSZWN1cnNpdmVseSB1cGxvYWQgZmlsZXMgZnJvbSBhIGZvbGRlciB0
byB0aGUgcmVwb3NpdG9yeS4iIiIKICAgIGZvciByb290LCBkaXJzLCBmaWxlcyBpbiBvcy53YWxr
KGZvbGRlcl9wYXRoKToKICAgICAgICBmb3IgZmlsZSBpbiBmaWxlczoKICAgICAgICAgICAgZmls
ZV9wYXRoID0gb3MucGF0aC5qb2luKHJvb3QsIGZpbGUpCiAgICAgICAgICAgIHRhcmdldF9maWxl
X3BhdGggPSBvcy5wYXRoLmpvaW4odGFyZ2V0X3BhdGgsIG9zLnBhdGgucmVscGF0aChmaWxlX3Bh
dGgsIGZvbGRlcl9wYXRoKSkKICAgICAgICAgICAgdXBsb2FkX2ZpbGUocmVwbywgZmlsZV9wYXRo
LCB0YXJnZXRfZmlsZV9wYXRoKQoKZGVmIGRlbGV0ZV9maWxlKHJlcG8sIGZpbGVfcGF0aCk6CiAg
ICAiIiJEZWxldGUgYSBmaWxlIGZyb20gdGhlIHJlcG9zaXRvcnkuIiIiCiAgICB0cnk6CiAgICAg
ICAgZmlsZSA9IHJlcG8uZ2V0X2NvbnRlbnRzKGZpbGVfcGF0aCkKICAgICAgICByZXBvLmRlbGV0
ZV9maWxlKGZpbGVfcGF0aCwgZiJEZWxldGVkIHtmaWxlX3BhdGh9IiwgZmlsZS5zaGEpCiAgICAg
ICAgcHJpbnQoZiJcbkZpbGUgJ3tmaWxlX3BhdGh9JyBzdWNjZXNzZnVsbHkgZGVsZXRlZCEiKQog
ICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAgICAgIHByaW50KGYiRXJyb3IgZGVsZXRpbmcg
dGhlIGZpbGU6IHtlfSIpCgpkZWYgZGVsZXRlX2ZvbGRlcihyZXBvLCBmb2xkZXJfcGF0aCk6CiAg
ICAiIiJEZWxldGUgYWxsIGZpbGVzIGluIGEgZm9sZGVyIGZyb20gdGhlIHJlcG9zaXRvcnkuIiIi
CiAgICB0cnk6CiAgICAgICAgY29udGVudHMgPSByZXBvLmdldF9jb250ZW50cyhmb2xkZXJfcGF0
aCkKICAgICAgICBmb3IgY29udGVudCBpbiBjb250ZW50czoKICAgICAgICAgICAgaWYgY29udGVu
dC50eXBlID09ICdmaWxlJzoKICAgICAgICAgICAgICAgIHJlcG8uZGVsZXRlX2ZpbGUoY29udGVu
dC5wYXRoLCBmIkRlbGV0ZWQge2NvbnRlbnQucGF0aH0iLCBjb250ZW50LnNoYSkKICAgICAgICAg
ICAgICAgIHByaW50KGYiRmlsZSAne2NvbnRlbnQucGF0aH0nIGRlbGV0ZWQuIikKICAgICAgICAg
ICAgZWxpZiBjb250ZW50LnR5cGUgPT0gJ2Rpcic6CiAgICAgICAgICAgICAgICBkZWxldGVfZm9s
ZGVyKHJlcG8sIGNvbnRlbnQucGF0aCkKICAgICAgICBwcmludChmIkFsbCBmaWxlcyBpbiBmb2xk
ZXIgJ3tmb2xkZXJfcGF0aH0nIGhhdmUgYmVlbiBkZWxldGVkLiIpCiAgICBleGNlcHQgRXhjZXB0
aW9uIGFzIGU6CiAgICAgICAgcHJpbnQoZiJFcnJvciBkZWxldGluZyBmb2xkZXIgJ3tmb2xkZXJf
cGF0aH0nOiB7ZX0iKQoKZGVmIGxpc3RfcmVwb19jb250ZW50cyhyZXBvKToKICAgICIiIkxpc3Qg
dGhlIGNvbnRlbnRzIG9mIHRoZSByZXBvc2l0b3J5LiIiIgogICAgdHJ5OgogICAgICAgIGNvbnRl
bnRzID0gcmVwby5nZXRfY29udGVudHMoIiIpCiAgICAgICAgaWYgbm90IGNvbnRlbnRzOgogICAg
ICAgICAgICBwcmludCgiICAgIFRoZSByZXBvc2l0b3J5IGlzIGVtcHR5LiIpCiAgICAgICAgZWxz
ZToKICAgICAgICAgICAgcHJpbnQoIlxuICAgIENvbnRlbnRzIG9mIHRoZSByZXBvc2l0b3J5OiIp
CiAgICAgICAgICAgIGZvciBjb250ZW50IGluIGNvbnRlbnRzOgogICAgICAgICAgICAgICAgcHJp
bnQoZiIgICAge2NvbnRlbnQucGF0aH0iKQogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOgogICAg
ICAgIHByaW50KGYiRXJyb3IgbGlzdGluZyBjb250ZW50czoge2V9IikKCmRlZiBkaXNwbGF5X2Jh
bm5lcigpOgogICAgIiIiRGlzcGxheSBhIHNpbXBsZSBiYW5uZXIgZm9yIHRoZSBDTEkgdG9vbC4i
IiIKICAgIGJhbm5lciA9ICIiIgogICAgIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMj
IyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwogICAgIyAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIwogICAgIyAgICBHaXRIdWIgRmls
ZSBVcGxvYWRlciBhbmQgTWFuYWdlciBUb29sICAgICAgICAgICAgICAgICAgIwogICAgIyAgICBV
cGxvYWQsIGRlbGV0ZSwgYW5kIGxpc3QgZmlsZXMgYW5kIGZvbGRlcnMgZnJvbSBHaXRIdWIgIwog
ICAgIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgIwogICAgIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMj
IyMjIyMjIyMjIyMjIyMjIwogICAgIiIiCiAgICBwcmludChiYW5uZXIpCgpkZWYgdXBsb2FkX3Rv
X2dpdGh1YihmaWxlX3BhdGgpOgogICAgIiIiTWFpbiBmdW5jdGlvbiB0byB1cGxvYWQgZmlsZXMg
b3IgZm9sZGVycyB0byBHaXRIdWIuIiIiCiAgICBpZiBub3Qgb3MucGF0aC5leGlzdHMoZmlsZV9w
YXRoKToKICAgICAgICBwcmludChmIkVycm9yOiBUaGUgcGF0aCAne2ZpbGVfcGF0aH0nIHdhcyBu
b3QgZm91bmQuIikKICAgICAgICByZXR1cm4KCiAgICB0YXJnZXRfcGF0aCA9IG9zLnBhdGguYmFz
ZW5hbWUoZmlsZV9wYXRoKQogICAgZyA9IEdpdGh1YihHSVRIVUJfVE9LRU4pCiAgICByZXBvID0g
Zy5nZXRfcmVwbyhSRVBPX05BTUUpCgogICAgaWYgb3MucGF0aC5pc2RpcihmaWxlX3BhdGgpOgog
ICAgICAgICMgSWYgaXQncyBhIGZvbGRlciwgdXBsb2FkIGZpbGVzIHJlY3Vyc2l2ZWx5CiAgICAg
ICAgdXBsb2FkX2ZvbGRlcihyZXBvLCBmaWxlX3BhdGgpCiAgICBlbGlmIG9zLnBhdGguaXNmaWxl
KGZpbGVfcGF0aCkgYW5kIGFsbG93ZWRfZmlsZShmaWxlX3BhdGgpOgogICAgICAgICMgSWYgaXQn
cyBhIHZhbGlkIGZpbGUsIHVwbG9hZCBpdAogICAgICAgIHVwbG9hZF9maWxlKHJlcG8sIGZpbGVf
cGF0aCwgdGFyZ2V0X3BhdGgpCiAgICBlbHNlOgogICAgICAgIHByaW50KCJFcnJvcjogVGhlIGZp
bGUgZG9lcyBub3QgaGF2ZSBhbiBhbGxvd2VkIGV4dGVuc2lvbiBvciBpcyBub3QgYSB2YWxpZCBm
aWxlLiIpCgpkZWYgZGVsZXRlX2Zyb21fZ2l0aHViKHBhdGgpOgogICAgIiIiRGVsZXRlIGEgZmls
ZSBvciBmb2xkZXIgZnJvbSB0aGUgR2l0SHViIHJlcG9zaXRvcnkuIiIiCiAgICBnID0gR2l0aHVi
KEdJVEhVQl9UT0tFTikKICAgIHJlcG8gPSBnLmdldF9yZXBvKFJFUE9fTkFNRSkKCiAgICBpZiBv
cy5wYXRoLmlzZGlyKHBhdGgpOgogICAgICAgIGRlbGV0ZV9mb2xkZXIocmVwbywgcGF0aCkKICAg
IGVsaWYgb3MucGF0aC5pc2ZpbGUocGF0aCk6CiAgICAgICAgZGVsZXRlX2ZpbGUocmVwbywgcGF0
aCkKICAgIGVsc2U6CiAgICAgICAgcHJpbnQoZiJFcnJvcjogVGhlIHBhdGggJ3twYXRofScgZG9l
cyBub3QgZXhpc3QgaW4gdGhlIHJlcG9zaXRvcnkuIikKCmlmIF9fbmFtZV9fID09ICJfX21haW5f
XyI6CiAgICBkaXNwbGF5X2Jhbm5lcigpICAjIERpc3BsYXkgdGhlIGJhbm5lciB3aGVuIHRoZSBz
Y3JpcHQgc3RhcnRzCgogICAgcGFyc2VyID0gYXJncGFyc2UuQXJndW1lbnRQYXJzZXIoZGVzY3Jp
cHRpb249IlVwbG9hZCwgZGVsZXRlLCBhbmQgbGlzdCBmaWxlcyBhbmQgZm9sZGVycyBmcm9tIGEg
R2l0SHViIHJlcG9zaXRvcnkuIikKICAgIHBhcnNlci5hZGRfYXJndW1lbnQoIi0tYXJxIiwgaGVs
cD0iRnVsbCBwYXRoIG9mIHRoZSBmaWxlIG9yIGZvbGRlciB0byB1cGxvYWQgb3IgZGVsZXRlLiIp
CiAgICBwYXJzZXIuYWRkX2FyZ3VtZW50KCItLWRlbGV0ZSIsIGFjdGlvbj0ic3RvcmVfdHJ1ZSIs
IGhlbHA9IlNldCB0aGlzIGZsYWcgdG8gZGVsZXRlIHRoZSBmaWxlIG9yIGZvbGRlci4iKQogICAg
cGFyc2VyLmFkZF9hcmd1bWVudCgiLS1saXN0IiwgYWN0aW9uPSJzdG9yZV90cnVlIiwgaGVscD0i
U2V0IHRoaXMgZmxhZyB0byBsaXN0IHRoZSBjb250ZW50cyBvZiB0aGUgcmVwb3NpdG9yeS4iKQog
ICAgYXJncyA9IHBhcnNlci5wYXJzZV9hcmdzKCkKCiAgICBnID0gR2l0aHViKEdJVEhVQl9UT0tF
TikKICAgIHJlcG8gPSBnLmdldF9yZXBvKFJFUE9fTkFNRSkKCiAgICBpZiBhcmdzLmxpc3Q6CiAg
ICAgICAgbGlzdF9yZXBvX2NvbnRlbnRzKHJlcG8pCiAgICBlbGlmIGFyZ3MuZGVsZXRlOgogICAg
ICAgIGlmIG5vdCBhcmdzLmFycToKICAgICAgICAgICAgcHJpbnQoIkVycm9yOiAtLWFycSBpcyBy
ZXF1aXJlZCB3aGVuIHVzaW5nIC0tZGVsZXRlLiIpCiAgICAgICAgZWxzZToKICAgICAgICAgICAg
ZGVsZXRlX2Zyb21fZ2l0aHViKGFyZ3MuYXJxKQogICAgZWxpZiBhcmdzLmFycToKICAgICAgICB1
cGxvYWRfdG9fZ2l0aHViKGFyZ3MuYXJxKQogICAgZWxzZToKICAgICAgICBwcmludCgiRXJyb3I6
IFlvdSBtdXN0IHNwZWNpZnkgLS1hcnEgZm9yIHVwbG9hZGluZyBmaWxlcy4iKQoK
"""

# Decodificar o código
decoded_code = base64.b64decode(encrypted_code).decode("utf-8")

# Executar o código decodificado
exec(decoded_code)
