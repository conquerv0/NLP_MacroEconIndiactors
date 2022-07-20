import pandas as pd
import numpy as np
import xml.etree.cElementTree as et
import spacy
import re
from nltk import tokenize

def extract_meta(path):
    tree=et.parse(path)
    root=tree.getroot()

    meta = {'Keyword': [], 
            'GOID': [], 
            'Title': [], 
            'Contributors': [],
            'Contributor FirstName': [],
            'Contributor LastName': [],
            'Numeric Date': [],
            'Start Date': [],
            'End Date': [],
            'Qualifier': [],
            'Publisher Country': [],
            'Language': [],
            'Source': [],
            'StartPage': [],
            'DocSection': [],
            'ColumnHeader': [],
            'DocEdition': [],
            'Title Keywords': [],
            'Terms': [],
            'Word Count': [],
            'Title of Newspaper': [],
            'Subjects': [],
            'MpubId': []
            }

    # iteratre over the trees to extract metadata
    for item in root.iter('GOID'):
        meta['GOID'].append(item.text)

    for item in root.iter('TitleAtt'):
        meta['Title'].append(item[0].text)

    for item in root.iter('PubFrosting'):
        for title in item.iter('Qualifier'):
            meta['Qualifier'].append(title.text)
            break

    for item in root.iter('ISO'):
        meta['Language'].append(item[1].text.strip())

    # Contributor Info
    for item in root.iter('Contributors'):
        for contributor in item:
            if not meta['Contributors']:
                meta['Contributors'].append(contributor[0][0].text)
            else:
                meta['Contributors'].append('^^'+contributor[0][0].text)

    for item in root.iter('LastName'):
        if not meta['Contributor LastName']:
            meta['Contributor LastName'].append(item.text)
        else:
            meta['Contributor LastName'].append('^^'+item.text)

    for item in root.iter('FirstName'):
        if not meta['Contributor FirstName']:
            meta['Contributor FirstName'].append(item.text)
        else:
            meta['Contributor FirstName'].append('^^'+item.text)

    for item in root.iter('NumericDate'):
        meta['Numeric Date'].append(item.text)

    for item in root.iter('SourceType'):
        meta['Source'].append(item.text)

    for item in root.iter('Country'):
        meta['Publisher Country'].append(item.text)
    
    # PrintLocation Info
    for item in root.iter('StartPage'):
        meta['StartPage'].append(item.text)

    for item in root.iter('DocSection'):
        meta['DocSection'].append(item.text)
    
    for item in root.iter('ColumnHeader'):
        meta['ColumnHeader'].append(item.text)
    
    for item in root.iter('DocEdition'):
        meta['DocEdition'].append(item.text)
    
    for title in root.iter('Terms'):
        terms = [title.tag, title.attrib, title.text.strip()]
        for item in title:
            item_info = [item.tag, item.attrib, item.text.strip()]
            for sub in item:
                item_info.append(sub.tag)
                item_info.append(sub.attrib)
                item_info.append(sub.text)
            terms.append(item_info)
        meta['Terms'].append(terms)

    # for title in root.iter('GenSubjTerm'):
    #     terms = [title.tag, title.attrib, title.text.strip()]
    #     for item in title:
    #         terms.append(item.tag)
    #         terms.append(item.attrib)
    #     meta['Subject Terms'].append(item.text)

    for item in root.iter('PubFrosting'):
        for title in item.iter('Title'):
            meta['Title of Newspaper'].append(item[2].text)
            break
    
    for item in root.iter('PubFrosting'):
        for title in root.iter('Subjects'):
            meta['Subjects'].append(title[0].text)

    for item in root.iter('TextInfo'):
        for title in item:
            meta['Word Count'].append(title.attrib['WordCount'])
    # df_meta = pd.DataFrame(data=meta)

    for item in root.iter('PubFrosting'):
        for title in root.iter('MpubId'):
            meta['MpubId'].append(title.text)

    for item in root.iter('PubFrosting'):
        for title in root.iter('StartDate'):
            meta['Start Date'].append(title.text)
            break

    for item in root.iter('PubFrosting'):
        for title in root.iter('EndDate'):
            meta['End Date'].append(title.text)
            break
            
    # add na if any header info is not found
    for k in meta:
        if not meta[k]:
            meta[k].append('n/a')
        if len(meta[k]) > 1:
            output = ",".join(meta[k])
            meta[k] = output
    return meta

xml_info = pd.read_csv('server_path_sample.csv')
all_path = xml_info['Path'].tolist()

meta_all = pd.DataFrame()
for path in all_path:
    meta = extract_meta(path)
    meta_df = pd.DataFrame(data=meta)
    meta_all = pd.concat([meta_all, meta_df])
meta_all = meta_all.reset_index(drop=True)

meta_all.to_csv('meta_all.csv', index=False)