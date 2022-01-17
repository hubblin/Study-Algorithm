#https://www.acmicpc.net/problem/10930

import hashlib
input_hub = input()
encode_data = input_hub.encode()
result = hashlib.sha256(encode_data).hexdigest()

print(result)