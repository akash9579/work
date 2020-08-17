# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:02:28 2020

@author: CSE
"""


import nltk
from tensorflow.keras.preprocessing.text import one_hot


paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               Why? Because we respect the freedom of others.That is why my 
               first vision is that of freedom. I believe that India got its first vision of 
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India 
               stands up to the world, no one will respect us. Only strength respects strength. We must be 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""
               
               
sentences = nltk.sent_tokenize(paragraph)   # 31 sentences
words = nltk.word_tokenize(paragraph)    # 399 words
a=len(set(words))                        # 188 unique values


# first we perfprm one-hot representation using keras
voc_size=200  # 188 unique values


onehot_repr=[one_hot(words,voc_size)for words in sentences] 
print(onehot_repr)

#  using one-hot encoding we replacing words with interger which was input for embedding layer


from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences    # all sentense should have same lenght sentense
from tensorflow.keras.models import Sequential


sent_length=30     # max sentense length
embedded_docs=pad_sequences(onehot_repr,padding='pre',maxlen=sent_length) # one_hot_repe, pre padding applied in front of sentense
#print(embedded_docs)



dim=20   # feature dimension   # as a hyper parameter


model=Sequential()    # making sequential model
model.add(Embedding(voc_size,dim,input_length=sent_length)) # adding layers we have to give (voc size,dimension,max legth)
model.compile('adam','mse')

model.summary()

print(embedded_docs[0])

test=model.predict(embedded_docs)[0]