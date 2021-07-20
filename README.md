# Summer2021_course
A course project done for HSE university 2 lections-course about webscrapping.
More precicely, there are 2 main parts of the program: webscrapping using BeautifulSoup from the free site, where Alice in Wonderland book is held, and auto-translation API from google translation done in the second program.

Both programs are realized via classes, which have __init__ and __call__ functions, where the second one randomly selects the line from the .txt files(translated of not depends on the program) and a number of lines afterward.
In the first program **WebScraping** class has the main function *scraping_data()*, where we fetch html from url and cleanse it in comfy way to further add at the .txt file. That way we have english version of our book from the web.
In the second program **Google_translate_text** class has the main functionality in function called *translate_file()*, where we use **googletrans API** to make translation from english to russian and save the text in the new .txt file.
 
In future, program could be easily expanded to translate other books from the site http://www.literatureproject.com/index.htm pretty easily(we just need to change a little URL and job is done).
