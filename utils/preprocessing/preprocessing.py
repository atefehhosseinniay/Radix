from flair.data import Sentence
from flair.models import SequenceTagger
from segtok.segmenter import split_single

import json
import re

from utils.preprocessing.utils import longest_num, most_common
from utils.preprocessing.extract_sections import extract_education, work_section, education_section, skill_section, hobbies_section


tagger = SequenceTagger.load('ner')


with open('./utils/preprocessing/words/bans.json') as io:
  banwords = json.load(io)
with open('./utils/preprocessing/words/skills.csv', 'r') as io:
  skillset = io.read().split(',')

def extract_name(text: str) -> str:
  '''
  Ideas:
    Check if name matches with email
    Use Matcher + NER
    Just grab first words
    Try Other NER than Spacy
  '''
  # Reduce text length, to only check first few sentences
  if len(text) > 500:
    text = text[:500]
  sentences = [Sentence(sent, use_tokenizer=True) for sent in split_single(text)]

  tagger.predict(sentences)
  for sent in sentences:
    for entity in sent.get_spans('ner'):
      if entity.labels[0].value == 'PER':
        return(entity.text)

def extract_email(text: str):
  email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", text)
  if email:
    try:
      return email[0].split()[0].strip(';')
    except IndexError:
      return None

def extract_phone_number(text: str):
  phone_format = re.compile(r'(\+?\d{3}[-\. \t]?\d{3}[-\. \t]?\d{4,7}|\(\+?\d{2,3}\)[-\. \t]?\d{3}[-\. \t]?\d{4,8}|\d{3}[-\. \t]?\d{4}|\+?\d{4}[-\. \t]?\d{3}[-\. \t]?\d{3}|\+?\d{2}[-\. \t]?\d{3,11}|\+?\d{4}[-\. \t]?\d{4,9})')
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

def preprocess(text: str) -> dict:
  result = {}
  start_len = len(text)

  # Remove stopwords & ban words
  lines = text.split('\n')
  lines = [line for line in lines if line] #Removes empty lines from text
  for i, line in enumerate(lines):
    line = line.split()
    new_line = []
    for word in line:
      if len(word) == 1 and ord(word) > 127:
        continue
      if word.lower() in banwords:
        continue
      new_line.append(word)
    lines[i] = ' '.join(new_line)
  text = '\n'.join(lines)
  # print(text)
  
  result['name'] = extract_name(text)
  result['phone'] = extract_phone_number(text)
  result['email'] = extract_email(text)

  lines = text.split('\n')
  result['work'] = work_section(lines)
  edu = education_section(lines)
  result['education'] = edu # extract_education(' '.join(edu))
  result['skill'] = skill_section(lines)
  
  end_len = len(text)
  # print(f'Length: {end_len}\nReduced: {start_len - end_len}')
  return(result)