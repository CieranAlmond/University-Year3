import urllib.request
import nltk
from nltk import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from termcolor import colored
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import json



class Ass1:
    '''
    This class is resposible for housing all functions related to the assignment
    '''
    def __init__(self):
        self.stemmer = SnowballStemmer("english")                               #Stemmer object
        self.stop_words = set(stopwords.words("english"))                       #Stop words list from nltk
        self.punctuation = "–!\"#$%&()*+-.,/:;<=>?@[\]^_`{|}~\n"                #Custom list of punctuation
        with open("term.json", "w") as json_file:
            data = {}
            data['terms'] = {}
            json.dump(data, json_file)
            json_file.close()
        
    '''
    This function is resposible for grabbing the html from the url and returning
    it as a urlib object
    
    @param url - the url address for the desired website
    @return html - urllib object containing html code
    '''
    def grab_html(self, url):
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()

        html = mybytes.decode("utf8")
        fp.close()

        return html
    '''
    This function applies a nltk.Snowball stemmer to the words

    @param text_list - list of all the words in the text
    @return text_list - list of all stemmed words
    '''
    def stem_words(self, text_list):
        for word in text_list:
            text_list[text_list.index(word)] = self.stemmer.stem(word)
        return text_list
    
    '''
    This function removes all stopwords from the text that are in the nltk.stopwords object
    @param text_list - list of all words in text
    @return relevant_words - all the words that are not stopwords in the text
    '''
    def remove_stopwords(self, text_list):
        relevant_words = []                                     #List to contain all words in the page
        for word in text_list:
            if word not in self.stop_words and word != "":      #Checking if word is a stop word or space
                relevant_words.append(word)
        return relevant_words

    '''
    Function to remove punction from a string
    
    @param text - a string containing punctuation
    @return text - a string without punctuation
    '''
    def remove_punctuation(self, text):
        for word in text:
            if word in self.punctuation:
                text = text.replace(word, " ")
        return text



    '''
       This function removes single characters from the text and stores them in a new text list
       @param text_list - list of all words in text
       @return text_list - all the words minus single characters
       '''
    def remove_single_words(self, text_list):
        for word in text_list:
            if len(word) > 1:
                text_list[text_list.index(word)] = text_list + " " + word
        return text_list



        
        

'''
Function to write each stage to a file

@param file_name - name of the file to be created
@param text - the string content to be written to a file
'''
def writer(file_name, text):
    f = open(file_name, "w")
    if (isinstance(text, list)):                    #Checking for lists so they can be printed over multiple lines
        for i in text:
            f.write("%s\n" % str(i))
    else: 
        f.write(text)
    f.close()


def main():
    vocab_list = []                                             #list of strings that are in the documents
    ass1 = Ass1()
    url_f = open('url.txt', 'r')                                #list of urls to be checked
    for url in url_f:
        try:
            soup = BeautifulSoup(ass1.grab_html(url), "lxml")

            writer("html.txt", str(soup))
            
            #removing js under the script tag from html
            for tag in soup(["script"]): 
                tag.extract()
                
            #removing css under the style tag from html
            for tag in soup(["style"]): 
                 tag.extract()
                
            text = soup.get_text()                           #remove all other html tags, leaving raw text
            writer("text.txt", text)

            sentence = sent_tokenize(text)                   #splitting the sentences
            writer("sentences.txt", sentence)
        
            text = ass1.remove_punctuation(text)             #removing punctuation
            writer("removed_punct.txt", text)

            text = text.lower()
            text_list = text.split(" ")
            text_list = ass1.remove_stopwords(text_list)    #removing stopwords
            text = " " 
            text = text.join(text_list)
            writer("removed_stopwords.txt", text)
            
            vocab_list.append(text)
            
            text_list = ass1.stem_words(text_list)          #stemming words
            text = " " 
            text = text.join(text_list)
            writer("stemmed.txt", text)
            
            
            tokens = nltk.word_tokenize(text)               #seperating text to part of speech
            tokens = nltk.pos_tag(tokens)                   #displaying words with part of speech tags
            writer("part_of_speech.txt", tokens)
            
        #handling http errors
        except(urllib.error.HTTPError):
            print(url[0:-1] + colored(" http error", "red"))
        except(UnicodeDecodeError):
            print(url[0:-1] + colored(" utf-8 error","green"))

    '''Performing tfidf on the list of document vocabularies'''
    #TF-IDF
    tfv = TfidfVectorizer(use_idf=True)
    tfidf_vector = tfv.fit_transform(vocab_list)
    #convert to pandas dataframe for formatting
    tfidf_vector = pd.DataFrame(tfidf_vector.T.todense(), index=tfv.get_feature_names(), columns=['url1', 'url2'])
    print(tfidf_vector)
    writer("tfidf.txt", tfidf_vector.to_string(header = True, index=True))

main()
