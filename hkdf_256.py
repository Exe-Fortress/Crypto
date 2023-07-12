__author__ = 'Exe-Fortress'
from hmac_256 import hmac_sha256

def hkdf_sha256(salt, message, info, length:int) -> bytes:
    try:
        if isinstance(salt, bytes) and isinstance(message, bytes) and isinstance(info, bytes):
            if len(salt) == 0:
                salt = b'\x00' * 32
            prk = hmac_sha256(salt, message)
            t = b''
            output_key_material = b''
            for i in range((length + 31) // 32):
                t = hmac_sha256(prk, t + info + bytes([i + 1]))
                output_key_material += t
            return output_key_material[:length]
        else:
            raise TypeError
    except TypeError:
        return b''

if __name__ == '__main__':
    salt = b'salt'
    info = b'info'
    message = b'Hello, World'
    length = 32
    result = '42beb4b7745127259ecf4545a2b9af0d279d5051b06e9fb10bb169213130ee67'
    assert hkdf_sha256(salt, message, info, length).hex() == result
