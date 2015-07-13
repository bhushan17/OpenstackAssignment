from StockDownload import StockDownload
from Display import Display
import sys

if __name__ == '__main__':
	userinput = '0' 


	while(userinput != '3' ):
        	#global user_input
		print "First Time"
		print userinput
        	print "\n\t Enter a choice : 1) Save data to File.  2) Display on scree. 3) Exit "
        	userinput = str(raw_input("\n\tSome input please: ex 1 or 2  as per above msg :  "))
		print "Second Time"
		print userinput
        	if (userinput == '1'):
                	stockDownload = StockDownload()
                	stockDownload.downloadStockCsv()
		        sys.exit(1)	
			#user_input = '3'

        	elif (userinput == '2'):
                	stockDownload = StockDownload()
                	stockDownload.downloadStockCsv()
                	vardisplay = Display()
                	vardisplay.display()
                	#break
		        sys.exit(1)	
			#user_input = '3'

        	else:
             		print "\n\t Invalid Input"

