#! /usr/bin/python3
# coding: utf-8

import analysis.csv as c_an
import analysis.xml as x_an

def main():
	c_an.launch_analysis("current_mps.csv")
	x_an.launch_analysis("xml/compteRendu/CRSANR5L15S2017E1N001.xml")

main()


if __name__ == '__main__':
	main()