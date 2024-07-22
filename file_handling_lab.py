print("*******************Question :- 1 *****************************")
word_to_search = "india"
word_count = 0
with open("india.txt", "r") as file:
    content = file.read()
    print(content)
    content_lower = content.lower()
    words = content_lower.split()
    word_count = words.count(word_to_search)
print(f'The word "{word_to_search}" occurs {word_count} times in the file.\n')

print("****************Question :- 2 ********************************")

with open("india.txt", "r") as file:
    lines = file.readlines()
for line in lines:  
    words = line.split()
    if len(words) > 5:
        print(line.strip())

print("***************Question :- 3 *********************************")

print("\nLetter starting with  I \n")
letter_to_search = 'i'
word_counts = 0
with open("india.txt", "r") as file:
    content = file.read()
    words = content.split()
    for word in words:
        cleaned_word = word.strip().lower()
        if cleaned_word.startswith(letter_to_search):
            word_counts += 1
print(f'Number of words starting with "{letter_to_search}": {word_counts}')

