import pandas as pd
data = pd.read_excel('canada.xlsx')
df = pd.DataFrame(data, columns= ['interest','inflation'])
X = df["inflation"]
y = df["interest"]
from statsmodels.tsa.stattools import coint
print('Results of Engle-Granger Test:')
egtest = coint(y, X, trend='c', method='aeg', autolag='AIC')
egoutput = pd.Series(egtest[0:3], index=['Test Statistic','p-value','Critical Values 1%,5%,10%'])
print (egoutput)
