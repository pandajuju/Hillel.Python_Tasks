text = input("Введіть речення: ")
text_split = text.split()
word_dict = {}
char_dict = {}
char_count = 0

for word in text_split:
    count_word = word_dict.get(word, 0)
    word_dict[word] = count_word + 1
    char_count += len(word)

    for char in word:
        count_char = char_dict.get(char, 0)
        char_dict[char] = count_char + 1

print(word_dict)

statistic_dict = {}
for char in char_dict:
    statistic_dict[char] = round((char_dict.get(char) / char_count) * 100, 2)

print("Статистика використаних літер:")

for char in char_dict:
    print(f"'{char}': {char_dict.get(char)} - {statistic_dict.get(char)}%")
