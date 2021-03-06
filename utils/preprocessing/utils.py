from typing import List

def longest_num(num: str) -> int:
  '''
  :param num: Receives a string containing digits and other characters
  :return: Number of digits present in the string
  '''
  i = 0
  for n in num:
    if n.isdigit():
      i += 1
  return i

def most_common(lst: List[str]) -> str:
  '''
  :param lst: Recevies a list of strings
  :return: Returns a string containing the most common element in list
  '''
  return max(set(lst), key=lst.count)

def search_keyword(text, keyword_list):
  for word in keyword_list:
    word = str(word)
    if word.title() in text or word.upper() in text or word.capitalize() in text:
      return True
  return False