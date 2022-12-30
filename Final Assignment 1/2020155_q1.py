#FCS Assignment 1, question 1
#Name: Vishesh Rangwani
#Roll number: 2020155

from Crypto.Cipher import Salsa20
import gmpy2
import os

def alice_generates_symmetric_key():
    ''' 
    A function that returns a 16 byte string to be used as the key for Salsa20.
    This key should be used to encrypt Bob and Alice's communications.
    But before that, it needs to be sent to Bob.

    Input: NA
    Return: the symmetric key (byte string)
    '''
    key = os.urandom(16)
    return key

def bob_generates_asymmetric_keys(p ,q):
    '''
    A function that takes in prime numbers p and q and generates 
    the public and private keys for Bob as per RSA. Note that you are 
    not allowed to use loops to find e or d.

    Input: p, q (upto 1023 digits long)
    Return: Bob's public key and private key ((e,n), (d,n)) as a tuple
    '''
    n = gmpy2.mpz(p)*gmpy2.mpz(q)
    z = (gmpy2.mpz(p)-1)*(gmpy2.mpz(q)-1)

    e = gmpy2.mpz(z)-1
    d = gmpy2.mpz(e)        # Even (gmpy2.mpz(e)+2)*gmpy2.mpz(e) would work as a private key or even 2*e

    return ((e, n), (d, n))

def alice_sends_symmetric_key(k, e, n):
    '''
    A function that Alice uses to encrypt the symmetric key
    using Bob's public key. The ciphertext is sent to Bob.

    Input: the symmetric key k, Bob's public key e, n.
    Return: encrypted ciphertext
    '''

    # enc_list = []
    # for x in k:
    #     enc_list.append(gmpy2.powmod(x, e, n))

    enc_key_string = ''
    for x in k:
        y = gmpy2.powmod(x, e, n)
        enc_key_string += gmpy2.digits(y)
        enc_key_string += ','
    
    
    return enc_key_string[:-1];
    # return enc_list;

def bob_decrypts_symmetric_key(c, d, n):
    '''
    A function that Bob uses to decrypt the ciphertext c using his private key.
    The decrypted message would give him the symmetric key.

    Input: the ciphertext c, Bob's private key d, n.
    Return: the symmetric key (byte string)
    '''
    enc_key_list = c.split(',')
    dec_key_list = []

    for x in enc_key_list:
        y = gmpy2.powmod(gmpy2.mpz(x), d, n)
        dec_key_list.append(y)
    
    dec_key = bytes(dec_key_list)
    return dec_key

def bob_sends_message(m, k):
    '''
    A function that takes a message m, shared key k and uses Salsa20 to encrypt m.

    Input: the message m (a byte string), the shared key k (byte string)
    Return: encrypted ciphertext
    '''
    m = m.encode('utf-8')
    cipher_key = Salsa20.new(key=k)
    encrypted_m = cipher_key.nonce + cipher_key.encrypt(m)
    return encrypted_m

def alice_decrypts_message(c_, k):
    '''
    A function that takes an encrypted message c_, shared key k and uses Salsa20 to decrypt c_.

    Input: the ciphertext c_, the shared key k (byte string)
    Return: plaintext message
    '''
    dec_m_nonce = c_[:8]
    ciphertext = c_[8:]
    cipher = Salsa20.new(key=k, nonce=dec_m_nonce)
    dec_m = cipher.decrypt(ciphertext)

    return dec_m.decode()

if __name__=="__main__":
    # p, q and the message m will be taken as inputs from the user.

    # p = '182302015849'
    # q = '156702016043'

    p = input("Enter the value for 'p' = ")
    q = input("Enter the value for 'q' = ")
    m = input('Enter the message: ')

'''
    print()
    k = alice_generates_symmetric_key()
    print("k = ", k)
    k_list = []
    for x in k:
        k_list.append(x)
    print(k_list)
    print()

    (public_key, private_key) = bob_generates_asymmetric_keys(p, q)
    print("Public Key: ", public_key)
    print("Private Key: ", private_key)
    print()
    (e, n) = public_key
    (d, n) = private_key

    encrypted_symmetric_key = alice_sends_symmetric_key(k, e, n)
    print("Encrypted Symmetric Key = ", encrypted_symmetric_key)
    print()

    decrypted_symmetric_key = bob_decrypts_symmetric_key(encrypted_symmetric_key, d, n)
    print("Decrypted Symmetric Key = ", decrypted_symmetric_key)
    print()

    print()


    encrypted_msg = bob_sends_message(m, decrypted_symmetric_key)
    print("Encrypted Message: ", encrypted_msg)
    print()

    decrypted_message = alice_decrypts_message(encrypted_msg, decrypted_symmetric_key)
    print("Decrypted Message: ", decrypted_message)
    print()
'''

