#! /usr/bin/python3
# coding: utf-8

import logging as lg
import argparse
import re

import analysis.csv as c_an
import analysis.xml as x_an


lg.basicConfig(level=lg.DEBUG)

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-e", "--extension",help="""Type of file to analyse. Is it a CSV or an XML?""")
	parser.add_argument("-d", "--datafile",help="""CSV file containing pieces of information about the members of parliment""")
	parser.add_argument("-p", "--byparty",action='store_true',help="""Display graph for each political party""")
	parser.add_argument("-i", "--info",action='store_true',help="""Information about the file""")

	return parser.parse_args()



if __name__ == "__main__":
	args = parse_arguments()
	try:
		datafile = args.datafile
		if not datafile :
			raise Warning('You must indicate a datafile !')
	except Warning as e:
		lg.warning(e)
	else:	
		try:
			e = re.search('^.+\.(\D{3})$', args.datafile)
			extension = e.group(1)

			if extension == 'xml':
				#'xml/compteRendu/CRSANR5L15S2017E1N001.xml'
				x_an.launch_analysis(datafile)
			elif extension == 'csv':
				#'current_mps.csv'
				c_an.launch_analysis(datafile,args.byparty, args.info) 

		except FileNotFoundError as e :
			lg.critical("Ow :( The file was not found. \nHere is the original message of the exception : {}".format(e))
	finally:
		lg.info('#'*10 + ' Analysis is over ' + '#'*10)


