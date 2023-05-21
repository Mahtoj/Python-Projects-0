#file: 5-21-23-WordSearch.py
#auth: Jotham King
#date: 5/21/2023
#func: word search example

#def search, where user will input text and then input word, if word is in text output word found.
def search(text, word):
  if word in text:
    return "Word found"
  else:
    return "Word not found"


text = input("Enter text: ")
word = input("Enter word to search for: ")

print(search(text, word))