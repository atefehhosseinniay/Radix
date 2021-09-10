import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import re
# from nltk.corpus import stopwords

nlp = spacy.load('en_core_web_lg')

from utils.preprocessing.utils import search_keyword



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


# from pyreparser import ResumeParser
# def extract_skills(file_pdf):
#     data = ResumeParser(file_pdf).get_extracted_data()

#     return data['skills']

# def extract_experience(file_pdf):
#     data = ResumeParser(file_pdf).get_extracted_data()

#     return data['experience'][0]



EDUCATION = [
            'BE','B.E.', 'B.E', 'BS', 'B.S',
            'ME', 'M.E', 'M.E.', 'MS', 'M.S',
            'BTECH', 'B.TECH', 'M.TECH', 'MTECH',
            'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
        ]

def extract_education(education_text):
    nlp_text = nlp(education_text)

    # Sentence Tokenizer
    # nlp_text = [sent.string.strip() for sent in nlp_text.sents]

    edu = {}
    # Extract education degree
    for index, txt in enumerate(nlp_text):
        for tex in txt:
            # Replace all special symbols
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex.upper() in EDUCATION and tex not in STOP_WORDS:
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