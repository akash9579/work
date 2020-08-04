import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import sys

#print('Reading file...')
infile = sys.argv[1]
covid19df = pd.read_csv(infile)

# function to convert sequence strings into k-mer words, default size = 6 (hexamer words)
kmer_size = 6
NGram = 4
#KFold_val = 10
def getKmers(sequence, size=kmer_size):
    return [sequence[x:x+size].lower() for x in range(len(sequence) - size + 1)]

#print('Creating token using K_Mer...')
covid19df['words'] = covid19df.apply(lambda x: getKmers(x['SEQ']), axis=1)

covid_texts = list(covid19df['words'])
#test_labels = np.array(covid19df.pop('CLASS'))

#print('Converting token to list...')
for item in range(len(covid_texts)):
    covid_texts[item] = ' '.join(covid_texts[item])


#print('Performing Count Vectorization...')
cv = pickle.load(open('countVectTrain.pkl', 'rb'))
X = cv.transform(covid_texts)

# load the model from disk
filename = 'corona_pred.pkl'
model = pickle.load(open(filename, 'rb'))
test_pred = model.predict(X)
pred_prob = model.predict_proba(X)
test_pred_prob = pred_prob.max(1)*100

covid19df = covid19df.drop('words', axis=1)

df_test_pred = pd.DataFrame(data=test_pred, index=None, columns=["pred_label"])
#df_test_labels = pd.DataFrame(data=test_labels, index=None, columns=["test_label"])
df_pred_prob = pd.DataFrame(data=test_pred_prob, index=None, columns=["pred_prob_percentage"])

covid19df.reset_index(inplace = True, drop = True)
df_test_pred.reset_index(inplace = True, drop = True)
#df_test_labels.reset_index(inplace = True, drop = True)
df_out = pd.concat([covid19df, df_test_pred, df_pred_prob], axis=1)
df_out.to_csv('corona_pred_out.csv', index=False)

#mylist = str("Patient ID,Class <br>")
#mylist = str("<table border = 1 ><tr><th>Sequence ID</th><th>&nbsp;&nbsp;&nbsp;Class</th><th>&nbsp;&nbsp;&nbsp;Probability (in %)</th></tr><br>")

#for row in range(df_out.shape[0]):
#    mylist = mylist + "<tr><td>" + df_out.iloc[row,0] + "</td>" +  "<td>&nbsp;&nbsp;&nbsp;" + str(df_out.iloc[row,2]) + "</td>" + "<td>&nbsp;&nbsp;&nbsp;" + str(df_out.iloc[row,3]) + "</td></tr><br>"
#    mylist = mylist + df_out.iloc[row,0] + "," + str(df_out.iloc[row,2]) + " <br>"

#mylist = mylist + "</table>"
#print(mylist)
df_out = df_out.drop('SEQ', axis=1)
df_out_html = df_out.to_html(index = False,justify = 'center')
import re
df_out_html = re.sub(r'PID', r'Sequence ID', df_out_html)
df_out_html = re.sub(r'pred_label', r'Predicted Class', df_out_html)
df_out_html = re.sub(r'pred_prob_percentage', r'Probability (in %)', df_out_html)
print(df_out_html)
