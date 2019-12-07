import nltk
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
import textblob


comment_list = []
def is_english_word(word):
    dictionary = dict.fromkeys(nltk_words.words(),None)
    try:
        x = dictionary[word]
        return True
    except KeyError:
        return False

for i in range(00,970,10):
    
    url = 'https://steamcommunity.com/comment/ClanAnnouncement/render/103582791433224455/1449457773990927103/?start=' +str(i)
    r = requests.get(url)
    data = r.json()
    soup = bs(data['comments_html'],'html.parser',from_encoding = 'big5')
    
    words = set(nltk.corpus.words.words())
    english_words = []
    d = enchant.Dict('en_US')
    try:
        for div in soup.find_all('div',{'class':"commentthread_comment_content"}):
            string = str(div.find('div',{'class':'commentthread_comment_text'}).get_text().strip())
            
            for word in string.split():
                if d.check(word):
                    english_words.append(word)
                
                comment_list = ' '.join(english_words)
        print(comment_list)
    except UnicodeEncodeError:
        pass

testimonial = textblob(comment_list)

print('Result')
print(testimonial.sentiment)
print('Polarity of all comments:' + str(testimonial.sentiment.polarity))
