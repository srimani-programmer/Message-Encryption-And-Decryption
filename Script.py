# Symmetric Cryptographic Encryption and Decryption in Python.
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

captial_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'	# [A-Z]
small_letter = 'abcdefghijklmnopqrstuvwxyz'	# [a-z]
special_characters = "[@_!#$%^&*()<>?/|\} {~:+-,.';]"
key = 6


def Encryption(filename): # Encrypts the file

	print('Enter the data into the file to Encrypt :')
	print('Press CTRL+D After giving the input to be encrypted :)')
	user_input = sys.stdin.readlines()	# CTRL + D to break the input

	encrypted_file_name = original_information_filename + "_ciphertext"

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

def Decryption(encrypted_file):	# produces the original result
		
	try:
		encrypted_file_object = open(encrypted_file,'r')
	except (FileNotFoundError,IOError):
		print('File with name {} is not found'.format(encrypted_file))
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


if __name__ == "__main__":

	while True:
		print('Enter your choice:')
		print('1. Encryption')
		print('2. Decryption')
		choice = int(input('Select your Choice:'))
		if(choice == 1):
			original_information_filename = input('Enter the filename to store Original information with .txt extension:')
			Encryption(original_information_filename)
			break
		elif(choice == 2):
			encrypted_file = input('Enter the Ciphertext file name with Extension:')	# Encrypted file as input
			Decryption(encrypted_file)
			break
		else:
			print('Please Enter a valid choice:')






