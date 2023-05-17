import os

#get url from user
userURL = input('Enter the URL here ')

#save the url
os.system('wget ' + userURL)

#save into folder
os.system('cp index.html /home/kali/Documents')
