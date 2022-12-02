import re

stop_words = '''
که به با ما تو هم می ان من
'''.split()

regex = r'(می‌|ب|ن|بۊ)?(\w{2,4})[تد]?(م|ی|د|یم|ین|ن|)'
r = re.compile(regex)

def find_possible_verbs(text):
### Tested for persian
    def f():
        found = r.findall(text)
        for v in found:
            v = ''.join([x for x in v])
            if len(v) < 2 or v in stop_words or v[-1] in 'ا'.split():
                continue
            yield v
    return list(f())

def can_be_verb(word):
    return r.fullmatch(word) != None

# print(can_be_verb('خوردن'))
# print(can_be_verb('چریدم'))
# print(can_be_verb('مواد'))
# print(can_be_verb('مجازات'))

string = ' که گفتار گفتیش گفتمان ما که نگفتیم و تو هم می‌گویی که چرا باید نگفت با من که نگفتم و اونام بۊگفتن بۊگفت که رفتیم نوشتم باید برن به بگم'
print(find_possible_verbs(string))
