#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def hell(params, pref='Hi'):
	if len(params) == 1:
		name =params[0]
	elif len(params) == 2:
		name = params[0] + ' ' + params[1]
		name = '-={0} {1}=-'.format(params[0], params[1])
		pref = 'Hello'
	else:
		name = 'Username'
	print(pref, name, sep=', ', end='!\n') #sep - razdelitel, end-okon4anie

def main():
	hell(sys.argv[1:]) #название программы, и все аргументы что ей присваиваются

if __name__ == '__main__': #ОТДЕЛЕНИЕ ОТ ИМПОРТА И ОТДЕЛЬНОГО ЗАПУСКА(?)
	main()