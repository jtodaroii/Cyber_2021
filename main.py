def main():
  print(encrypt_word(decrypt_word('xyz', 2), 2))


"""
letter should be a lower case letter from 'a' to 'z'
"""
def encrypt_letter(letter, key):
  plaintext_letter_number = ord(letter) - ord('a')
  cipher_letter_number = (plaintext_letter_number + key) % 26
  #print(cipher_letter_number)
  cipher_letter = chr(cipher_letter_number + ord('a'))
  return cipher_letter

def encrypt_word(word, key):
  encrypted_word = ""
  for letter in word:
    encrypted_word += encrypt_letter(letter, key)
  return encrypted_word

def decrypt_letter(letter, key):
  ciphertext_letter_number = ord(letter) - ord('a')
  plain_letter_number = (ciphertext_letter_number - key)
  if plain_letter_number < 0:
    plain_letter_number += 26
  plain_letter = chr(plain_letter_number + ord('a')) 
  return plain_letter

def decrypt_word(word, key):
  decrypted_word = ""
  for letter in word:
    decrypted_word += decrypt_letter(letter, key)
  return decrypted_word


#program starts running here
main()