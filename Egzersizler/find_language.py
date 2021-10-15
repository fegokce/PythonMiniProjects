from langdetect import detect

# language = detect("bir iki üç dört beş")
# print("Language: " + language)

# language = detect("one two three four five")
# print("Language: " + language)

# language = detect("eins zwei drei vier fünf")
# print("Language: " + language)

# language = detect("uno due tre quattro cinque")
# print("Language: " + language)

language = input("Write something and let's find out what language it is: ")
print("Language: " + detect(language))