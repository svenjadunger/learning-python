word = input("Enter a word ")

print(word.lower().count('a'))
reverse_word = ''.join(reversed(word))
print(reverse_word)

print(word[::2])
print(word[-3:])

replaced_word = word.replace(' ', '***')
print(replaced_word)