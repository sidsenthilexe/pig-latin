def main():
    sentence_input = input('Input your sentence: ')
    sentence_split = sentence_input.split()
    final_sentence = []
    array_var = -1
    
    for term in sentence_split:
        array_var += 1
        word_broken = list(term)
        if word_broken[0] in ['a', 'e', 'i', 'o', 'u']: 
            word_output = sentence_input+"ay"
        elif word_broken[1] in ['a', 'e', 'i', 'o', 'u']:
            sentence_save = word_broken[0:1]
            del word_broken[0:1]
            save_assembled = ''.join(sentence_save)
            word_assembled = ''.join(word_broken)
            word_output = word_assembled + save_assembled + "ay"
        elif word_broken[2] in ['a', 'e', 'i', 'o', 'u']:
            sentence_save = word_broken[0:2]
            del word_broken[0:2]
            save_assembled = ''.join(sentence_save)
            word_assembled = ''.join(word_broken)
            word_output = word_assembled + save_assembled + "ay"
        elif word_broken[3] in ['a', 'e', 'i', 'o', 'u']:
            sentence_save = word_broken[0:3]
            del word_broken[0:3]
            save_assembled = ''.join(sentence_save)
            word_assembled = ''.join(word_broken)
            word_output = word_assembled + save_assembled + "ay"
        final_sentence.insert(array_var, word_output)
    final_sentence_assembled = ' '.join(final_sentence)
    print(final_sentence_assembled)

main()