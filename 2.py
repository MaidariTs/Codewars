"""Your task is to write a function that takes a string
and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!"
would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel."""


def disemvowel(string_):
    array = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in string_:
        if i not in array:
            result.append(i)
    return ''.join(result)


string_ = 'This website is for losers LOL!'
print(disemvowel(string_))
