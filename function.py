from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage

file=r'C:\Users\atefe\Downloads\curriculum_vitae_data-master\curriculum_vitae_data-master\pdf\1.pdf'


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

   for token in doc.ents:
       if token.label_ == 'LOC':
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
        print("Person names:",person_names)
    else:
        print("Couldn't find a Person name.")
