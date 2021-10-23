word = input("Enter a Word: ")
vowel_list = []


def vowel_Count():
    vowels = ['a', 'e', 'i', 'o', 'u']
    lower_case_word = word.lower()

    for letter in lower_case_word:
        if letter in vowels:
            vowel_list.append(letter)


vowel_Count()
seperator = ','
print('Vowels: ' + seperator.join(vowel_list))
