word = input("Enter a Word: ")


def vowel_Count():
    vowels = ['a', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count


print(vowel_Count())
