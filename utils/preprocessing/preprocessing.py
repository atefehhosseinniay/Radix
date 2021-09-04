import spacy
import json

nlp = spacy.load('en_core_web_lg')
stopwords = nlp.Defaults.stop_words
with open('./utils/preprocessing/words/bans.json') as io:
  banwords = json.load(io)

def preprocess(text: str):
  start_len = len(text)
  lines = text.split('\n')
  for i in range(len(lines)):
    line = lines[i]
    line = line.split()
    new_line = []
    for word in line:
      if word.lower() not in stopwords and word.lower() not in banwords:
        new_line.append(word)
    lines[i] = ' '.join(new_line)

  # lines = [line for line in lines if line] #Removes empty lines from text
  # text = ' '.join(lines)
  # print(text)
  print(lines)
  end_len = len(text)
  print(f'Length: {end_len}\nReduced: {start_len - end_len}')