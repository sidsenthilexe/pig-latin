# import modules for gui
import tkinter
from tkinter import ttk
import sv_ttk
import darkdetect

# import modules for playing sound
from gtts import gTTS
from playsound import playsound

# import modules for ai and api key
import os
from dotenv import load_dotenv
# from transformers import pipeline

language = 'en'

# set up ai
load_dotenv()
API_KEY = os.getenv('ENV_API_KEY')

# question_answerer = pipeline(task="question-answering")

# set up root window
root = tkinter.Tk()
root.geometry("400x350")
root.resizable(False, True)
root.title("Pig Latin Translator")

# init global variables
sentence_input_stringvar = tkinter.StringVar()
global final_sentence_assembled
global sentence_input
sentence_input = ''


# function to copy output text to the clipboard
def copy_clipboard():
    global final_sentence_assembled
    root.clipboard_clear()
    root.clipboard_append(final_sentence_assembled)


# function to speak the output text
def play_audio():
    global final_sentence_assembled
    if os.path.exists('speak.mp3'):
        os.remove('speak.mp3')
    audio_object = gTTS(text=final_sentence_assembled, lang=language, slow=False)
    audio_object.save('speak.mp3')
    playsound('speak.mp3')
    

# function to use user input as the ai prompt, then translate to pig latin
# def ai():
#     global sentence_input
#     question = sentence_input
#     generated_text = question_answerer(question)
#     sentence_input = generated_text
#     print(generated_text)
#     # main()
    

# function to directly go to translation
def translate():
    global sentence_input
    sentence_input = sentence_input_stringvar.get()
    main()


# translate the input text to pig latin
def main():
    global final_sentence_assembled
    global sentence_input
    
    # split up the sentence into words
    sentence_split = sentence_input.split()
    final_sentence = []
    array_var = -1

    # for each word
    for term in sentence_split:
        array_var += 1
        word_broken = list(term)
        
        # for each letter in the word
        for word_term in word_broken:
            
            # decide how to translate it (see README)
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
        # insert the translated word into the array for output sentence
        final_sentence.insert(array_var, word_output)
        
    # assemble the final sentence
    final_sentence_assembled = ' '.join(final_sentence)
    final_sentence_assembled = final_sentence_assembled.lower()
    
    # output the sentence and create buttons
    final_sentence_label = ttk.Label(root, text=f"This sentence in Pig Latin is: " + final_sentence_assembled, wraplength=350)
    final_sentence_label.pack(side=tkinter.TOP, pady = 10)

    copy_text_button = ttk.Button(root, text="Copy", command=copy_clipboard)
    copy_text_button.pack(side=tkinter.TOP, pady=10)
    
    play_audio_button = ttk.Button(root, text="Speak", command=play_audio)
    play_audio_button.pack(side=tkinter.TOP, pady=10)


# create main ui elements
sentence_input_label = ttk.Label(root, text="Enter the text to be translated:")
sentence_input_label.pack(side=tkinter.TOP, pady = 10)

sentence_input_entry = ttk.Entry(root, textvariable=sentence_input_stringvar)
sentence_input_entry.pack(side=tkinter.TOP, pady = 10)
sentence_input_entry.focus()

enter_button = ttk.Button(root, text="Translate", command=translate)
enter_button.pack(side=tkinter.TOP, pady = 10)

# ai_button = ttk.Button(root, text="Pig Latin AI", command=ai)
# ai_button.pack(side=tkinter.TOP, pady=10)

sv_ttk.set_theme(darkdetect.theme())

root.mainloop()
