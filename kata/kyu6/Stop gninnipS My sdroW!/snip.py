def spin_words(sentence):
    sentence = sentence.split(' ')
    new_string = []
    for i in sentence:
        if len(i) < 5:
            i = i
            new_string += [i]
        else:
            i = i[::-1]
            new_string += [i]
    return ' '.join(new_string)
