from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage

file=r'C:\Users\atefe\Downloads\curriculum_vitae_data-master\curriculum_vitae_data-master\pdf\3.pdf'
#file=r'C:\Users\atefe\Desktop\HosseinNiayHassankiadeh-Atefeh-CV.pdf'

def pdffile_totext(path_to_pdf):

    #PDFResourceManager is used to store shared resources such as fonts or images that we might encounter in the files.

    resource_manager = PDFResourceManager(caching=True)


    #create a string object that will contain the final text the representation of the pdf.

    out_text = StringIO()


    #UTF-8 is one of the most commonly used encodings, and Python often defaults to using it.
    #In our case, we are going to specify in order to avoid some encoding errors.

    codec = 'utf-8'

    #LAParams is the object containing the Layout parameters with a certain default value.

    laParams = LAParams()

    text_converter = TextConverter(resource_manager, out_text, codec, laparams=laParams)
    fp = open(path_to_pdf, 'rb')

    interpreter = PDFPageInterpreter(resource_manager, text_converter)

    for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
        interpreter.process_page(page)

    text = out_text.getvalue()


    #Closing all the ressources we previously opened

    fp.close()
    text_converter.close()
    out_text.close()


    return text

str_text=pdffile_totext(file)
print(str_text)


import spacy
from spacy.matcher import Matcher

# load pre-trained model
nlp = spacy.load('en_core_web_sm')

# initialize matcher with a vocab
matcher = Matcher(nlp.vocab)

def extract_name(resume_text):
    name=[]
    name2=[]
    nlp_text = nlp(resume_text)

    # First name and Last name are always Proper Nouns
    #pattern1 = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN', "OP": "*"}, {'POS': 'PROPN'}]
    #pattern2 = [{'POS': 'PROPN'} , {'POS': 'PROPN'} ,  {'POS': 'PROPN',"OP":"?"} ]

    person_name = [ent.text for ent in nlp_text.ents if ent.label_ == 'PERSON']
    name2.append(person_name)


    matcher.add('NAME',[pattern])
    matches = matcher(nlp_text)

    #matcher2.add('NAME', [pattern2])
    #matches2 = matcher2(nlp_text)

    for match_id, start, end in matches:
         span1 = nlp_text[start:end]
         if span1.text.lower() != 'curriculum vitae' and span1.text.lower() != 'curriculam vitae' and span1.text.lower() != 'cirriculam vitae' and span1.text.lower() != 'RESUME':
             name.append(span1.text)


    if name[0] in name[2] :

        return name[2] , name2
    else:
        return name[0] , name2






names = extract_name(str_text)
print(names)

import re

def extract_phone_number(resume_text):
    PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
    #phone = re.findall(re.compile(
       # r'([+(]?\d+[)\-]?[ \t\r\f\v]*[(]?\d{2,}[()\-]?[ \t\r\f\v]*\d{2,}[()\-]?[ \t\r\f\v]*\d*[ \t\r\f\v]*\d*[ \t\r\f\v]*)'),
                      # resume_text)
    phone = re.findall(PHONE_REG, resume_text)

    if phone:
        number = ''.join(phone[0])

        if resume_text.find(number) >= 0 and len(number) < 16:
            return number
    return None

phone = extract_phone_number(str_text)
print(phone)


import re

def extract_email(text):
    email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", text)
    if email:
        try:
            return email[0].split()[0].strip(';')
        except IndexError:
            return None


email = extract_email(str_text)
print(email)

import requests

def skill_exists(skill):
    url = f'https://api.promptapi.com/skills?q={skill}&count=1'
    headers = {'apikey': 'YOUR API KEY'}
    response = requests.request('GET', url, headers=headers)
    result = response.json()

    if response.status_code == 200:
        return len(result) > 0 and result[0].lower() == skill.lower()
    raise Exception(result.get('message'))




import spacy
from spacy import displacy
from spacy.matcher import Matcher

def extract_address(text):

   nlp = spacy.load('en_core_web_lg')
   doc = nlp(text)
   address=[]

   for token in doc.ents:
       if token.text=='Address' and token.label_ == 'LOC':
           address.append(token)
   return token

ad=extract_address(str_text)
print(ad)

from flair.models import SequenceTagger
from flair.data import Sentence

s = Sentence(str_text)
model = SequenceTagger.load('ner-large')
model.predict(s)

person_names = []
for entity in s.get_spans('ner'):
    if entity.labels[0].value == "PER":
        person_names.append(entity.text)

    else:
        pass

#print("Person names:",person_names[0])


loc=[]
geo=[]

for entity in s.get_spans('ner'):
    if entity.labels[0].value == "LOC":
        loc.append(entity.text)
    if entity.labels[0].value == "GPE":
        geo.append(entity.text)
    else:
        pass

