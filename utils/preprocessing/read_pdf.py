import os
from pdfminer.high_level import extract_text
from pdfminer.pdfparser import PDFSyntaxError, PSEOF
from typing import Union, List

class PDF:
  """
    Container class to have pdf name and text in same object
  """
  def __init__(self, name: str, text: str):
    self.name = name
    self.text = text

class PDFExtractor:
  """
    Class handeling pdfs, getting pdf list in folder & iter through them
  """
  def __init__(self, dir: str, max_iter: Union[int, None] = None):
    self.path: str = dir
    self.files = os.listdir(dir)
    if len(self.files) == 0:
      raise Exception("No files in directory")

    # iterator values
    self.i = 0
    self.current = 0
    self.max_files = len(self.files)
    self.max_iter = max_iter if type(max_iter) == int else self.max_files
  
  def __iter__(self):
    return self
  
  def __next__(self) -> PDF:
    text = ''
    while text == '':
      if self.i < self.max_files and self.current < self.max_iter:
        text = self._get_text_(self.path + self.files[self.i])
        self.i += 1
        if text != '':
          self.current += 1
          return text
      else:
        raise StopIteration

  def get_pdf_list(self) -> List[str]:
    '''
    Get list of pdf files as read in the given directory
    :return: list of pdf files
    '''
    return self.files
  
  def get_pdf_by_id(self, id: int) -> str:
    '''
    Get pdf text by id
    :param id: ID of the file in filelist. File list is generated by collecting all the files in gived directory
    :return: extracted text from the pdf
    '''
    if id > len(self.files):
      raise IndexError("index out of range")
    return self._get_text_(self.path + self.files[id])

  def get_pdf_by_name(self, file_name: str) -> str:
    '''
    Get pdf text by file name
    :param file_name: name of the pdf file you want to get text
    :return: extracted text from the pdf
    '''
    return self._get_text_(self.path + file_name)
  
  @staticmethod
  def _get_text_(path: str) -> PDF:
    try:
      name = path.split('/')[-1]
      text = extract_text(path)
      return PDF(name, text)
    except PDFSyntaxError as e:
      print(f'{path}: {e}')
    except PSEOF as e:
      print(f'{path}: {e}')
    except:
      print(f'{path}: An unexpected error occured')
    return ''