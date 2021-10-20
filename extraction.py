import csv
import re
from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

from pdf_to_text import pdffile_totext
#from key_words import search_keyword

def search_keyword(text, keyword_list):
    for word in keyword_list:
        word = str(word)
        if word.title() in text or word.upper() in text or word.capitalize() in text:
            return True
    return False

file=r'C:\Users\atefe\Downloads\curriculum_vitae_data-master\curriculum_vitae_data-master\pdf\2.pdf'
text_pdf,pdf_to_text_list = pdffile_totext(file)

print(text_pdf)

hobby_keywords=['hobbies',"hobby's",'hobby']
other_keywords = ['Summary', 'DECLARATION', 'personal profile', 'objective', 'strength', 'PERSONAL DETAILS ',
                       'PERSONAL PARTICULARS','ABOUT ME']

education_keywords = ['education', 'school', 'qualification', 'qualifications', 'high school', 'university',
                      'academic background', 'college']
education_degree = ['associate', 'bachelor', "bachelor's", 'masters', 'master', "master's", 'doctoral']

project_keywords = ['academic projects', 'personal projects', 'other projects', 'professional projects', 'projects']
skill_keywords = ['credentials', 'areas of experience', 'areas of expertise', 'areas of knowledge', 'skills',
                  'career related skills', 'professional skills', 'specialized skills', 'technical skills',
                  'computer skills', 'computer knowledge', 'technical experience', 'programming languages',
                  'languages', 'language competencies and skills', 'proficiencies', 'technical proficiency']
work_experience_keywords = ['career highlight', 'employment history', 'experience', 'employment', ' work history',
                            'work experience',
                            'professional experience', 'professional background', 'industry experience']

info=['curriculum vitae','curriculam vitae','cirriculam vitae','RESUME']
def work_section(pdf_to_text_list):
    work_segment=[]

    for i, text in enumerate(pdf_to_text_list):
        flag = False
        if search_keyword(text, work_experience_keywords):
            work_segment.append(text)
            i += 1
            flag = True
            while True:
                text = pdf_to_text_list[i]
                if not search_keyword(text, education_keywords) and not search_keyword(text,education_degree) and not search_keyword(
                    text, project_keywords) and not search_keyword(text, skill_keywords) and not search_keyword(text, other_keywords) and not search_keyword(text, hobby_keywords):


                    work_segment.append(text)
                else:
                    break
                i += 1
                if i==len(pdf_to_text_list)-1:
                    break


        if flag:
            break
    return work_segment

#work=work_section(pdf_to_text_list)
#print('work',work)

'''def work_extraction(work_sec):
    work_section_text = ''
    if work == []:
        print('No information')
    if len(work) > 1:
        work_section_text = str("".join(work[1:]))'''




def education_section(pdf_to_text_list):
    education_segment=[]

    for i, text in enumerate(pdf_to_text_list):
                flag = False
                if search_keyword(text, education_keywords):
                    education_segment.append(text)
                    i += 1
                    flag = True
                    while True and i < len(pdf_to_text_list):

                        text = pdf_to_text_list[i]
                        if not search_keyword(text, work_experience_keywords) and not search_keyword(
                            text, project_keywords) and not search_keyword(text, skill_keywords) and not search_keyword(
                            text, other_keywords) and not search_keyword(text, hobby_keywords):

                            education_segment.append(text)
                        else:
                            break
                        i += 1
                        if i==len(pdf_to_text_list)-1:
                            break
                if flag:
                    break
    return education_segment

#educ_sec=(education_section(pdf_to_text_list))
#print('education:',educ_sec)

'''def edducation_extraction(education_sec_list):
    education_sec_text=''.join(education_sec_list)
    for word in education_keywords:
        if word.title() or word.upper() or word.capitalize() in education_sec_text:
            education_sec_text=education_sec_text.replce(word.upper(),'')
            education_sec_text = education_sec_text.replce(word.capitalize(), '')
            education_sec_text = education_sec_text.replce(word.title(), '')'''




def skill_section(pdf_to_text_list):
    skill_segment=[]

    for i, text in enumerate(pdf_to_text_list):
        flag = False
        if search_keyword(text, skill_keywords):
            skill_segment.append(text)
            i += 1
            flag = True
            while True and i < len(pdf_to_text_list):
                text = pdf_to_text_list[i]
                if not search_keyword(text, education_keywords) and not search_keyword(text,education_degree) and not search_keyword(
                    text, project_keywords) and not search_keyword(text, work_experience_keywords) and not search_keyword(text, other_keywords) and not search_keyword(text, hobby_keywords):
                    skill_segment.append(text)
                else:
                    break
                i += 1
                if i==len(pdf_to_text_list)-1:
                    break

        if flag:
            break
    return skill_segment

#skill_sec=skill_section(pdf_to_text_list)
#print('skills_section',skill_sec)

