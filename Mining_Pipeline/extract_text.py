import pandas as pd
import numpy as np
import xml.etree.cElementTree as et
import spacy
import re
from nltk import tokenize

# Parse the xml by paragraph and sentence
def extract_paragraphs_new(path):
    tree=et.parse(path)
    root=tree.getroot()
    del_list = []
    full = ''
    goid = ''
    for text in root.iter('Text'):
        full = text.text
    for i in range(len(full)):
        if full[i:i+3] == '<p>':
            del_list.append(i)
    for item in root.iter('GOID'):
        goid = item.text
    temp = {'GOID': [], 'Paragraph': [], 'Sentence': [], 'Overall Sentence': [], 'Text': []}
    sentence_count = 1
    #temp = {'Paragraph': [], 'Text': []}
    for i in range(len(del_list)-1):
        text = full[(del_list[i]+3):(del_list[i+1])]
        text = text.replace("\n","")
        text = text.replace("<p>","")
        text = text.replace("</p>","")
        text = text.replace("<i>","")
        text = text.replace("</i>","")
        text = text.replace("<b>","")
        text = text.replace("</b>","")
        all_sen = tokenize.sent_tokenize(text)
        for j in range(len(all_sen)):
            temp['GOID'].append(goid)
            temp['Paragraph'].append(i+1)
            temp['Sentence'].append(j+1)
            temp['Overall Sentence'].append(sentence_count)
            temp['Text'].append(all_sen[j])
            sentence_count += 1
    df = pd.DataFrame(data=temp)
    return df

# for sentiment analysis
from spacytextblob.spacytextblob import SpacyTextBlob
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

def get_tags(sentence):
    """Return POS tags of each sentence."""
    res = []
    for token in nlp(sentence):
        res.append((token.text, token.pos_, token.dep_))
    return res

def get_polarity(sentence):
    """Return polarity score of each sentence."""
    token = nlp(sentence)
    polarity = token._.blob.polarity
    return polarity

def get_subjectivity(sentence):
    """Return subjectivity score of each sentence."""
    token = nlp(sentence)
    subjectivity = token._.blob.subjectivity
    return subjectivity

xml_info = pd.read_csv('server_path_sample.csv')
all_path = xml_info['Path'].tolist()

def keyword_search(all_path, keyword):
    temp = pd.DataFrame()
    for i in range(len(all_path)):
        extracts = extract_paragraphs_new(all_path[i])
        extracts['Polarity'] = extracts['Text'].apply(get_polarity)
        extracts['Subjectivity'] = extracts['Text'].apply(get_subjectivity)
        temp = temp.append(extracts)
    result = temp[temp['Text'].astype(str).str.contains(keyword)]
    return result        

keyword_econ = keyword_search(all_path, 'economics')
keyword_econ.to_csv('keyword_econ.csv', index=False)

def get_number(all_path):
    temp = {'GOID': [], 'Paragraph Number': [], 'Sentence Number': []}
    for i in range(len(all_path)):
        extracts = extract_paragraphs_new(all_path[i])
        temp['GOID'].append(extracts['GOID'].max())
        temp['Paragraph Number'].append(extracts['Paragraph'].max())
        temp['Sentence Number'].append(extracts['Overall Sentence'].max())
    df = pd.DataFrame(data=temp)   
    return df

text_info = get_number(all_path)
text_info.to_csv('text_info.csv', index=False)
