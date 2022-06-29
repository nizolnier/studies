def get_length(string):
    length = 0
    for letter in string:
        length += 1

    return length

print(get_length("banana"))

def letter_check(word, letter):
    for l in word:
        if letter == l:
            return True
    return False

def contains(big_string, little_string):
    return little_string in big_string

def common_letters(string1, string2):
    common = []
    for letter in string1:
        if (letter in string2) and not (letter in common):
            common.append(letter)
    return common
