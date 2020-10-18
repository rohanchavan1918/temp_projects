import re
import os
import sys

#check For OS
os_name = sys.platform


if os_name == 'linux':
	print(f'|===================================================|\n|       Ohhh You Are using {os_name.title()} Slaute You Man     |\n|===================================================|') 

	#Create File
	os.system('pip3 list -o > outdated.txt')

	if 'outdated.txt' in os.listdir():
		with open('outdated.txt', 'r') as file:
			for line in file.readlines()[2:]:
				extract_word = re.findall('^[a-zA-Z]+', line)
				package_name = ''.join(extract_word)
				os.system(f'pip3 install --upgrade {package_name}')
	os.system('rm outdated.txt')

elif os_name == 'win32':
	print(f'|===================================================|\n|  Ohhh You Are using Windows, Just Try Linux Once  |\n|===================================================|') 

	#Create File
	os.system('pip3 list -o > outdated.txt')
	if 'outdated.txt' in os.listdir():
		with open('outdated.txt', 'r') as file:
			for line in file.readlines()[2:]:
				extract_word = re.findall('^[a-zA-Z]+', line)
				package_name = ''.join(extract_word)
				os.system(f'pip3 install --upgrade {package_name}')
	os.system('del outdated.txt')
