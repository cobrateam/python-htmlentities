from htmlentitydefs import codepoint2name


__version__ = '0.1'


def encode(source):
    new_source = ''

    for char in source:
        if ord(char) in codepoint2name:
            char = '&%s;' % codepoint2name[ord(char)]
        new_source += char

    return new_source
