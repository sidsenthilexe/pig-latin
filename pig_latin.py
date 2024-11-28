def main():
    sentence_input = input('Input your sentence: ')
    sentence_broken = list(sentence_input)
    if sentence_broken[0] in ['a', 'e', 'i', 'o', 'u']: 
        sentence_output = sentence_input+"ay"
    elif sentence_broken[1] in ['a', 'e', 'i', 'o', 'u']:
        sentence_save = sentence_broken[0]
        print(sentence_save)
        del sentence_broken[0]
        print(sentence_broken)
        sentence_assembled = ''.join(sentence_broken)
        print(sentence_assembled)
        sentence_output = sentence_assembled + sentence_save + "a"
    print(sentence_output)

main()