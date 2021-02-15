from PyDictionary import PyDictionary

def dictionary_lol(letter):
    def meaning(word):
        dic = PyDictionary()
        mean = dic.meaning(word)
        return mean

    word_temp = meaning(letter)

    for state in word_temp:
        return str(word_temp[state][0])


#
# print(dictionary_lol("Astronomy"))

#ENDOFCODE- Made By Akshat Rastogi