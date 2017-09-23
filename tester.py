path = 'C:/Users/Mig/Desktop/Microsoft-Logo-3.jpg'
word = path.split('/')
print(word)
last_word = word[-1]
print(last_word)

path = path.replace(last_word, '')
print(path)
