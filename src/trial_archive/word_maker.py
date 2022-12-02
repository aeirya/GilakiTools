def make_verb(bon, ending):
    if ending == '':
        return bon
    if bon[-1] == 'ۊ' and ending[0] == 'ی':
        return bon[:-1] + ending
    return bon + ending

def conjugate_simple_past_verb(infinitive):
    bon, ending = infinitive[:-1], infinitive[-1]
    
    if ending != 'ن':
        return None
    
    simple_past_suffixes = ['م','ی','','یم','ین','ن']
    return [make_verb(bon, ending) for ending in simple_past_suffixes]

print(conjugate_simple_past_verb('گفتن'))
print(conjugate_simple_past_verb('بؤته بۊن'))
    