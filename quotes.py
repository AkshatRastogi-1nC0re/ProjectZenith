import random
import os

def get_quote():

    quote_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'quotes.txt')
    f = open(quote_file, 'r')
    txt = f.read()
    lines = txt.split('\n.\n')

    quote_raw = random.choice(lines)
    listA = quote_raw.split('"')
    listB = []
    for items in listA:
        if items != "":
            for i in range(items.count("\n")):
                items = items.replace('\n', '')
            for i in range(items.count("--")):
                items = items.replace('--', '')
            listB.append(items)

    return listB[0], listB[1]

# quote, author = get_quote()
# print(type(author))

