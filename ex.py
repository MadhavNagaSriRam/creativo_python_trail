import base64
string_input=input()
encode_data=base64.b64encode(string_input.encode('utf-8'))
print(encode_data)
decode_data=base64.b64decode(encode_data).decode('utf-8')
