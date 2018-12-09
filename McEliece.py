import numpy as np
import encoder
import decoder
import keygen

key_info = keygen.hamming_keygen(3)
#g_prime = key_info.Gcarat
g = key_info.G
h = key_info.paritycheck
#encoded = encoder.Encoder(np.array([1,0,1,0]), g_prime)
encoded = encoder.Encoder(np.array([1,0,1,0]), g)
message = encoded.get_message()
encrypted = encoded.get_encrypted()
print("message = " + str(message))
print("encrypted = " + str(encrypted))
decoded = decoder.decoder(encrypted, key_info.S, key_info.P, key_info.paritycheck, message)
print(decoded.decrypted)
