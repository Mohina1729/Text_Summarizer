
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from sys import exec_prefix
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import browserhistory as bh
import os


LANGUAGE = "english"
SENTENCES_COUNT = 10
file=r"C:\Users\mohina\extracted_text.txt"

def fetch_urls():
    obj= bh.get_browserhistory()
    urls=[]
    for key,val in obj.items(): #keys are browsers [chrome,safari,firefox]
        for i in obj[key]:      #Values are a tuple of (url,title,last visited time)
            urls.append(i[0])
    urls=urls[0:5] #Recent 10 urls
    print(urls)
    generate_summary(urls)


def generate_summary(urls):
    for url in urls:
        try:
            parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
        except:
            continue
        stemmer = Stemmer(LANGUAGE)
        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        with open(file, "a", encoding="utf-8") as f:
            for sentence in summarizer(parser.document, SENTENCES_COUNT):
                #print(str(sentence))
                f.write(str(sentence) + "\n")
            f.write("\n")
    os.system(file)
  
    
print("Give access to browser history?")
res=input("Enter Yes/No:")
if res=="Yes":
    fetch_urls()







