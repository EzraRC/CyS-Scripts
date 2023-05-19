#script to create folder with user inputted name

#import os, to get the os.system function to execute python commands
import os

#get user folder name
folderName = input('Enter your folder name: ')

#execute command
os.system('mkdir ' + folderName)
