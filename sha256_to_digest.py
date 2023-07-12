def sha256(data=b''):
    I = [
        0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
    ]
    C = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
        0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
        0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
        0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
        0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
        0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
        0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
        0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]
    padding = b"\x80" + b"\x00" * ((55 - len(data)) & 63)
    #length_bits = (len(data) << 3).to_bytes(8, 'big')
    length_bits = b''
    data_length = len(data) << 3
    for _ in range(8):
        length_bits = bytes([data_length & 0xFF]) + length_bits
        data_length >>= 8
    buffer = data + padding + length_bits
    while len(buffer) >= 64:
        W = [int.from_bytes(buffer[i*4:(i+1)*4], 'big') for i in range(16)]
        for i in range(16, 64):
            s0 = ((W[i - 15] >> 7) | (W[i - 15] << 25)) ^ ((W[i - 15] >> 18) | (W[i - 15] << 14)) ^ (W[i - 15] >> 3)
            s1 = ((W[i - 2] >> 17) | (W[i - 2] << 15)) ^ ((W[i - 2] >> 19) | (W[i - 2] << 13)) ^ (W[i - 2] >> 10)
            W.extend([(W[i - 16] + s0 + W[i - 7] + s1) & 0xFFFFFFFF])
        a, b, c, d, e, f, g, h = I
        for i in range(64):
            T1 = h + (((e >> 6) | (e << 26)) ^ 
                    ((e >> 11) | (e << 21)) ^ 
                    ((e >> 25) | (e << 7))) + ((e & f) ^ ((~e) & g)) + C[i] + W[i]
            T2 = (((a >> 2) | (a << 30)) ^ 
                ((a >> 13) | (a << 19)) ^ 
                ((a >> 22) | (a << 10))) + ((a & b) ^ 
                                            (a & c) ^ 
                                            (b & c))
            h = g; g = f; f = e; e = (d + T1) & 0xFFFFFFFF; d = c; c = b; b = a;a = (T1 + T2) & 0xFFFFFFFF
        I[0] = (I[0] + a) & 0xFFFFFFFF
        I[1] = (I[1] + b) & 0xFFFFFFFF
        I[2] = (I[2] + c) & 0xFFFFFFFF
        I[3] = (I[3] + d) & 0xFFFFFFFF
        I[4] = (I[4] + e) & 0xFFFFFFFF
        I[5] = (I[5] + f) & 0xFFFFFFFF
        I[6] = (I[6] + g) & 0xFFFFFFFF
        I[7] = (I[7] + h) & 0xFFFFFFFF
        buffer = buffer[64:]
    #return b''.join([h.to_bytes(4, 'big') for h in I[:8]])
    return b''.join(bytes([(val >> 24) & 0xFF, (val >> 16) & 0xFF, (val >> 8) & 0xFF, val & 0xFF]) for val in I[:8])

def H256_test():
    import time, os, hashlib
    INTERNAL_HASH = []
    round = 1000
    message = os.urandom(round)
    start = time.time()
    size = 0     
    for i in range(round):
        INTERNAL_HASH.append(sha256(message[:i]))
        size += i    
    elapsed = time.time() - start
    print ('Eval:  ',(sha256(message).hex() == hashlib.sha256(message).digest().hex()))
    print (f'H256: \t{i+1} Hash \nSize: \t{size} bytes \nTime: \t{elapsed:.8f} second \t{(i+1) / elapsed:.2f} Hash/second \t{size / elapsed:.2f} Bits/second\n')

while True:
    H256_test()


