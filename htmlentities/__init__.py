from htmlentitydefs import codepoint2name, name2codepoint

import re


__version__ = '0.2.1'


def encode(source):
    new_source = ''

    for char in source:
        if ord(char) in codepoint2name:
            char = '&%s;' % codepoint2name[ord(char)]
        new_source += char

    return new_source


def decode(source):
    for entitie in re.findall('&(?:[a-z][a-z0-9]+);', source):
        entitie = entitie.replace('&', '')
        entitie = entitie.replace(';', '')
        source = source.replace('&%s;' % entitie, unichr(name2codepoint[entitie]))
    return source
