sMessage = "The!Quick!Brown!Fox!Jumps!Over!The!Lazy!Dog."
sMessage = sMessage.replace("!"," ")
print(sMessage) #string without !
print (sMessage.upper()) #string in capital words
print(sMessage[len(sMessage)::-1]) #string in reverse order starting from last word to all the way to first word by steping back 1 i.e -1 argument of string slice

