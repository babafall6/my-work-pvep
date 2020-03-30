#! /usr/bin/python3
# coding: utf-8

import argparse
import analysis.csv as c_an
import analysis.xml as x_an

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-e", "--extension",help="""Type of file to analyse. Is it a CSV or an XML?""")
	parser.add_argument("-d", "--datafile",help="""CSV file containing pieces of information about the members of parliment""")
	return parser.parse_args()



if __name__ == "__main__":
	args = parse_arguments()
	datafile = args.datafile
	if datafile :
		if args.extension == 'xml':
			#'xml/compteRendu/CRSANR5L15S2017E1N001.xml'
			x_an.launch_analysis()
		elif args.extension == 'csv':
			#'current_mps.csv'
			c_an.launch_analysis(datafile) 
	else:
		print("Please give filename CSV")