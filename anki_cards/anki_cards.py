import re
import tkinter as tk
from tkinter import filedialog
from deep_translator import (GoogleTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             DeepL,
                             QCRI,
                             single_detection,
                             batch_detection)
translator = GoogleTranslator(source="french", target="german")


def open_file():
    root = tk.Tk()
    root.withdraw()

    return filedialog.askopenfilename()

def translate(text):
    return translator.translate(text, return_all=True)

def translate_batch(batch):
    translated = translator.translate_batch(batch)
    return translated

def read_file(file):
    fin = open(file, "rt", encoding='utf-8')
    fout = open("out.txt", "wt", encoding='utf-8')
    for line in fin:
        index = line.index("\t")
        try:
            to_translate = re.search(r'\((.*?)\)', line).group(1)
            print(f"translating {to_translate}...")
            translated = translate(to_translate)
            clozed = f"{{{{c1::{translated}}}}}"
            fout.write(f"{line[:index+1]}{clozed}{line[index:]}")
        except:
            fout.write(f"{line[:index+1]}Error{line[index:]}")

    fin.close()
    fout.close()
    

def main():
    read_file(open_file())

if __name__ == "__main__":
    main()