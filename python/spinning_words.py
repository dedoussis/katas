def spin_words(sentence):
    words = sentence.split(' ')
    for idx, word in enumerate(words):
        if len(word) >= 5:
            words[idx] = word[::-1]
    return ' '.join(words)