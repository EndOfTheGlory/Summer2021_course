# API version 4.0.0rc !!!
import googletrans
from googletrans import Translator
import random
from typing import Dict, Tuple, List

print(googletrans.LANGUAGES)
russian_text = (
    "Когда ты разбираешься с библиотеками и "
    "почти закончил проект, но дедлайн только что прошел: Потрачено"
)
translator = Translator()
result = translator.translate(russian_text, src="ru", dest="en")
# ОНО ЖИВОЕ!!!! МХА-ХА-ХА-ХА-ХА!!!
print(result.text)


class Google_translate_text:
    def __init__(self, file_to_read, file_to_write):
        self.file_to_read = file_to_read
        self.file_to_write = file_to_write

    def __call__(self) -> List[str]:
        # Get random part of the text(assuming we have already translated the whole thing)
        file_rus_read = open(self.file_to_write, "r")
        rus_lines = file_rus_read.readlines()
        number_of_lines = len(rus_lines)
        index = random.randint(0, number_of_lines - 1)
        # For example, let's take this line and 5 after that
        to_add = 0
        example = list()
        while index + to_add < number_of_lines and to_add < 6:
            new_line = rus_lines[index + to_add]
            print(new_line)
            example.append(new_line)
            to_add += 1
        return example

    def translate_file(self):
        file = open(self.file_to_read, "r")
        lines = file.readlines()
        file_to_write_translated = open(self.file_to_write, "w")
        total_lines_to_read = len(lines)
        # Using to rewrite the file
        file_to_write_translated.seek(0)
        for i in range(total_lines_to_read):
            translated_line = translator.translate(lines[i], src="en", dest="ru")
            file_to_write_translated.write(translated_line.text)
            file_to_write_translated.write("\n")
            # To end program early(hate the waiting)
            if i == 10:
                break
        file_to_write_translated.truncate()


google_translator = Google_translate_text(
    "whole_text_eng.txt", "whole_translated_text.txt"
)
google_translator.translate_file()
# checking __call__
answ = google_translator()
print(answ)
