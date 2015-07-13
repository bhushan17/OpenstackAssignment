#!/usr/bin/env python3

import ConfigParser
import os
from  STOCKDOWNLOAD import  StockDownload
from DISPLAY import Display
"""
This is the main Module
"""
if __name__ == '__main__':
	pass
'''
Read the configuration from stock_config.cfg 
This incliudes menu messages , user input messages, Invalid and success/fail message.
Also http url and file paths are configure.
'''
Config = ConfigParser.ConfigParser()
Config.read("STOCK_CONFIG.cfg")

menu_msg = Config.get("stockInfoMessage","menu")
user_input_msg = Config.get("stockInfoMessage","userinput")
invalid_input_msg = Config.get("stockInfoMessage","invalidinput")
success_msg = Config.get("stockInfoMessage","sucessful")
fail_msg = Config.get("stockInfoMessage","fail")
exit_msg = Config.get("stockInfoMessage","exit")

url_string = Config.get("stock","url")
#file_path = Config.get("file","path")
newfile_path = Config.get("file","newpath")

os.system('clear') 
user_input = 0

while(user_input != 3):
	"""
	Read user input to take appropriate action.
	"""
        print (menu_msg)
        user_input = input(user_input_msg)
	user_input = int(user_input)
        if (user_input == 1):
		'''
		Download stock file and save it.
		'''
               	stockDownload = StockDownload()
		file_path = input('\n Enter file path and file name in " ". ')
               	result=stockDownload.downloadStockCsv(url_string,file_path)
		if(result==1):
			print ("\n********************************************************************************************************** ")
			print ( "\n\t"+file_path+"   " + success_msg + "   created")
			print ("\n********************************************************************************************************** ")
		else:
			print result
			print (fail_msg)

       	elif (user_input == 2):
		'''
		Read the stock data from the given URL and display it on console
		'''
               	stockDownload = StockDownload()
               	result=stockDownload.downloadStockCsv(url_string,newfile_path)
		if(result):
               		displayStock = Display()
			print ("\n********************************************************************************************************** ")
                	displayStock.display(newfile_path)
			print ("\n********************************************************************************************************** ")
               	else:
			print(fail_msg)
        elif(user_input == 3):
		'''
		Exit from the application.
		'''
		print ("\n********************************************************************************************************** ")
	        print (exit_msg)
		print ("\n********************************************************************************************************** ")
		
       	else:
         	print (invalid_input_msg)

