
import csv
import re
from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

from pdf_to_text import pdffile_totext

file=r'C:\Users\atefe\Downloads\curriculum_vitae_data-master\curriculum_vitae_data-master\pdf\1.pdf'
text1,pdf_to_text_list = pdffile_totext(file)

print(pdf_to_text_list)

def get_keywords(file):
    file1 = open(file, 'r')
    words= csv.reader(file1)
    keywords = []
    for row in words:
        keywords.append(row[0])
    return keywords

def qualification_word(file):
    file1 = open(file, 'r')
    reader = csv.reader(file1)
    qualification_word_dict = {}
    abbreviation_list = []
    degree_list = []
    for row in reader:

        abbreviation_list.append(row[0].lower())
        degree_list.append(row[1].lower())
        qualification_word_dict[row[0].lower()] = row[1].lower()
    return qualification_word_dict, abbreviation_list, degree_list

qualification_word_dict, abbreviation_list, degree_list = qualification_word('qualification_degree_list.csv')
#print(qualification_word_dict)
#print(abbreviation_list)
#print(degree_list)


def major_word(file):
    #file_name = "educational_major.csv"
    file1 = open(file, 'r')
    reader = csv.reader(file1)
    major_list = []
    for row in reader:
        major_list.append(row[0].lower())
    return major_list
#print(major_word("educational_major.csv"))


def university_word(file):
    #file_name = "university.csv"
    file1 = open(file, 'r')
    reader = csv.reader(file1)
    university_word_dict = {}
    for row in reader:
        value = [row[2].lower(), row[3].lower(), row[4].lower(), row[5].lower()]
        university_word_dict[row[1]] = value
    return university_word_dict
university_word_dict = university_word ("university.csv")
#print(university_word_dict)


def search_keyword(text, keyword_list):
    for word in keyword_list:
        word = str(word)
        if word.title() in text or word.upper() in text or word.capitalize() in text:
            return True
    return False

