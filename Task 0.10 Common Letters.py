word1 = input('Enter First Word: ')
word2 = input('Enter Second Word: ')
List3 = []


def common_letters():
    lower_word1 = word1.lower()
    lower_word2 = word2.lower()
    for letter in lower_word1:
        if letter in lower_word2:
            List3.append(letter)

common_letters()
seperator = ','
print('Common Letters: ' + seperator.join(List3))
