__author__ = 'Exe-Fortress'
from hashlib import sha256

def hmac_sha256(key, message) -> bytes:
    try:
        if isinstance(key, bytes) and isinstance(message, bytes):
            if len(key) <= 64:
                key += b'\x00' * (64 - len(key))
            else:
                key = sha256(key).digest()
            inner_hash = sha256(bytes((x ^ 0x36) for x in key) + message).digest()
            return sha256(bytes((x ^ 0x5C) for x in key) + inner_hash).digest()
        else:
            raise TypeError
    except TypeError:
        return b''

if __name__ == '__main__':
    message = b'Hello, World'
    key = b'Secret'
    result = '4a761a9703f52506e40b44c802b76628e0e6ba6417cd56ec06363d32fbe222c5'
    assert hmac_sha256(key, message).hex() == result