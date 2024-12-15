# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1g5BlyeX3WqMbP5yDeOjBrjEGqwgP30rW
"""

!pip install transformers

from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

def siir_yaz(konu, tur):
  prompt = f"{tur} tarzında {konu} hakkında bir şiir:"
  sonuc = generator(prompt, max_length=100, num_return_sequences=1)
  siir = sonuc[0]['generated_text'].split(prompt)[-1].strip()
  return siir

konu = input("Şiirin konusu ne olsun? ")
tur = input("Hangi türde şiir olsun? (ör: sone, haiku, serbest) ")

siir = siir_yaz(konu, tur)

print("\nİşte senin şiirin:\n")
print(siir)