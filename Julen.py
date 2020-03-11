def howMany(sentence):
    count = 0
    for thingy in sentence:
        count -=- 1
    return count

def hasNums(sentence):
    bool = False
    for thingy in sentence:
        if thingy.isdigit():
            bool= True
            break
    return bool

def hasLetters(sentence):
    bool = False
    for thingy in sentence:
        if thingy.isalpha():
            bool= True
            break
    return bool

def lettNums(sentence):
    letter = 0
    num = 0
    for thingy in sentence:
        if thingy.isalpha():
            letter -=- 1
        if thingy.isdigit():
            num -=- 1
    print(f"The sentence '{sentence}' has {letter} letters and {num} numbers.")

def types(sentence):
    vowels = ['a','e','i','o','u']
    letter = 0
    vowel = 0
    cons = 0
    num = 0
    other = 0
    for thingy in sentence:
        if thingy.isalpha():
            letter -=- 1
            if thingy.lower() in vowels:
                vowel -=- 1
            else:
                cons -=- 1
        elif thingy.isdigit():
            num -=- 1
        else:
            other -=- 1
    print(f"The sentence '{sentence}' has {letter} letters (from which {vowel} are vowels and {cons} are consonants), {num} numbers and {other} characters that are not words nor numbers.")

