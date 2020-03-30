#! /usr/bin/python3
# coding: utf-8

import os

def launch_analysis(data_file):
	directory = os.path.dirname(os.path.dirname(__file__))
	path_to_file = os.path.join(directory,'data',data_file)
	try :
		with open(path_to_file, 'r') as file :
			preview = file.readline()
			print("Yeah! We managed to read the file. Here is a preview {}".format(preview))
	except FileNotFoundError :
		print("Oups! No file csv here.")




if __name__ == "__main__" :
	launch_analysis('current_mps.csv')
