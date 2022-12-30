from base64 import urlsafe_b64decode
from jose import jws
import json

def base64UrlDecode(base64Url):
    padding = b'=' * (4 - (len(base64Url) % 4))

    return urlsafe_b64decode(base64Url + padding)

def verifyJwt(token, secret):
    token_components = []
    token_components = token.split('.')
    encoded_header = token_components[0]
    encoded_payload = token_components[1]
    encoded_signature = token_components[2]

    
    # Converting Base64URL encoded string to bytes:
    header_bytes = encoded_header.encode('ascii')
    payload_bytes = encoded_payload.encode('ascii')

    # Decoding the Base64URL in 'bytes' data type to plain text in 'bytes' data type:
    header = base64UrlDecode(header_bytes)
    payload = base64UrlDecode(payload_bytes)

    # Converting 'byte' data type to string
    header_text = header.decode('ascii')
    payload_text = payload.decode('ascii')

    # Converting the strings obtained above to dictionary format:
    header_dict = json.loads(header_text)
    payload_dict = json.loads(payload_text)

    # print()
    # print(header_dict)
    # print()
    # print(payload_dict)
    # print()

    secret_encoded = jws.sign(payload_dict, secret, algorithm=header_dict['alg'])
    # print(secret_encoded)
    # print()
    if secret_encoded==token:
        return payload_dict
    else:
        raise Exception('Invalid Secret')


# print(verifyJwt('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmY3MtYXNzaWdubWVudC0xIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE2NzI1MTE0MDAsInJvbGUiOiJ1c2VyIiwiZW1haWwiOiJhcnVuQGlpaXRkLmFjLmluIiwiaGludCI6Imxvd2VyY2FzZS1hbHBoYW51bWVyaWMtbGVuZ3RoLTUifQ.LCIyPHqWAVNLT8BMXw8_69TPkvabp57ZELxpzom8FiI', 'p1gzy'))
# print(verifyJwt('eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.5Pmd-MV2zXayY1vhmDKHNe-MAYNkp-RglT9IdtbT4TaIP2NmvZH67GrSKfJZNyL5aI0gmKJufN7m0HLuijsUuA', 'abcde'))
