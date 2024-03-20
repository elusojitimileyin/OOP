# class Sentence:
#     def __init__(self):
#         pass

def output_letter_digit(sentence):
    letter = 0
    digit = 0
    for word in sentence:
        if word.isalaph():
            letter += 1
        if word.isdigit():
            digit += 1

    return f'LETTER{letter} DIGIT{digit} '
