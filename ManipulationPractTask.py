s_user_text = ""
s_user_text = input("Please Enter Some Text : ")
print(f"The Length Of Text is {len(s_user_text)}")
s_last_char =s_user_text[len(s_user_text)-1] #getting last character of sentence
s_text_last_char_replaced=  s_user_text.replace(s_last_char,"@") #replacing last character with @
print(s_text_last_char_replaced)

sLast3CharsReversed = sUserText[len(sUserText):len(sUserText)-4:-1] #Getting last three characters in reversed order
print(sLast3CharsReversed)

sRequiredWord = sUserText[0:3] + sUserText[len(sUserText)-2:len(sUserText)]
print(sRequiredWord)