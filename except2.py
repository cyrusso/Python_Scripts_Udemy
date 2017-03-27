#!/usr/bin/python3
try:
	num = int(input('Enter a number: '))
	print(num)
	aFile = open('modul.py')
	print(aFile.readline())
except ValueError:
	print('Not a number, please re-enter: ')
	num = int(input('Enter a number: '))
except IOError:
	print('Cannot open file')
print('finished')
