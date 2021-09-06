import spacy
from spacy.matcher import Matcher
import json
import re

nlp = spacy.load('en_core_web_lg')
matcher = Matcher(nlp.vocab)
stopwords = nlp.Defaults.stop_words
with open('./utils/preprocessing/words/bans.json') as io:
  banwords = json.load(io)
with open('./utils/preprocessing/words/skills.csv', 'r') as io:
  skillset = io.read().split(',')

def extract_name(text: str):
  nlp_text = nlp(text)
  
  # First name and Last name are always Proper Nouns
  pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
  
  matcher.add('NAME', [pattern])
  
  matches = matcher(nlp_text)
  
  for match_id, start, end in matches:
      span = nlp_text[start:end]
      return span.text

def extract_email(text: str):
  email = re.findall("([^@|\s]+@[^@]+\.[^@|\s]+)", text)
  if email:
      try:
          return email[0].split()[0].strip(';')
      except IndexError:
          return None

def extract_phone_number(text: str):
  phone_format =re.compile(r'(\+?\d{3}[-\. \t]??\d{3}[-\. \t]??\d{4}|\(\d{3}\)[-\. \t]??\d{3}[-\. \t]??\d{4}|\d{3}[-\. \t]??\d{4}|\+?\d{4}[-\. \t]??\d{3}[-\. \t]??\d{3}|\+?\d{2}[-\. \t]??\d{3,}|\+?\d{4}[-\. \t]??\d{4,})')
  phone = re.findall(phone_format, text)
  if phone:
    for number in phone:
      if len(number) < 5:
        pass
      if number.startswith('+'):
        return number
      elif len(number) > 10 and not number.startswith('0'):
        return '+' + number
    return max(phone, key=len) # should count len of numbers not raw string (here more spaces win)

def preprocess(text: str):
  start_len = len(text)
  lines = text.split('\n')
  skills = []
  for i, line in enumerate(lines):
    line = line.split()
    new_line = []
    for word in line:
      # Remove stopwords & ban words
      if word.lower() not in stopwords and word.lower() not in banwords:
        new_line.append(word)
        # If not a ban / stop word, check if skill & ads it into skill list
        if word.lower() in skillset and word.lower() not in skills:
          skills.append(word.lower())
    lines[i] = ' '.join(new_line)
  text = '\n'.join(lines)
  print(extract_name(text))
  print(extract_phone_number(text))
  print(extract_email(text))
  print(f'skills:\n{skills}')

  # lines = [line for line in lines if line] #Removes empty lines from text
  # text = ' '.join(lines)
  # print(text)
  # print(lines)
  end_len = len(text)
  print(f'Length: {end_len}\nReduced: {start_len - end_len}')