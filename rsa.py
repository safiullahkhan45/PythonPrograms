def find_e(phi_n):
	factorials = []
	e = 1

	for i in range(2, phi_n):
		if phi_n%i == 0:
			factorials.append(i)

	for i in range(2, phi_n):
		if i not in factorials:
			e = i
			break

	return e


def find_d(e, phi_n):
	d = 1
	for i in range(2, phi_n):
		if e*i % phi_n == 1:
			d = i
	return d


def listtostring(l):
    string = ""
    for i in l:
        string += i

    return string


p = int(input("Enter Value of P"))
q = int(input("Enter Value of Q"))

n = p*q
phi_n = (p-1)*(q-1)
e = find_e(phi_n)
d = find_d(e, phi_n)

message = input("Insert message")

# Encryption
# 1 Break message into characters
message_characters = list(message)
message_asci = []
cipher_asci = []
cipher_list = []

# 2 Covert message characters to ascii values
for i in message_characters:
    asci = ord(i)
    message_asci.append(asci)

# 3 Apply Cipher operations on each character
for i in message_asci:
    epower = pow(i, e)
    cipher = epower % n
    cipher_asci.append(cipher)

# 4 Convert Ascii values of Cipher to characters
for i in cipher_asci:
    characters = chr(i)
    cipher_list.append(characters)

# print(cipher_list)

# 5 Convert List to String
cipher_text = listtostring(cipher_list)
print("value of n = " + str(n))
print("Value of phi_n = " + str(phi_n))
print("Value of e = " + str(e))
print("value of d = " + str(d))
print("Cipher Text: " + str(cipher_text))

# Decryption
dec_msg_asci = []
dec_characters = []

# 1. Operations on already present list
for i in cipher_asci:

    dpower = pow(i, d)
    msg_asci = dpower % n
    dec_msg_asci.append(msg_asci)

# 2. Converting Ascii values to characters.
for i in dec_msg_asci:
    dec_chars = chr(i)
    dec_characters.append(dec_chars)

# 3. List to String Conversion.
dec_message = listtostring(dec_characters)
print("Decrypted Text: " + str(dec_message))

