

'''
future.standard_library - is used to make this class compatible for python 2.x and 3.x 
refered from - http://python-future.org/compatible_idioms.html
'''
from future.standard_library import install_aliases
install_aliases()

from urllib.request import urlopen, Request
import csv
import os 

'''
This class is to retrieve and save stock information.
'''

class StockDownload():
	'''
	classdocs
	'''


	def __init__(self):
        	'''
        	Constructor
        	'''
    
	def downloadStockCsv(self,url,filePath):
		'''
		Method is to download and save stock information file from the given url.
		'''
		try:
        		u = urlopen(url)
        		localFile = open(filePath, 'a')
			localFile.write(u.read())
	        	localFile.close()
			return 1
		except Exception as e:
			#print(e)
		 	return e 



