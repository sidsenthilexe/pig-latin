def main():
    sentence_input = input('Input your sentence: ')
    sentence_split = sentence_input.split()
    final_sentence = []
    array_var = -1

    for term in sentence_split:
        array_var += 1
        word_broken = list(term)
        for word_term in word_broken:
            if word_term in ['a', 'e', 'i', 'o', 'u']:
                word_term_index = word_broken.index(word_term)
                if word_term_index == 0:
                    word_assembled = ''.join(word_broken)
                    word_output=word_assembled+"way"
                    break
                else:
                    sentence_save = word_broken[0:word_term_index]
                    del word_broken[0:word_term_index]
                    save_assembled = ''.join(sentence_save)
                    word_assembled = ''.join (word_broken)
                    word_output = word_assembled+save_assembled+"ay"
                    break
        final_sentence.insert(array_var, word_output)
        
    final_sentence_assembled = ' '.join(final_sentence)
    final_sentence_assembled = final_sentence_assembled.lower()
    print("this sentence in Pig Latin is: " + final_sentence_assembled)

main()
