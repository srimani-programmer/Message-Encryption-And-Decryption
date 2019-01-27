# Symmetric Cryptographic Decryption in Python.
# done by @Sri_Programmer
# Python v3.7.0

__author__ = 'Sri Manikanta Palakollu'

import sys
import os

captial_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'	# [A-Z]
small_letter = 'abcdefghijklmnopqrstuvwxyz'	# [a-z]
special_characters = "[@_!#$%^&*()<>?/\|} {~:+-,.';]"
key = 6

encrypted_file = input('Enter the Ciphertext file name with Extension:')	# Encrypted file as input

try:
	encrypted_file_object = open(encrypted_file,'r')
except (FileNotFoundError,IOError):
	print('File Not found')
	sys.exit(0)

decrypted_file = input('Enter the Decryption filename to store the data:') # Decrypted file as output

decrypted_file_object = open(decrypted_file,'w+')


try:
	for line in encrypted_file_object: # To read data from the file
		Decryted_value = ''
		line = line[:-2]
		for character in line:
			if character.isupper() == True:
				ele_position = captial_letter.find(character)
				ele_position = (ele_position - key)%26
				Decryted_value += captial_letter[ele_position]
			elif character.islower() == True:
				ele_position = small_letter.find(character)
				ele_position = (ele_position - key)%26
				Decryted_value += small_letter[ele_position]
			elif character.isnumeric() == True:
				new_val = (int(character) - key)%10
				Decryted_value += str(new_val)
			else:
				ele_position = special_characters.find(character)
				ele_position = (ele_position - key)%30
				Decryted_value += special_characters[ele_position]

		decrypted_file_object.writelines(Decryted_value)
		decrypted_file_object.write('\n')

except Exception:
		print('Some problem Ciphertext unable to handle.')

finally:
	encrypted_file_object.close()
	decrypted_file_object.close()

