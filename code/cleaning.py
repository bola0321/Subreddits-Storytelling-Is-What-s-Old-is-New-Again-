#Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import re
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer


from sklearn.feature_extraction.text import TfidfVectorizer


def clean_data(file_str_list):
    concat_df = pd.DataFrame(columns=["post_id","title","selftext","subreddit","created_utc","is_osr"])
    
    for file in file_str_list:
        #read in file
        df = pd.read_csv(file)
        #remove rows that don't contain selftext
        df = df.dropna(subset="selftext")
        #rename column to post_id for clarity
        df = df.rename(columns={"Unnamed: 0": "post_id"})
        #drop comments
        df = df.drop(columns=["comments"])
        #assign new column to 0/1 if a row is from the osr subreddit or not
        df["is_osr"] = df["subreddit"].map({"rpg": 0, "osr": 1})

        #concatenate data 
        concat_df = pd.concat([concat_df, df])

    return concat_df




stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # default to noun

def preprocess_selftext(text):

    # 1. Lowercase
    text = text.lower()

    # 2. Tokenize
    tokens = nltk.word_tokenize(text)

    # 3. POS-tag the tokens
    tagged_tokens = nltk.pos_tag(tokens)

    # 4 & 5. Lemmatize and remove stopwords
    lemmatized_words = []
    for token, tag in tagged_tokens:
        wn_tag = get_wordnet_pos(tag)
        lemma = lemmatizer.lemmatize(token, pos=wn_tag)
        lemmatized_words.append(lemma)

    # 6. Return space-joined string
    return " ".join(lemmatized_words)

# tokenizer function to lowecase and remove urls
def custom_tokenizer(text):
    # Lowercase the text
    text = text.lower()
    # Remove URLs (http, https, www); adjust the pattern to your needs
    text = re.sub(r'http\S+|www\.\S+', '', text)
    
    # NLTK RegexpTokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    
    return tokens


def tfidf_list_and_barplot(ngram1, ngram2, X_train, X_test, y_train, y_test):
# instantiate TfidfVectorizer, use the custom tokenizer
    tvec = TfidfVectorizer(
        stop_words=stopwords.words("english"),  
        tokenizer=custom_tokenizer,            
        ngram_range=(ngram1,ngram2),
        min_df=10,
        max_features=65,
        token_pattern=None
    )
    
    # fit and transform
    X_train_cv = tvec.fit_transform(X_train)
    X_test_cv  = tvec.transform(X_test)
    
    # convert to dataframe to see the feature names and use for plotting
    X_train_df = pd.DataFrame(X_train_cv.toarray(), columns=tvec.get_feature_names_out())
    
    # Display top tokens
    top_tokens = X_train_df.sum().sort_values(ascending=False).head(25)
    print(top_tokens)
    
    # Plot top 15 words in combined dataframe
    top_tokens.head(15).plot(kind='barh');