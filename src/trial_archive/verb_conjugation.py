from enum import Enum
import re

### VERB PROPERTIES

class Person(Enum):
    SINGULAR_FIRST_PERSON = 'اول شخص مفرد'
    SINGULAR_SECOND_PERSON = 'دوم شخص مفرد'
    # TODO

class Tenses(Enum):
    SIMPLE_PAST = 'ماضی ساده'
    SIMPLE_PRESENT = 'حال ساده'
    # TODO

past_suffixes = {
    'م': Person.SINGULAR_FIRST_PERSON,
    'ی': Person.SINGULAR_SECOND_PERSON
    # TODO
}

past_suffixes_re = f"({'|'.join(['یم','ین','م','ن','ی'])})?"
# print(past_suffixes_re)

present_suffixes = 'م ی ه یم ین ن'.split()


def past_conjugation(bon):
### bon: بن ماضی
    suffixes = past_suffixes_re
    # prefixes = r'''(
    #     ?:
    #     بۊ|
    #         (
    #             (?:د|فۊ|وا)
    #             (ن?)
    #         )
    #     |)
    #     '''
    prefixes = r'(بۊ|(د))?'   
    regexes = {
        # Tenses.SIMPLE_PAST: '(?:' + rf'({bon})' + suffixes + ')'
        Tenses.SIMPLE_PAST: prefixes + rf'({bon})' + suffixes
    }
    print(regexes[Tenses.SIMPLE_PAST])
    return { k: re.compile(r) for k,r in regexes.items() }

def find_verb_tense(verb, bons):
###
    pass

regexes = lambda bon: {
    Tenses.SIMPLE_PAST: rf"{bon}[{'|'.join(past_suffixes)}]"
}

import re

# regex = (regexes('گفت'))['ماضی ساده']
# print(regex)
# regex_obj = re.compile(regex)
regex_obj = past_conjugation(r'\w{2,4}')[Tenses.SIMPLE_PAST]
# print(regex_obj)
string = ' که گفتار گفتیش گفتمان ما که نگفتیم و تو هم می‌گویی که چرا باید نگفت با من که نگفتم و اونام بۊگفتن بۊگفت که رفتیم نوشتم باید برن به بگم'
# print(string)
found = regex_obj.findall(string)

for v in found:
    print(''.join([x for x in v]))
# regex_obj.ma