def hobbies_section(pdf_to_text_list):
    hobbies_segment=[]


    for i, text in enumerate(pdf_to_text_list):
        flag = False
        if search_keyword(text, hobby_keywords):
            hobbies_segment.append(text)
            i += 1
            flag = True
            while True and i < len(pdf_to_text_list):
                text = pdf_to_text_list[i]
                if not search_keyword(text, education_keywords) and not search_keyword(text,education_degree) and not search_keyword(
                    text, project_keywords) and not search_keyword(text, work_experience_keywords) and not search_keyword(text, skill_keywords) and not search_keyword(text, other_keywords):
                    hobbies_segment.append(text)
                else:
                    break
                i += 1
                if i==len(pdf_to_text_list)-1:
                    break


        if flag:
            break
    return hobbies_segment

#hobby=hobbies_section(pdf_to_text_list)
#print('hobby:', hobby)

def other_section(pdf_to_text_list):
    other_segment = []

    for i, text in enumerate(pdf_to_text_list):
        flag = False
        if search_keyword(text, other_keywords):
            other_segment.append(text)
            i += 1
            flag = True
            while True and i < len(pdf_to_text_list):
                text = pdf_to_text_list[i]
                if not search_keyword(text, education_keywords) and not search_keyword(text,
                                                                                       education_degree) and not search_keyword(
                        text, project_keywords) and not search_keyword(text,
                                                                       work_experience_keywords) and not search_keyword(
                    text, skill_keywords) and not search_keyword(text, hobby_keywords):
                    other_segment.append(text)
                else:
                    break
                i += 1
                if i == len(pdf_to_text_list) - 1:
                    break

        if flag:
            break
    return other_segment

#other=other_section(pdf_to_text_list)

#print('other:',other)


def personal_information_section(pdf_to_text_list):
    personal_information_segment = []
    for i, text in enumerate(pdf_to_text_list):


         while i < len(pdf_to_text_list):
            text = pdf_to_text_list[i]
            if not search_keyword(text, education_keywords) and not search_keyword(text,
                                                                                   education_degree) and not search_keyword(
                    text, project_keywords) and not search_keyword(text,
                                                                   work_experience_keywords) and not search_keyword(
                text, skill_keywords) and not search_keyword(text, hobby_keywords) and not search_keyword(text, other_keywords):
                personal_information_segment.append(text)
            else:
                break
            i += 1
            if i == len(pdf_to_text_list) - 1:
                break


    return personal_information_segment


#personal_info=personal_information_section(pdf_to_text_list)
#print('personal_info:',personal_info)

def cleaned_segment(list_text,keys):
    text=str(list_text[0])
    for word in keys:
        word = str(word)
        if word.title() in text or word.upper() in text or word.capitalize() in text:
            text = text.replace(word.title(), '')
            text = text.replace(word.upper(), '')
            text = text.replace(word.capitalize(), '')
            list_text[0] = text
    return list_text
def list_to_text(list_text):
    ch=['\uf07d','\uf0d8','\u2019']
    text='\n'.join([i for i in list_text[1:]])
    for x in ch:
        if x in text:
            text=text.replace(x,'')

    return text

def final_function(file):
    text_pdf, pdf_to_text_list = pdffile_totext(file)
    all_text=[]

    work = work_section(pdf_to_text_list)
    cleaned_work=cleaned_segment(work, work_experience_keywords)
    work_text=list_to_text(cleaned_work)

    educ_sec = education_section(pdf_to_text_list)
    cleaned_educ_sec=cleaned_segment(educ_sec, education_keywords)
    education_text = list_to_text( cleaned_educ_sec)

    skill_sec = skill_section(pdf_to_text_list)
    cleaned_skill_sec = cleaned_segment(skill_sec, skill_keywords)
    skill_text = list_to_text(cleaned_skill_sec)

    hobby = hobbies_section(pdf_to_text_list)
    cleaned_hobby = cleaned_segment(hobby, hobby_keywords)
    hobby_text = list_to_text(cleaned_hobby)

    other = other_section(pdf_to_text_list)
    cleaned_other  = cleaned_segment( other , other_keywords)
    other_text = list_to_text(cleaned_other)

    personal_info = personal_information_section(pdf_to_text_list)
    cleaned_personal_info = cleaned_segment(personal_info, info)
    personal_info_text = list_to_text(cleaned_personal_info)
    '''all_text.append(cleaned_personal_info)
    all_text.append(cleaned_work)
    all_text.append(cleaned_educ_sec)
    all_text.append(cleaned_skill_sec)
    all_text.append(cleaned_hobby)'''


    return personal_info_text, other_text,hobby_text,skill_text, education_text,work_text

personal_info_text, other_text,hobby_text,skill_text, education_text,work_text=final_function(file)
print(education_text)



