# encoding: utf-8
CRACKER = {
    '!': 'a',
    ')': 'b',
    '"': 'c',
    '(': 'd',
    '/': 'e',
    '*': 'f',
    '%': 'g',
    '&': 'h',
    '>': 'i',
    '<': 'j',
    '@': 'k',
    'a': 'l',
    'b': 'm',
    'c': 'n',
    'd': 'o',
    'e': 'p',
    'f': 'q',
    'g': 'r',
    'h': 's',
    'i': 't',
    'j': 'u',
    'k': 'v',
    'l': 'w',
    'm': 'x',
    'n': 'y',
    'o': 'z',
}


def code_cracker(message):
    cracked_message = ''

    for c in message:
        try:
            cracked_message += CRACKER[c.lower()]
        except:
            cracked_message += ' '

    return cracked_message


def reverse_code_cracker(message):
    hidden_message = ''
    values = [x for x in CRACKER.values()]
    keys = [x for x in CRACKER.keys()]

    for m in message:
        try:
            hidden_message += keys[values.index(m.lower())]
        except:
            hidden_message += ' '

    return hidden_message