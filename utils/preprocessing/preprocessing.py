import spacy
from spacy.matcher import Matcher
import json
import re

from utils.preprocessing.utils import longest_num, most_common

nlp = spacy.load('en_core_web_lg')
matcher = Matcher(nlp.vocab)
stopwords = nlp.Defaults.stop_words
with open('./utils/preprocessing/words/bans.json') as io:
  banwords = json.load(io)
with open('./utils/preprocessing/words/skills.csv', 'r') as io:
  skillset = io.read().split(',')

def extract_name(text: str):
  '''
  Ideas:
    Check if name matches with email
    Use Matcher + NER
    Just grab first words
    Try Other NER than Spacy
  '''
  doc = nlp(text)
  result = []
  for ent in doc.ents:
    if ent.label_ == 'PERSON':
      print(ent.label_, ent.text)
      result.append(ent.text)
    else:
      next
  if len(result) > 0:
    res = result[0].split('\n')[0]
    print("*"*10)
    return res.strip()
  else:
    return 'no name'

def extract_email(text: str):
  email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", text)
  if email:
      try:
          return email[0].split()[0].strip(';')
      except IndexError:
          return None

def extract_phone_number(text: str):
  phone_format = re.compile(r'(\+?\d{3}[-\. \t]?\d{3}[-\. \t]?\d{4,6}|\(\+?\d{2,3}\)[-\. \t]?\d{3}[-\. \t]?\d{4,8}|\d{3}[-\. \t]?\d{4}|\+?\d{4}[-\. \t]?\d{3}[-\. \t]?\d{3}|\+?\d{2}[-\. \t]?\d{3,}|\+?\d{4}[-\. \t]?\d{4,})')
  phone = re.findall(phone_format, text)
  if phone:
    for number in phone:
      if len(number) < 5:
        pass
      if number.startswith('+'):
        return number
      elif len(number) > 10 and not number.startswith('0') and not '+' in number:
        return '+' + number
      elif len(number) > 10 and '+' in number:
        return number
    return max(phone, key=longest_num)

def preprocess(text: str):
  start_len = len(text)

  # Remove stopwords & ban words
  lines = text.split('\n')
  cleaned_text = []
  for i, line in enumerate(lines):
    line = line.split()
    new_line = []
    for word in line:
      if word.lower() not in banwords:
        new_line.append(word)
    lines[i] = ' '.join(new_line)
  text = '\n'.join(lines)
  # print(text)
  
  print(extract_name(text))
  # print(extract_phone_number(text))
  print(extract_email(text))
  # print(f'skills:\n{skills}')

  # lines = [line for line in lines if line] #Removes empty lines from text
  # text = ' '.join(lines)
  # print(text)
  # print(lines)
  end_len = len(text)
  # print(f'Length: {end_len}\nReduced: {start_len - end_len}')