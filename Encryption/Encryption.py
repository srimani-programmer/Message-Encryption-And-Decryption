# Symmetric Cryptographic Encryption in Python.
# done by @Sri_Programmer
# Python v3.7.0
print('''
_________ __________ _____.___.__________ ________________________________ 
\_   ___ \\______   \\__  |   |\______   \\__    ___/\_   _____/\______   \
/    \  \/ |       _/ /   |   | |     ___/  |    |    |    __)_  |       _/
\     \____|    |   \ \____   | |    |      |    |    |        \ |    |   \
 \______  /|____|_  / / ______| |____|      |____|   /_______  / |____|_  /
        \/        \/  \/                                     \/         \/ 

        ''')

__author__ = 'Sri Manikanta Palakollu'

import sys
import os

original_information_filename = input('Enter the filename for Originalwith .txt extension:')
encrypted_file_name = input('Enter the Ciphertext filename with .txt extension:')

print('Enter the data into the file to Encrypt :')
print('Press CTRL+D After giving the input to be encrypted :)')
user_input = sys.stdin.readlines()	# CTRL + D to break the input

captial_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'	# [A-Z]
small_letter = 'abcdefghijklmnopqrstuvwxyz'	# [a-z]
special_characters = "[@_!#$%^&*()<>?/|\} {~:+-,.';]"
key = 6

# Creating a new file object to store the data into the file
try:
	encrypt_file = open(original_information_filename,'w+')

	for data in user_input:	# writing the data into the file
		encrypt_file.write(data)
	
	encrypt_file = open(original_information_filename,'r')
	cipher_text = open(encrypted_file_name,'w+')

	for line in encrypt_file:
		Encrypted_value = ''
		for character in line:
			if character.isupper() == True:
				ele_position = captial_letter.find(character)
				ele_position = (ele_position + key)%26
				Encrypted_value += captial_letter[ele_position]
			elif character.islower() == True:
				ele_position = small_letter.find(character)
				ele_position = (ele_position + key)%26
				Encrypted_value += small_letter[ele_position]
			elif character.isnumeric() == True:
				new_val = (int(character) + key)%10
				Encrypted_value += str(new_val)
			else:
				ele_position = special_characters.find(character)
				ele_position = (ele_position + key)%30
				Encrypted_value += special_characters[ele_position]
				
		cipher_text.write(Encrypted_value)
		cipher_text.write('\n')
		
except (FileNotFoundError, IOError):
	print('Required files not found.')
	sys.exit(0)

finally:
	encrypt_file.close()
	cipher_text.close()

print('Do you want to keep the original data file [y/n]')

while True:
	result = input()
	if (result == 'y' or result == 'Y'):
		sys.exit(0)
	elif (result == 'n' or result == 'N'):
		os.remove(original_information_filename)
		break
	else:
		print('Enter a valid choice:')

