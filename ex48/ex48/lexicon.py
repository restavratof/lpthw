
directions = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat')
stops = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(stuff):
    words = stuff.split()
    sentence = []
    for word in words:
        if word in directions:
            result = ('direction', word)
        elif word in verbs:
            result = ('verb', word)
        elif word in stops:
            result = ('stop', word)
        elif word in nouns:
            result = ('noun', word)
        elif convert_number(word) != None:
            result = ('number', convert_number(word))
        else:
            result = ('error', word)
        sentence.append(result)
    return sentence

stuff = input('> ')
scan(stuff)