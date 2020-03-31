#! /usr/bin/python3
# coding: utf-8

import analysis.setOfParliamentMembers as sopm
import os

# def launch_analysis(data_file):
# 	directory = os.path.dirname(os.path.dirname(__file__))
# 	path_to_file = os.path.join(directory,'data',data_file)
	
# 	with open(path_to_file, 'r') as file :
# 		preview = file.readline()
# 		print("Yeah! We managed to read the file. Here is a preview {}".format(preview))

def launch_analysis(data_file, by_party = True):
	
	directory = os.path.dirname(os.path.dirname(__file__))
	path_to_file = os.path.join(directory,'data',data_file)

	o_sopm = sopm.SetOfParliamentMembers("All MPs")
	o_sopm.data_from_csv(path_to_file)
	o_sopm.display_chart()

	if by_party :
		for party, s in o_sopm.split_by_political_party().items():
			s.display_chart()



if __name__ == "__main__" :
	launch_analysis('current_mps.csv')
