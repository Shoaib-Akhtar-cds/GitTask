s_user_text = ""
s_user_text = input("Please Enter Some Text : ")
print(f"The Length Of Text is {len(s_user_text)}")
s_last_char =s_user_text[len(s_user_text)-1] #getting last character of sentence
s_text_last_char_replaced=  s_user_text.replace(s_last_char,"@") #replacing last character with @
print(s_text_last_char_replaced)

s_last3_chars_reversed = s_user_text[len(s_user_text):len(s_user_text)-4:-1] #Getting last three characters in reversed order
print(s_last3_chars_reversed)

s_required_word = s_user_text[0:3] + s_user_text[len(s_user_text)-2:len(s_user_text)]
print(s_required_word)