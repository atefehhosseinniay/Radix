from pyresparser import ResumeParser

directory = '/home/vincent/PycharmProjects/pyreparser/Radix/data/pdf/'
file_1 = '1.pdf'
file_2= '2.pdf'

data_1 = str(ResumeParser(directory+file_1).get_extracted_data())
data_2 = str(ResumeParser(directory+file_2).get_extracted_data())


data_list = [data_1, data_2]

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(strip_accents= 'unicode', lowercase= True, stop_words='english')
count_matrix = cv.fit_transform(data_list)

from sklearn.metrics.pairwise import cosine_similarity
# get the match percentage
matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
matchPercentage = round(matchPercentage, 2) # round to two decimal
print( 'sklearn cosine similarity: '+str(file_1)+" matches about"+ str(matchPercentage)+ "% of the "+ str(file_2))


import difflib

similarity = difflib.SequenceMatcher(None, data_1, data_2).ratio()
similarity_perc = similarity *100
print( 'difflib seq matcher: '+str(file_1)+" matches about "+ str(similarity_perc)+ "% of the "+ str(file_2))

from scipy.spatial import distance

distance_ham= distance.hamming(data_1, data_2)
print ('Spicy spatial distance ham is: '+ str(distance_ham))

import textdistance
print ('TEXTDISTANCE lib:')
'''
Cosine similarity is a common way of comparing two strings. This algorithm treats strings as vectors,
and calculates the cosine between them. Similar to Jaccard Similarity, 
cosine similarity also disregards order in the strings being compared.

For example, here we compare the word “apple” with a rearranged anagram of itself. 
This gives us a perfect cosine similarity score.
'''

cosine = textdistance.cosine(data_1, data_2) # 1.0
print ('cosine similarity is '+ str(cosine*100))

'''
Levenshtein distance 
measures the minimum number of insertions, deletions, 
and substitutions required to change one string into another.
Is useful measure to use if you think that the differences between two strings 
are equally likely to occur at any point in the strings. 

It’s also more useful if you do not suspect full words in the strings are rearranged from each other 
(see Jaccard similarity or cosine similarity a little further down).
'''
leven_dis = textdistance.levenshtein(data_1, data_2)
print ('Levenshtein distance is: ' +str(leven_dis))


'''
Jaro-Winkler 
is another similarity measure between two strings. 
This algorithm penalizes differences in strings more earlier in the string. 
A motivational idea behind using this algorithm is that typos are generally more likely to occur later in the string, 
rather than at the beginning. 
When comparing “this test” vs. “test this”, even though the strings contain the exact same words 
(just in different order), the similarity score is just 2/3.
If it matters more that the beginning of two strings in your case are the same, then this could be a useful algorithm to try
'''
jaro = textdistance.jaro_winkler(data_1, data_2)
print ('Jaro distance is : ' + str(jaro))

'''
Jaccard similarity 
measures the shared characters between two strings, regardless of order. 
In the first example below, we see the first string, “this test”, has nine characters (including the space). 
The second string, “that test”, has an additional two characters that the first string does not (the “at” in “that”). 
This measure takes the number of shared characters (seven) divided by this total number of characters (9 + 2 = 11).
Thus, 7 / 11 = .636363636363…
'''

jaccard = textdistance.jaccard(data_1, data_2)
print ("Jaccard distance is " + str(jaccard))
