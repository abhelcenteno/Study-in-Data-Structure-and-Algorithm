import random


def generate_sentence(str_len):
    alphabet = 'abcdefghijklmnopqrstuvwxyz '
    sentence = ''
    for letter in range(str_len):
        sentence += alphabet[random.randrange(27)]
    return sentence


def score(to_evaluate):
    counter = 0
    target = 'methinks it is like a weasel'
    for i in range(len(target)):
        if to_evaluate[i] == target[i]:
            counter += 1
    return counter / len(target)


if __name__ == '__main__':
    sentence = generate_sentence(28)
    current_score = score(sentence)
    best = (sentence, current_score)

    while current_score < 1:
        sentence = generate_sentence(28)
        current_score = score(sentence)
        if current_score > best[1]:
            best = (sentence, current_score)
            print(best)
