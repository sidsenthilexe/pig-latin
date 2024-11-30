import tkinter
from tkinter import ttk

import sv_ttk
import darkdetect

root = tkinter.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Pig Latin Translator")

sentence_input_stringvar = tkinter.StringVar()
sentence_input = ''

def main():
    sentence_input_stringvar.get()
    sentence_input = sentence_input_stringvar
    print(sentence_input)
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

sentence_input_label = ttk.Label(root, text="Enter the text to be translated:")
sentence_input_label.pack(side=tkinter.TOP, pady = 10)

sentence_input_entry = ttk.Entry(root, textvariable=sentence_input_stringvar)
sentence_input_entry.pack(side=tkinter.TOP, pady = 10)
sentence_input_entry.focus()

enter_button = ttk.Button(root, text="Go!", command=main)
enter_button.pack(side=tkinter.TOP, pady = 10)

sv_ttk.set_theme(darkdetect.theme())
root.mainloop()
