words = []
lenght = []

for user in range(10):
    x = input("         Please Enter a Word: ")
    words.append(x)
            
while True:
    letters = input("         Enter the number of letters in a word that you want to Display: ")
    if letters.isdigit():
        letters = int(letters)
        break

for word in words:
    
    if len(word) >= letters:
        lenght.append(word)
        
    else:
        continue
print(f"          Here are the words that has {letters} letters of: {lenght}")             