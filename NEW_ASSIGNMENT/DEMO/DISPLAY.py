
import os
import csv
'''
This Class is use to Display content.
'''
class Display():
        def __init__(self):
                '''
                constructor
                '''

        def display(self,filePath):
		'''
		This method is for displaying content of provided csv file.
		'''
                with open(filePath,'rb') as csvfile:
                        filereader = csv.reader(csvfile, delimiter=',' , quotechar='|')
                        for row in filereader:
				#This print is use for proper formatting of fields
				print ('\t'.join(['%10s' % (row[col]) for col in xrange(len(row))]))
                os.remove(filePath)