print("loc:",loc)
print("geo:",geo)


import spacy
nlp = spacy.load('en_core_web_sm')
text = str_text
doc = nlp(text)
for ent in doc.ents:
    if ent.label_ in ['GPE', 'LOC']:
        print (ent.text, ent.start_char, ent.end_char, ent.label_)



import re
from nltk.corpus import stopwords

# load pre-trained model
nlp = spacy.load('en_core_web_sm')

# Grad all general stop words
STOPWORDS = set(stopwords.words('english'))

# Education Degrees
EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S','C.A.','c.a.','B.Com','B. Com','M. Com', 'M.Com','M. Com .',
            'ME', 'M.E', 'M.E.', 'MS', 'M.S',
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH',
            'PHD', 'phd', 'ph.d', 'Ph.D.','MBA','mba','graduate', 'post-graduate','5 year integrated masters','masters',
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
        ]

def extract_education1(resume_text):
    nlp_text = nlp(resume_text)
    # Sentence Tokenizer
    nlp_text = [sent.text.strip() for sent in nlp_text.sents]
    edu = {}
    # Extract education degree
    for index, text in enumerate(nlp_text):
        #print(index, text), print('-'*50)
        for tex in text.split():
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            #print(tex)
            if tex.upper() in EDUCATION and tex not in STOPWORDS:
                edu[tex] = text + nlp_text[index + 1]
                return list(edu.keys())

print(extract_education1(text))


import re
import spacy
from nltk.corpus import stopwords

def extract_education(resume_text):
    nlp = spacy.load('en_core_web_lg')

    # Grad all general stop words
    STOPWORDS = set(stopwords.words('english'))

    # Education Degrees
    EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S','C.A.','c.a.','B.Com','B. Com','M. Com', 'M.Com','M. Com .',
            'ME', 'M.E', 'M.E.', 'MS', 'M.S',
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH',
            'PHD', 'phd', 'ph.d', 'Ph.D.','MBA','mba','graduate','GRADUATE', 'post-graduate','POST-GRADUATE','5 year integrated masters','5 YEAR INTEGRATED MASTERS','masters','MASTERS',
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII','bachelors','BACHELORS','p.h.d','b.e', 'b.e.', 'm.e.','engineering','ENGINEERING','certificate','CERTIFICATE','diploma','DIPLOMA'
        ]
    nlp_text = nlp(resume_text)

    # Sentence Tokenizer
    nlp_text = [sent.text.strip() for sent in nlp_text.sents]

    edu = {}
    # Extract education degree
    for index, text in enumerate(nlp_text):
        for tex in text.split():
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex.upper() in EDUCATION and tex not in STOPWORDS:
                edu[tex] = text + nlp_text[index + 1]

    # Extract year
    education = []
    for key in edu.keys():
        year = re.search(re.compile(r'(((20|19)(\d{2})))'), edu[key])
        if year:
            education.append((key, ''.join(year[0])))
        else:
            education.append(key)
    return education


educ=extract_education(text)
print(educ)

import nltk

#nltk.download('stopwords')
# nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('words')
#nltk.download('maxent_ne_chunker')


def extract_education2(str_text):
    """
    Function to get the education of person out of given text
    """
    education_words = [
        # 'school',
        # 'university',
        'certificate',
        # 'study',
        'diploma',
        # 'hsc',
        # 'ssc',
        # 'college',
        # 'higher',
        # 'institute',
        # 'studies',
        # 'education',
        # 'high',
        # 'master',
        # 'bachelor',
        # 'academy',
        # 'polytechnic',
        # 'degree',
        'masters',
        'bachelors',
        'p.h.d',
        'b.e',
        'b.e.',
        'm.e.'
        'engineering'
    ]
    tokens = nltk.word_tokenize(str_text)
    tokens_with_pos = nltk.pos_tag(tokens)
    edu_institutes = []
    for each, tag in tokens_with_pos:
        if each.lower() in education_words:
            edu_institutes.append(each)

    return edu_institutes

ed=extract_education1(text)
print(ed)


from fitz.utils import Shape
from numpy import concatenate
from tabulate import tabulate
import pandas as pd
import fitz
import nltk

import spacy
from spacy.lang.en import English
from spacy import displacy

from nltk.corpus import stopwords

import string

import re

def text_to_df( text : str) -> pd.DataFrame :
    """
    Function to generate a dataframe with words and types from given text
    """

    # Creating a doc by processing the given text with an nlp object
    doc = nlp(text)

    # create a 2 column empty dataframe
    df = pd.DataFrame(columns = ['token_text', 'token_label' ])

    # Populating the dataframe with the word and its type
    for ent in doc.ents:
        #print(ent.text, ent.label_)
        df.loc[df.shape[0]] = [ent.text, ent.label_]

    return df

df=text_to_df( text )
print(df)
