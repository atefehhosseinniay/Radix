from utils.preprocessing.read_pdf import PDFExtractor

if __name__ == '__main__':
  pdfs = PDFExtractor(dir = './data/pdf/', max_iter = None)
  i = 0
  # Iter trough every pdf of the directory
  for pdf in pdfs:
    i += 1
    # pdf contains the extracted text from the pdf file
    # print(pdf)
    # Preprocess every pdf here (preporcessing not done yet)
    # print('-'*50)
  print(i)

  # Get pdf with file name, here gets ./data/pdf/3000.pdf
  print(len(pdfs.get_pdf_by_name('3000.pdf')))

  # Print the list of files from the directory ./data/pdf/
  print(pdfs.get_pdf_list())

  # Get the pdf by id from the pdf file list
  print(len(pdfs.get_pdf_by_id(54)))