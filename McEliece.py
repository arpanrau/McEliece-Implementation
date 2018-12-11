import numpy as np
import encoder
import decoder
import keygen

key_info = keygen.hamming_keygen(3)
g_prime = key_info.Gcarat
encoded = encoder.Encoder(np.array([1,0,1,0]), g_prime)
message = encoded.get_message()
encrypted = encoded.get_encrypted()
print("Message = " + str(message))
print("G^ = \n" +str(g_prime))
print("Encoded Message = " + str(encoded.c_prime))
print("Error Introduced =" + str(encoded.z))
print("Encrypted Message = " + str(encrypted))


decoded = decoder.decoder(encrypted, key_info.S, key_info.P, key_info.paritycheck, message)
print("Message = " + str(decoded.decrypted))
