import random

def random_choosing1(stmt):
    listA = stmt.split()
    try:
        while 'or' in listA:
            listA.remove('or')
    except:
        pass

    print(listA)

    return random.choice(listA)
