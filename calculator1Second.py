#hackUCF CTF problem to answer complex math question in under 1 second to retrieve the flag

import requests
import math

#retrieve the html code from the website
url = ('http://ctf.hackucf.org:4000/calc/calc.php')

# create a session object
session = requests.Session()
htmlFile = (session.get(url)).text

#find the <expression> tag
expressionIndex = htmlFile.index("<expression")

#set the start and ending indices of the entire expression
start = expressionIndex + len("<expression>")
end = htmlFile.index("</expression>")

#assign the expression to string
expressionCode = htmlFile[start:end]

#get rid of the tags inbetween the expression
expression = expressionCode.replace("<br/>", " ")

#evaluate the expression
answer = str(math.floor(eval(expression)))

#create tuple for the data
#inputTag = {'input type':"text", 'name':"answer", 'class':"input", 'value':"\"" + answer + "\""}
postAnswer = {'answer': answer}

#post answer
flag = session.post(url = url, data = postAnswer)
print(flag.text)
