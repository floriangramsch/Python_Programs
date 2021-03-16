import re
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

def translate(text):
    translated = translator.translate(text, return_all=True)
    return translated

def translate_batch(batch):
    translated = translator.translate_batch(batch)
    return translated

def read_file(file):
    fin = open(file, "rt")
    fout = open("out.txt", "wt")
    for line in fin:
        index = line.index("\t")
        try:
            to_translate = re.search(r'\((.*?)\)', line).group(1)
            translated = translate(to_translate)
            clozed = f"{{{{c1::{translated}}}}}"
            fout.write(f"{line[:index+1]}{clozed}{line[index:]}")
        except:
            fout.write(f"{line[:index+1]}Error{line[index:]}")

    fin.close()
    fout.close()

read_file("PetitPrince_1_2.txt")