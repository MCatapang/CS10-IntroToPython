# def stemmer(text):
#     suffix_arr = ['ed', 'ly', 'ing']
#     text_arr = text.split()
#     newtext_arr = []
#     for word in text_arr:
#         len_MoreThan3 = len(word) > 3
#         mod_word = word
#         modded = False
#         if(len_MoreThan3):
#             suffix_2 = word[-2]+word[-1]
#             suffix_3 = word[-3]+suffix_2
#             if (suffix_2 in suffix_arr):
#                 mod_word = word[0:-2]
#                 modded = True
#             elif (suffix_3 in suffix_arr):
#                 mod_word = word[0:-3]
#                 modded = True
#         if(modded and len(mod_word) > 8):
#             mod_word = mod_word[0:8]
#         newtext_arr.append(mod_word)
#     s = " "
#     output_str = s.join(newtext_arr)
#     return output_str

# test_input = "police agent everybody differen run public though become inside air despite matter agree customer political mrs writer oil society accord skill radio free choice very forget behavior best start onto sister religious mind wait happen move someone our still news push and determine everyth bad you between entire paper give government dark effect thought pass official close rather church grow use owner mission world without right democratic wrong far economic worry then specific fall part who such international each directio might drug worker wife understa daughter treatment letter be analysis bill occur responsibility himself arrive get too long themselv sign"

# print(stemmer(test_input))





# from string import ascii_lowercase

# def cryptogram(message, rotation=4):
#     rotated = ascii_lowercase[rotation:] + ascii_lowercase[:rotation]
#     cipher = {o: n for o, n in zip(ascii_lowercase, rotated)}

#     encoded = []
#     for char in message.lower():
#         if char in cipher:
#             encoded.append(cipher[char])
#         else:
#             encoded.append(char)

#     return "++++" + ''.join(encoded) + "++++"


# print(cryptogram("SUPER"))



# def test():
#     results = []
#     x  = 5
#     for i in range(0,5):
#         x=2
#         x += i
#         results.append(x)
#     results.append(x)
#     print(results)

# test()


number1 = 2.32
number2 = 5/3

result = number1 + format(number2, '.2f')
print(result)