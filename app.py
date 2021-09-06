from utils.preprocessing.read_pdf import PDFExtractor
from utils.preprocessing.preprocessing import preprocess

if __name__ == '__main__':
  pdfs = PDFExtractor(dir = './data/pdf/', max_iter = 3)
  
  # Iter trough every pdf of the directory
  for pdf in pdfs:
    # pdf contains the extracted text from the pdf file
    # print(pdf)
    # Preprocess every pdf here (preporcessing not done yet)
    preprocess(pdf)
    print('-'*50)