#create pdf

'''text_pdf_1=''
text_pdf_1+=personal_info_text
text_pdf_1+=work_text
text_pdf_1+=education_text
text_pdf_1+=skill_text
text_pdf_1+=hobby_text
text_pdf_1=str(text_pdf_1)
print(text_pdf_1)
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size=12)
# create a cell
for x in text_pdf_1:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
pdf.output("mypdf.pdf")'''
'''pdf.cell(200, 10, txt=personal_info_text,
         ln=1, align='C')
# add another cell
pdf.cell(200, 10, txt=education_text,
         ln=2, align='C')
pdf.cell(200, 10, txt=education_text,
         ln=3, align='C')
pdf.cell(200, 10, txt=skill_text,
         ln=4, align='C')
pdf.cell(200, 10, txt=hobby_text,
         ln=5, align='C')''
# save the pdf with name .pdf
pdf.output("pdf1_clean.pdf")'''


import joblib
from flair.models import SequenceTagger
from flair.data import Sentence
def name_extraction(text_pd):
    s = Sentence(text_pdf)
    model = SequenceTagger.load('ner-large')
    #joblib.dump(model,"ner-large_m.pkl")
    model = joblib.load("ner-large_m.pkl")
    model.predict(s)

    person_names = []
    for entity in s.get_spans('ner'):
        if entity.labels[0].value == "PER":
            person_names.append(entity.text)

    return person_names
n=name_extraction(personal_info_text)
print('name',n)
personal_info_text
def extract_email(text: str):
  email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", text)
  if email:
      try:
          return email[0].split()[0].strip(';')
      except IndexError:
          return None


mail=extract_email(personal_info_text)
print('mail:',mail)
from flair.data import Sentence
from flair.models import SequenceTagger
from segtok.segmenter import split_single

import json
import re

def extract_mobile_number(resume_text):

    phone = re.findall(re.compile(
        r'([+(]?\d+[)\-]?[ \t\r\f\v]*[(]?\d{2,}[()\-]?[ \t\r\f\v]*\d{2,}[()\-]?[ \t\r\f\v]*\d*[ \t\r\f\v]*\d*[ \t\r\f\v]*)'),
                       resume_text)
    print(phone)


    if phone:
        number = (''.join(phone[0])).replace(' ','')
        print(number)
        if len(number) > 10:
            return '+' + number
        if len(number) < 10:
            number1 = ''.join(phone[1]).replace(' ','')
            print(number1)

            if len(number1) > 10:
                return '+' + number1
            else:
                return number1

number=extract_mobile_number(personal_info_text)
print('phone',number)

from pyresparser import ResumeParser
def extract_skills(file_pdf):
    skills = []
    data = ResumeParser(file_pdf).get_extracted_data()
    skills .append(data['skills'])
    #skills = ' '.join(skills)

    return skills
skillsss=extract_skills(file)
print(skillsss)

def extract_experience(file_pdf):
    exp = []
    data = ResumeParser(file_pdf).get_extracted_data()
    exp .append(data['experience'][0])
    #skills = ' '.join(skills)

    return exp
exp=extract_skills(file)
print(exp)
import spacy

from nltk.corpus import stopwords

nlp = spacy.load('en_core_web_sm')

# Grad all general stop words
STOPWORDS = set(stopwords.words('english'))

EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S',
            'ME', 'M.E', 'M.E.', 'MS', 'M.S',
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH',
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
        ]

def extract_education(education_text):

    nlp_text = nlp(education_text)

    # Sentence Tokenizer
    nlp_text = [sent.string.strip() for sent in nlp_text.sents]

    edu = {}
    # Extract education degree
    for index, txt in enumerate(nlp_text):
        for tex in txt.split():
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex.upper() in EDUCATION and tex not in STOPWORDS:
                edu[tex] = txt + nlp_text[index + 1]

    # Extract year
    education = []
    for key in edu.keys():
        year = re.search(re.compile(r'(((20|19)(\d{2})))'), edu[key])
        if year:
            education.append((key, ''.join(year[0])))
        else:
            education.append(key)
    return education

education=extract_education(education_text)
print('educations',education)


def creat_dict(file):
    list_col=['name','Phone_number','email','Education','skills','hobby','experience']
    personal_info_text, other_text, hobby_text, skill_text, education_text, work_text = final_function(file)
    text_pdf, pdf_to_text_list = pdffile_totext(file)

    result={}
    result['name']=name_extraction(text_pdf)
    result['Phone_number']=extract_mobile_number(personal_info_text)
    result['email']=extract_email(personal_info_text)
    result['skills']=extract_skills(file)
    result['hobby'] = hobby_text
    result['experience'] = extract_experience(file)
    result['Education'] = extract_education(education_text)

    return result

result=creat_dict(file)
print('result',result)
