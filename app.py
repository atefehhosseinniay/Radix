import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from utils.preprocessing.read_pdf import PDFExtractor
from utils.preprocessing.preprocessing import preprocess

if __name__ == '__main__':
  pdfs = PDFExtractor(dir = './data/pdf/', max_iter = None)
  
  # Iter trough every pdf of the directory
  saved = []
  for pdf in pdfs:
    # pdf contains the extracted text from the pdf file
    # Preprocess every pdf here (ans save result)
    data = preprocess(pdf.text)
    data['pdf'] = pdf.name
    
    saved.append(data)
  df = pd.DataFrame(saved)
  df.to_csv('pdf_data.csv')
# pdf = pdfs.get_pdf_by_name('1003.pdf')
# print(pdf.name, preprocess(pdf.text))

# pdf = pdfs.get_pdf_by_name('1006.pdf')
# print(pdf.name, preprocess(pdf.text))


corpus = pd.read_csv('pdf_data.csv')

def find_similarity(corpus: list, input_doc: str):
  '''
    Check similarity between corpus (list of files) and input_doc
  '''
  vect = TfidfVectorizer(min_df=1, stop_words="english")
  tfidf = vect.fit_transform(corpus)
  pairwise_similarity2 = tfidf * tfidf.T #product to create a square matrix

  arr = pairwise_similarity2.toarray()
  np.fill_diagonal(arr, np.nan) #we need that to eclude the 1 value from the nanargmax
  print (arr)

  input_idx = corpus.index(input_doc)
  result_idx = np.nanargmax(arr[input_idx])