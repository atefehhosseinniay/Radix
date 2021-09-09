
"""
Test pyreparser package

 ! Warning !

 if having OS error E053 or packages compatibility,
 please consider :
pip install nltk
pip install spacy==2.3.5
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
pip install pyresparser

"""
import os
from pyresparser import ResumeParser
import pandas as pd
import en_core_web_sm
nlp = en_core_web_sm.load()

list = []

directory = '/home/vincent/PycharmProjects/NLP/Radix/data/pdf/'
file = '1.pdf'
data = ResumeParser(directory+file).get_extracted_data()
list = data['skills']

print (list)


"""to get all the skills of all pdf in a list"""
# for file in os.listdir(directory):
#     data=ResumeParser(directory+file).get_extracted_data()
#     list=list+data['skills']

"""to put list of skills in a DataFrame"""

# df = pd.DataFrame(list, columns=['skills'])
# print(df)



