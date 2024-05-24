#!/usr/bin/env python3
import re
class MyString:
    def __init__(self,sentence=''):
      self._sentence=sentence

    @property
    
    def sentence(self):
       return self._sentence
    
    @sentence.setter
    def sentence(self,sentence):
      if not isinstance(sentence,str):
          print("The value must be a string.")
      else:
        self._sentence=sentence
    
    def is_sentence(self):
       sentence=str(self.sentence)
       return '.' in sentence
   
    @property

    def value(self):

        return self.sentence


    @value.setter

    def value(self, value):

        self.sentence = value

    def is_question(self):
       sentence=str(self.sentence)
       return '?' in sentence

    def is_exclamation(self):
       sentence=str(self.sentence)
       return '!' in sentence  

    def count_sentences(self):
       sentences=re.split('[.!?]',self.sentence)
       sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
       return len(sentences)
      
  