import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# function to convert sequence strings into k-mer words, default size = 6 (hexamer words)
kmer_size = 6
NGram = 4
#KFold_val = 10
def getKmers(sequence, size=kmer_size):
    return [sequence[x:x+size].lower() for x in range(len(sequence) - size + 1)]

print('Reading file...')
#covid19df= pd.read_csv('SARS_MERS_COV_train.csv')
covid19df= pd.read_csv('sars_mers_cov_other_train.csv')

print('Creating token using K_Mer...')
covid19df['words'] = covid19df.apply(lambda x: getKmers(x['SEQ']), axis=1)
covid19df = covid19df.drop('SEQ', axis=1)
covid_texts = list(covid19df['words'])

print('Converting token to list...')
for item in range(len(covid_texts)):
    covid_texts[item] = ' '.join(covid_texts[item])
y_data = covid19df["CLASS"].values

print('Performing Count Vectorization...')
cv = CountVectorizer(ngram_range=(NGram,NGram))
X = cv.fit_transform(covid_texts)
pickle.dump(cv, open('countVectTrain.pkl', 'wb'))

print('Creating Classifiers...')
NB_classifier = MultinomialNB(alpha=0.1)

NB_classifier.fit(X, y_data)
# save the model to disk
filename = 'corona_pred.pkl'
pickle.dump(NB_classifier, open(filename, 'wb'))
