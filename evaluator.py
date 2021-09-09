from pyresparser import ResumeParser
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

directory = '/home/vincent/PycharmProjects/pyreparser/Radix/data/pdf/'
'''
Let's try with a bunch of 5 pdfs
'''

file_1 = '1.pdf'
file_2 = '2.pdf'
file_3 = '3.pdf'
file_4 = '4.pdf'
file_5 = '5.pdf'

#pyreparser creat dictionaries, I need string here for test
# but it's not smart because we need this dictionaries to get the sections as 'skills'
data_1 = str(ResumeParser(directory+file_1).get_extracted_data())
data_2 = str(ResumeParser(directory+file_2).get_extracted_data())
data_3 = str(ResumeParser(directory+file_3).get_extracted_data())
data_4 = str(ResumeParser(directory+file_4).get_extracted_data())
data_5 = str(ResumeParser(directory+file_5).get_extracted_data())

corpus = [data_1, data_2, data_3, data_4, data_5]

'''
Let's do the magic of vectorisation here 
'''
cv = CountVectorizer(strip_accents= 'unicode', lowercase= True, stop_words='english')
count_matrix = cv.fit_transform(corpus)

vect = TfidfVectorizer(min_df=1, stop_words="english") #yeah stop words again
tfidf = vect.fit_transform(corpus)
pairwise_similarity2 = tfidf * tfidf.T #product to create a square matrix
print ("pairwise simi 2 is ")

arr = pairwise_similarity2.toarray()
np.fill_diagonal(arr, np.nan) #we need that to eclude the 1 value from the nanargmax
print (arr)
input_doc = data_4 #could be an user input...should be !

input_idx = corpus.index(input_doc)
result_idx = np.nanargmax(arr[input_idx])
print ('this doc: ', input_doc)
print ('is similar to', corpus[result_idx])
print('input is ', input_idx+1) #+1 to make te result more instinctive
print ('is simliar to ', result_idx+1) #the answer the client want

