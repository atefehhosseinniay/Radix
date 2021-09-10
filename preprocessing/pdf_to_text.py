import re
from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

file=r'C:\Users\atefe\Downloads\curriculum_vitae_data-master\curriculum_vitae_data-master\pdf\1.pdf'

def pdffile_totext( path_to_pdf ) :

    resource_manager = PDFResourceManager(caching=True)

    out_text = StringIO()

    codec = 'utf-8'

    laParams = LAParams()

    text_converter = TextConverter(resource_manager, out_text, codec, laparams=laParams)
    fp = open(path_to_pdf, 'rb')

    interpreter = PDFPageInterpreter(resource_manager, text_converter)

    for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
        interpreter.process_page(page)

    text = out_text.getvalue()
    text = re.sub(r'\n\s*\n', '\n', text)
    pdf_to_text_list = text.split("\n")

    fp.close()
    text_converter.close()
    out_text.close()

    return text, pdf_to_text_list

text,pdf_to_text_list = pdffile_totext(file)
#print(text)
#print(pdf_to_text_list)