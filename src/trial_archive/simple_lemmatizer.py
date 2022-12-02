from verb_roots import get_verb_lemmas
from verb_finder import can_be_verb

verb_lemmas = get_verb_lemmas()

def lemmatize(word):    
    if can_be_verb(word):
        if word in verb_lemmas:
            return word
        last_three_letters = word[-3:]
        if last_three_letters in ['مون','تون','شون']:
            w = lemmatize(word[:-3])
            if w in verb_lemmas:
                return w
        last_two_letters = word[-2:]
        if last_two_letters in ['یی','یم','ین','ید']:
            w = lemmatize(word[:-2])
            if w in verb_lemmas:
                return w
        last_letter = word[-1]
        if last_letter in ['ی','م','ن'] + ['ش', 'ت', 'م']:
            w = lemmatize(word[:-1])
            if w in verb_lemmas:
                return w
    return word

def lemmatize_rewritten(word):
    if can_be_verb(word):
        endings = [''] + ['مون','تون','شون'] + ['یی','یم','ین','ید'] + ['د','ی','م','ن'] + ['ش', 'ت', 'م']
        for i in range(3,-1,-1):
            if i >= len(word):
                continue
            if word[-i:] in endings:
                w = lemmatize_rewritten(word[:-i])
                if w in verb_lemmas:
                    return w
        beginnings = ['می‌', 'ب', 'ن']
        for i in range(2,0,-1):
            if i >= len(word):
                continue
            if word[:i] in beginnings:
                w = lemmatize_rewritten(word[i:])
                if w in verb_lemmas:
                    return w
        return word
    '''
    TODO:
     هم فعل مضارع هم ماضی باید یه لم پس بدن
     بهینه‌تر هست که هرلایه چک نشه آیا لم هست٬ بلکه یه بول هم پس بدیم
    '''

    return word

string = '''
من آزمودم که چگونه شد چنین چیزی را پرسید که رفت و داد زد که گفتیم رفتین می‌رود می‌گویم برویم نخوریم زدن
'''

for word in string.split():
    if not can_be_verb(word):
        continue
    print(word, lemmatize_rewritten(word))