r = 'S O V'

# حروف اضافه
particles = '''
مئن
ؤ
-أ
 ٚ
-یه
'''.split()

def tag(sentence):
    tags = []
    verb = sentence[-1]
    sentence = sentence[:-1]
    for word in sentence:
        if word in particles:
            tags.append((word, 'particle'))
            continue
        
