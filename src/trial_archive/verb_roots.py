
verb_roots = '''
گو
رو
میر
ساز
سوز
تاز
نواز
رم
زن
کن
رین
چین
توان
دان
جوی
پوی
روی
پر
جه
خر
بُر
بَر
روب
شنُو
آی
سای
خای
چای
سرای
آزمای
گیر
پز
شو
خور
نوش
پوش
زنگ
'''.split()

irregular_verbs = {
    'بَر': 'بردن',
    'آی': 'آمدن',
    'میر': 'مردن',
    'کن': 'کردن',
    'گیر': 'گرفتن',
    'شو': 'شدن',
    'خور': 'خوردن'
    # 'سرای': 'سرودن',
}

def verb_to_informative(v):
    '''
    v: بن مضارع
    '''
    if v in irregular_verbs:
        return irregular_verbs[v]

    stem, ending = v[:-1], v[-1]
    if ending in ['و', 'ب']:
        return stem + 'فتن'
    if ending == 'ز':
        return stem + 'ختن'
    if v[-2:] == 'ان':
        return v + 'ستن'
    if v[-2:] == 'ای' and len(v) > 3:
        return v[:-2] + 'ودن'
    if ending == 'ن':
        return stem + 'دن'
    return v + 'یدن'
        
def get_verb_lemmas():
    roots = verb_roots + list(irregular_verbs.keys())
    return roots + [verb_to_informative(v)[:-1] for v in roots]


for v in verb_roots:
    print(verb_to_informative(v))