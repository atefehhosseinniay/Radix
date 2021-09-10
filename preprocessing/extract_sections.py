import csv
import re
from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

from pdf_to_text import pdffile_totext
from key_words import search_keyword
file=r'C:\Users\atefe\Downloads\curriculum_vitae_data-master\curriculum_vitae_data-master\pdf\2.pdf'
text1,pdf_to_text_list = pdffile_totext(file)

#print(pdf_to_text_list)




def work_section(pdf_to_text_list):
    work_segment=[]
    other_keywords = ['Personal Information','Summary','DECLARATION','personal profile','objective','strength','PERSONAL DETAILS ','hobbies','PERSONAL PARTICULARS']


    education_keywords= ['education','school','qualification','qualifications','high school','university','academic background','college']
    education_degree=['associate','bachelor',"bachelor's",'masters','master',"master's",'doctoral']

    project_keywords=['academic projects','personal projects','other projects','professional projects','projects']
    skill_keywords = ['credentials','areas of experience','areas of expertise','areas of knowledge','skills','career related skills','professional skills','specialized skills','technical skills','computer skills','computer knowledge','technical experience','programming languages','languages','language competencies and skills','proficiencies','technical proficiency']
    work_experience_keywords=['career highlight','employment history','experience','employment',' work history','work experience',
                              'professional experience','professional background','industry experience']

    for i, text in enumerate(pdf_to_text_list):
        flag = False
        if search_keyword(text, work_experience_keywords):
            work_segment.append(text)
            i += 1
            flag = True
            while True:
                text = pdf_to_text_list[i]
                if not search_keyword(text, education_keywords) and not search_keyword(text,education_degree) and not search_keyword(
                    text, project_keywords) and not search_keyword(text, skill_keywords) and not search_keyword(text, other_keywords):


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
def education_section(pdf_to_text_list):
    education_segment=[]
    other_keywords = ['Summary', 'DECLARATION', 'personal profile', 'objective', 'strength', 'PERSONAL DETAILS ',
                      'hobbies', 'PERSONAL PARTICULARS']

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
                            text, other_keywords):

                            education_segment.append(text)
                        else:
                            break
                        i += 1
                        if i==len(pdf_to_text_list)-1:
                            break
                if flag:
                    break
    return education_segment

educ_sec=education_section(pdf_to_text_list)
#print('education:',educ_sec)

def skill_section(pdf_to_text_list):
    skill_segment=[]
    other_keywords = ['Summary', 'DECLARATION', 'personal profile', 'objective', 'strength', 'PERSONAL DETAILS ',
                      'hobbies', 'PERSONAL PARTICULARS']

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
    for i, text in enumerate(pdf_to_text_list):
        flag = False
        if search_keyword(text, skill_keywords):
            skill_segment.append(text)
            i += 1
            flag = True
            while True and i < len(pdf_to_text_list):
                text = pdf_to_text_list[i]
                if not search_keyword(text, education_keywords) and not search_keyword(text,education_degree) and not search_keyword(
                    text, project_keywords) and not search_keyword(text, work_experience_keywords) and not search_keyword(text, other_keywords):
                    skill_segment.append(text)
                else:
                    break
                i += 1
                if i==len(pdf_to_text_list)-1:
                    break

        if flag:
            break
    return skill_segment

skill_sec=skill_section(pdf_to_text_list)
print('skills_section',skill_sec)

def hobbies_section(pdf_to_text_list):
    hobbies_segment=[]
    hobby_keywords=['hobbies',"hobby's",'hobby']
    other_keywords = ['Summary', 'DECLARATION', 'personal profile', 'objective', 'strength', 'PERSONAL DETAILS ',
                      'hobbies', 'PERSONAL PARTICULARS']

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
    for i, text in enumerate(pdf_to_text_list):
        flag = False
        if search_keyword(text, hobby_keywords):
            hobbies_segment.append(text)
            i += 1
            flag = True
            while True and i < len(pdf_to_text_list):
                text = pdf_to_text_list[i]
                if not search_keyword(text, education_keywords) and not search_keyword(text,education_degree) and not search_keyword(
                    text, project_keywords) and not search_keyword(text, work_experience_keywords):
                    hobbies_segment.append(text)
                else:
                    break
                i += 1
                if i==len(pdf_to_text_list)-1:
                    break


        if flag:
            break
    return hobbies_segment

hobbies_segment=hobbies_section(pdf_to_text_list)
print('hobbies_segment:',hobbies_segment)

def cleaned_segment(lis):
    lis=lis[1:]
    lis.replace('\uf0d8','')
    l = ''.join(lis)
    return l
hob=cleaned_segment(hobbies_segment)
print(hob)

hobby=''.join(hobbies_segment)
print(hobby)
