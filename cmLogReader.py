from __future__ import print_function
import sys
import csv

logPath = sys.argv[1]
w = "[Warn]"
n = 0
with open(logPath) as cmLog:
	found = False
	for line in cmLog:
		if w in line:
			n = n+1
			print("%d. %s" % (n, line), end='')
			print(next(cmLog), end='')
			print('\n \n')
			found = True 
	if not found:
		print('No CloudMigrator warnings found')
print("\nThe total number of warnings in this log file is: %d \n \n" % (n))
print("Current log file being searched: %s \n \n \n" % (logPath))