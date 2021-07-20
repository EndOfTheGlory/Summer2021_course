import requests
from bs4 import BeautifulSoup
from typing import List
import random

# Program that read Alice in Wonderland book with all it's chapters
# With little adjustment can be made into reading other books from the same site


class WebScraping:
    def __init__(self, domen, book, out_file_name):
        self.domen = domen
        self.book = book
        self.out_file_name = out_file_name

    def __call__(self) -> List[str]:
        # Select random lines from written book
        file = open(self.out_file_name, "r")
        our_answer = list()
        lines = file.readlines()
        number_of_lines = len(lines)
        index = random.randint(0, number_of_lines - 1)
        # selecting 10 lines after that
        i = 0
        while index + i < number_of_lines and i < 10:
            our_line = lines[index + i]
            print(our_line)
            our_answer.append(our_line)
            i += 1
        return our_answer

    def scraping_data(self):
        book_name = self.book
        CORRECT_RESPONSE = 200
        chapters = []
        chapters_contents = []

        for page_num in range(1, 1000):
            url = f"{self.domen}{book_name}/{book_name}_{page_num}.htm"
            try:
                response = requests.get(url, timeout=100)
            except:
                break
            if response.status_code != CORRECT_RESPONSE:
                break
            soup = BeautifulSoup(response.content, "html.parser")
            chapter_title = soup.title.contents
            # print(chapter_title)
            # гораздо более простой поиск. На 2 странице я понял, что меня надули и надо все заново...
            meaningful_text = []
            if page_num == 1:
                paragraphs = soup.find_all("p", {"dir": "ltr"})
                # print(paragraphs)
                for one_p in paragraphs:
                    whats_under_the_tag = one_p.contents
                    whats_under_the_tag = whats_under_the_tag[0]
                    whats_under_the_tag = whats_under_the_tag.replace("\xa0", " ")
                    meaningful_text.append(whats_under_the_tag)
            else:
                all_paragraphs = soup.find_all("p")
                paragraphs = []
                print(all_paragraphs[3].text.strip())
                for one_par in all_paragraphs:
                    paragraphs.append(one_par.text)
                # print(paragraphs)
                for one_p in paragraphs:
                    # print(one_p)
                    one_p = one_p.replace("\xa0", " ")
                    one_p = one_p.replace("\r\n", "")
                    meaningful_text.append(one_p)
            print(meaningful_text)
            chapters_contents.append(meaningful_text)
            chapters.append(chapter_title)
        file = open(self.out_file_name, "w")
        total_num_of_chaps = len(chapters)
        file.seek(0)
        for i in range(total_num_of_chaps):
            file.write(chapters[i][0])
            for one_str in chapters_contents[i]:
                file.write(one_str)
        file.truncate()


working = WebScraping(
    "http://www.literatureproject.com/", "alice", "whole_text_eng.txt"
)
working.scraping_data()
answ = working()
print(answ)
