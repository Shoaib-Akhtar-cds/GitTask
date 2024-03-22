sUserText = ""
sUserText = input("Please Enter Some Text : ")
print(f"The Length Of Text is {len(sUserText)}")
sLastChar =sUserText[len(sUserText)-1] #getting last character of sentence
sTextLastCharRplaced=  sUserText.replace(sLastChar,"@") #replacing last character with @
print(sTextLastCharRplaced)

sLast3CharsReversed = sUserText[len(sUserText):len(sUserText)-4:-1] #Getting last three characters in reversed order
print(sLast3CharsReversed)

sRequiredWord = sUserText[0:3] + sUserText[len(sUserText)-2:len(sUserText)]
print(sRequiredWord)