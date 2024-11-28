def main():
    sentence_input = input('Input your sentence: ')
    sentence_broken = list(sentence_input)
    var = 0
    
    if sentence_broken[0] in ['a', 'e', 'i', 'o', 'u']: 
        sentence_output = sentence_input+"ay"
    elif sentence_broken[1] in ['a', 'e', 'i', 'o', 'u']:
        sentence_save = sentence_broken[0:1]
        del sentence_broken[0:1]
        save_assembled = ''.join(sentence_save)
        sentence_assembled = ''.join(sentence_broken)
        sentence_output = sentence_assembled + save_assembled + "ay"
    elif sentence_broken[2] in ['a', 'e', 'i', 'o', 'u']:
        sentence_save = sentence_broken[0:2]
        del sentence_broken[0:2]
        save_assembled = ''.join(sentence_save)
        sentence_assembled = ''.join(sentence_broken)
        sentence_output = sentence_assembled + save_assembled + "ay"
    elif sentence_broken[3] in ['a', 'e', 'i', 'o', 'u']:
        sentence_save = sentence_broken[0:3]
        del sentence_broken[0:3]
        save_assembled = ''.join(sentence_save)
        sentence_assembled = ''.join(sentence_broken)
        sentence_output = sentence_assembled + save_assembled + "ay"
    print(sentence_output)
    

main()