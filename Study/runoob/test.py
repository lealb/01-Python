# -*- coding: utf-8 -*-
# Description: 
# 2017/12/27 18:04


if __name__ == '__main__':
    favorite_languages = {
        'jen': ['Python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell'],
        'Ivring': []
    }
    for k, v in favorite_languages.items():
        if v:
            if len(v) == 1:
                print(k + "'s favorite languages is ")
                print("\t" + v[0])
            else:
                for language in v:
                    print(k + "'s favorite languages are ")
                    print("\t" + language)
        else:
            print(k + "doesn't like coding!")
