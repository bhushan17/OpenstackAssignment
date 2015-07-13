import subprocess
import os 
import urllib2
#import requests
import urllib2
import csv
import sys

class StockDownload:
	'''
	classdocs
	'''


	def __init__(self):
        	'''
        	Constructor
        	'''
    
	def downloadStockCsv(self):
        	print ("\n\t Inside downloadStockCsv")
        	#response = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s=%40%5EDJI,GOOG')
        	#html = response.read()  
        
        
        	url = 'http://download.finance.yahoo.com/d/quotes.csv?s=%40%5EDJI,GOOG&f=nsl1op&e=.csv'
        	u = urllib2.urlopen(url)
        	localFile = open('./file.csv', 'w')
        	localFile.write(u.read())
        	#localFile.close()

        	#r = requests.get(url)
        	#r.content
        	#print r.content
        	print ("\n\t Outside downloadStockCsv")


class Display:
	def __init__(self):
		'''
		constructor
		'''

	def display(self):
		with open('./file.csv','rb') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=' ' , quotechar='|')
			for row in spamreader:
				print ','.join(row)

		os.remove('./file.csv')

user_input = 0

while (user_input != '3'):

	print "\n\t Enter a choice : 1) Save data to File.  2) Display on scree. 3) Exit "
	user_input = raw_input("\n\tSome input please: ex 1 or 2  as per above msg :  ")
        if (user_input == '1'):
		stockDownload = StockDownload()
		stockDownload.downloadStockCsv() 
		break
	elif (user_input == '2'):
		stockDownload = StockDownload()
		stockDownload.downloadStockCsv() 
		vardisplay = Display()
		vardisplay.display()
		break
	else:
	     print "\n\t Invalid Input"



