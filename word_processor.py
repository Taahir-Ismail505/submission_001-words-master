import string


def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    """
    uses lambda to take out all spaces and uses split to take out all punc.
    """
    sList = split('?,;. ',text.lower())
    sList= list(filter(lambda x: x != '', sList))
    #print(sList)
    return sList


def words_longer_than(length, text):
    """
    takes user input and it uues that number to filter through the list and only pulls words of that length
    """
    lengthWord = length
    text = convert_to_word_list(text)
    LenWord = list(filter(lambda word:len(word) >lengthWord,text))
    sNO = LenWord
    return sNO


def words_lengths_map(text):
    """
    counts all items in the list and makes it a dict.
    after it creates keys for it and keeps track
    """
    text = convert_to_word_list(text)
    wordLen = list(map(lambda word: len(word),text))
    wordLen.sort()
    Wordlist = {key:wordLen.count(key) for key in wordLen}
    return Wordlist 
    # ouw what you wys


def letters_count_map(text):
    """
    takes the list and changes into a string so that it can be scanned 
    and where the leeter has been found it incs. by one
    """
    text  = convert_to_word_list(text)
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    text = "".join(text)
    SMapCount = {letter: text.count(letter)for letter in alphabet_list} 
    return SMapCount


def most_used_character(text):
    """
    checks if the text is filled or not 
    and it if it is then it looks for the biggest number and displays it
    """
    if text == "":
        return None
    else:
        text = letters_count_map(text)
        SMost_chars1 = max(text,key = text.get) 
        return SMost_chars1


#words = convert_to_word_list('These are indeed interesting, an obvious understatement, times. What say you?')
#print(words)
# words1 = words_longer_than(int(input("how Big?")),'These are indeed interesting, an obvious understatement, times. What say you?')
# print(words1)
# word2 =  words_lengths_map('These are indeed interesting, an obvious understatement, times. What say you?')
# print(word2)
# word3 = letters_count_map('These are indeed interesting, an obvious understatement, times. What say you?')
# print(word3)
#word4 = most_used_character('')
#print(word4)