import os

#get input from the user
num = input('Enter the number of files: ')
fileName = input ('Enter the name of the files: ')

#create a folder
folderName = (fileName + 'Folder')
os.system('mkdir ' + folderName)

#execute the command
for i in range(0, int(num)):
	#create the file and add file number
	os.system('touch ' + fileName + str(i+1))
	#move the file to folder
	os.system('mv ' + fileName + str(i+1) + ' ' + folderName)
