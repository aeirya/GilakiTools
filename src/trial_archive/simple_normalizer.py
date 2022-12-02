alph = set('ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهیآاَاِاُ'+' ٚ‌ؤۊئأ') # also has نیم‌فاصله
punc = set('.،'+'!؟'+'()' + '-')

def standard_letter(char):
    non_std_to_std = {
        'ي': 'ی',
        '٫': '،',
        ',': '،',
        '?': '؟'
    }
    char = non_std_to_std.get(char, char)
 
    if not (char in alph or char in punc or char in [' ']):
        return ''

    return char

def normalize(text):
    # standardize letters
    std = ''.join(map(standard_letter, list(text)))
    # add whitespace before and after punctuation marks
    with_ws = ''.join(map(lambda char: f' {char} ' if char in punc else char, list(text)))
    # remove excess whitespace
    text = ' '.join(with_ws.split())
    return text