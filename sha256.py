"""
    author  : Exe_Fortress
    version : 0.1.0
    ref     : NIST.FIPS.180-4, other scripts for references

    #  !!!You can sample this script and improve it!!!

"""
class H256():    
      
    def __init__(self, message=b''):
        self.Buffer = b''
        self.Length = 0     
        self.I = (
                    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
                    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
                 )
        self.update(message)
    
    def update(self, message=b''):
        if not isinstance (message, (bytes)): raise TypeError ('Strings must be encoded before hashing')
        self.Buffer += message
        self.Length += len(message)
        while len(self.Buffer) >= 64:
            K = (
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
                         )   
            a, b, c, d, e, f, g, h =  self.I 
            W = [
                    int.from_bytes(self.Buffer[0:4]),int.from_bytes(self.Buffer[4:8]),int.from_bytes(self.Buffer[8:12]),int.from_bytes(self.Buffer[12:16]), 
                    int.from_bytes(self.Buffer[16:20]),int.from_bytes(self.Buffer[20:24]),int.from_bytes(self.Buffer[24:28]),int.from_bytes(self.Buffer[28:32]), 
                    int.from_bytes(self.Buffer[32:36]),int.from_bytes(self.Buffer[36:40]),int.from_bytes(self.Buffer[40:44]),int.from_bytes(self.Buffer[44:48]),
                    int.from_bytes(self.Buffer[48:52]),int.from_bytes(self.Buffer[52:56]),int.from_bytes(self.Buffer[56:60]),int.from_bytes(self.Buffer[60:64]),
                ] + [0] * 48        
            
            sigma0 = lambda i: (((i>>7) | (i<<25)) ^ ((i>>18) | (i<<14)) ^ (i>>3))
            sigma1 = lambda i: (((i>>17) | (i<<15)) ^ ((i>>19) | (i<<13)) ^ (i>>10))
            W[16] = W[0] + sigma0(W[1]) + W[9] + sigma1(W[14]) & 0xFFFFFFFF
            W[17] = W[1] + sigma0(W[2]) + W[10] + sigma1(W[15]) & 0xFFFFFFFF
            W[18] = W[2] + sigma0(W[3]) + W[11] + sigma1(W[16]) & 0xFFFFFFFF
            W[19] = W[3] + sigma0(W[4]) + W[12] + sigma1(W[17]) & 0xFFFFFFFF
            W[20] = W[4] + sigma0(W[5]) + W[13] + sigma1(W[18]) & 0xFFFFFFFF
            W[21] = W[5] + sigma0(W[6]) + W[14] + sigma1(W[19]) & 0xFFFFFFFF
            W[22] = W[6] + sigma0(W[7]) + W[15] + sigma1(W[20]) & 0xFFFFFFFF
            W[23] = W[7] + sigma0(W[8]) + W[16] + sigma1(W[21]) & 0xFFFFFFFF
            W[24] = W[8] + sigma0(W[9]) + W[17] + sigma1(W[22]) & 0xFFFFFFFF
            W[25] = W[9] + sigma0(W[10]) + W[18] + sigma1(W[23]) & 0xFFFFFFFF
            W[26] = W[10] + sigma0(W[11]) + W[19] + sigma1(W[24]) & 0xFFFFFFFF
            W[27] = W[11] + sigma0(W[12]) + W[20] + sigma1(W[25]) & 0xFFFFFFFF
            W[28] = W[12] + sigma0(W[13]) + W[21] + sigma1(W[26]) & 0xFFFFFFFF
            W[29] = W[13] + sigma0(W[14]) + W[22] + sigma1(W[27]) & 0xFFFFFFFF
            W[30] = W[14] + sigma0(W[15]) + W[23] + sigma1(W[28]) & 0xFFFFFFFF
            W[31] = W[15] + sigma0(W[16]) + W[24] + sigma1(W[29]) & 0xFFFFFFFF
            W[32] = W[16] + sigma0(W[17]) + W[25] + sigma1(W[30]) & 0xFFFFFFFF
            W[33] = W[17] + sigma0(W[18]) + W[26] + sigma1(W[31]) & 0xFFFFFFFF
            W[34] = W[18] + sigma0(W[19]) + W[27] + sigma1(W[32]) & 0xFFFFFFFF
            W[35] = W[19] + sigma0(W[20]) + W[28] + sigma1(W[33]) & 0xFFFFFFFF
            W[36] = W[20] + sigma0(W[21]) + W[29] + sigma1(W[34]) & 0xFFFFFFFF
            W[37] = W[21] + sigma0(W[22]) + W[30] + sigma1(W[35]) & 0xFFFFFFFF
            W[38] = W[22] + sigma0(W[23]) + W[31] + sigma1(W[36]) & 0xFFFFFFFF
            W[39] = W[23] + sigma0(W[24]) + W[32] + sigma1(W[37]) & 0xFFFFFFFF
            W[40] = W[24] + sigma0(W[25]) + W[33] + sigma1(W[38]) & 0xFFFFFFFF
            W[41] = W[25] + sigma0(W[26]) + W[34] + sigma1(W[39]) & 0xFFFFFFFF
            W[42] = W[26] + sigma0(W[27]) + W[35] + sigma1(W[40]) & 0xFFFFFFFF
            W[43] = W[27] + sigma0(W[28]) + W[36] + sigma1(W[41]) & 0xFFFFFFFF
            W[44] = W[28] + sigma0(W[29]) + W[37] + sigma1(W[42]) & 0xFFFFFFFF
            W[45] = W[29] + sigma0(W[30]) + W[38] + sigma1(W[43]) & 0xFFFFFFFF
            W[46] = W[30] + sigma0(W[31]) + W[39] + sigma1(W[44]) & 0xFFFFFFFF
            W[47] = W[31] + sigma0(W[32]) + W[40] + sigma1(W[45]) & 0xFFFFFFFF
            W[48] = W[32] + sigma0(W[33]) + W[41] + sigma1(W[46]) & 0xFFFFFFFF
            W[49] = W[33] + sigma0(W[34]) + W[42] + sigma1(W[47]) & 0xFFFFFFFF
            W[50] = W[34] + sigma0(W[35]) + W[43] + sigma1(W[48]) & 0xFFFFFFFF
            W[51] = W[35] + sigma0(W[36]) + W[44] + sigma1(W[49]) & 0xFFFFFFFF
            W[52] = W[36] + sigma0(W[37]) + W[45] + sigma1(W[50]) & 0xFFFFFFFF
            W[53] = W[37] + sigma0(W[38]) + W[46] + sigma1(W[51]) & 0xFFFFFFFF
            W[54] = W[38] + sigma0(W[39]) + W[47] + sigma1(W[52]) & 0xFFFFFFFF
            W[55] = W[39] + sigma0(W[40]) + W[48] + sigma1(W[53]) & 0xFFFFFFFF
            W[56] = W[40] + sigma0(W[41]) + W[49] + sigma1(W[54]) & 0xFFFFFFFF
            W[57] = W[41] + sigma0(W[42]) + W[50] + sigma1(W[55]) & 0xFFFFFFFF
            W[58] = W[42] + sigma0(W[43]) + W[51] + sigma1(W[56]) & 0xFFFFFFFF
            W[59] = W[43] + sigma0(W[44]) + W[52] + sigma1(W[57]) & 0xFFFFFFFF
            W[60] = W[44] + sigma0(W[45]) + W[53] + sigma1(W[58]) & 0xFFFFFFFF
            W[61] = W[45] + sigma0(W[46]) + W[54] + sigma1(W[59]) & 0xFFFFFFFF
            W[62] = W[46] + sigma0(W[47]) + W[55] + sigma1(W[60]) & 0xFFFFFFFF
            W[63] = W[47] + sigma0(W[48]) + W[56] + sigma1(W[61]) & 0xFFFFFFFF
            for i in range(64):
                T2 = (((a >> 2) | (a << 30)) ^ ((a >> 13) | (a << 19)) ^ ((a >> 22) | (a << 10))) + ((a & b) ^ (a & c) ^ (b & c))
                T1 = h + (((e >> 6) | (e << 26)) ^ ((e >> 11) | (e << 21)) ^ ((e >> 25) | (e << 7))) + ((e & f) ^ ((~e) & g)) + K[i] + W[i] 
                h = g
                g = f
                f = e
                e = (d + T1) & 0xFFFFFFFF
                d = c
                c = b
                b = a
                a = (T1 + T2) & 0xFFFFFFFF

            self.I = [
                        (self.I[0] + a) % (1<<32),
                        (self.I[1] + b) % (1<<32),
                        (self.I[2] + c) % (1<<32),
                        (self.I[3] + d) % (1<<32),
                        (self.I[4] + e) % (1<<32),
                        (self.I[5] + f) % (1<<32),
                        (self.I[6] + g) % (1<<32),
                        (self.I[7] + h) % (1<<32)
                     ]
            self.Buffer = self.Buffer[64:]

    def digest(self):
        Length = self.Length % 64
        endless = (self.Length << 3).to_bytes(8, 'big')
        padding = 55 - Length if Length < 56 else 119 - Length 
        REMAKE = self.copy()
        REMAKE.update(b'\x80' + (b'\x00' * padding) + endless)
        PRE_SHA256 = b''.join(i.to_bytes(4, 'big') for i in REMAKE.I[:8])
        if (len(PRE_SHA256) == 32): return PRE_SHA256
        raise OverflowError ("length over 32")
   
    def hexdigest(self):
        if (len(self.digest().hex()) == 64): return self.digest().hex()
        raise OverflowError ("length over 64")
     
    def copy(self):
        REMAKE_SHA256 = type(self)()
        REMAKE_SHA256.__dict__.update(self.__dict__)
        return REMAKE_SHA256  

def H256_test():
    import time, os, hashlib, sha256_1
    INTERNAL_HASH = []
    round = 1000
    message = os.urandom(round)
    start = time.time()
    size = 0     
    for i in range(round):
        INTERNAL_HASH.append(H256(message[:i]).hexdigest())
        size += i    
    elapsed = time.time() - start
    print ('Eval:  ',H256(message).hexdigest() == hashlib.sha256(message).hexdigest())
    print (f'H256: \t{i+1} Hash \nSize: \t{size} bytes \nTime: \t{elapsed:.8f} second \t{(i+1) / elapsed:.2f} Hash/second \t{size / elapsed:.2f} Bits/second\n')
    
while True:
    H256_test()