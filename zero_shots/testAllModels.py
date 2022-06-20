from bart import Bart
from mdeberta import Mdeberta
from roberta import Roberta
import plotly.express as px
import pandas as pd

metrics = list()
set = 'validation'

#-----------------BART--------------------
language = 'de'
labelDE = ['genehmigt', 'abgelehnt']
hypoDE = "Dieser Fall wurde {}."
bDE = Bart(language, set, hypoDE, labelDE)
print(bDE)
bDE.runBart()
print(bDE.getData())
metrics.append(bDE.getData())

language = 'fr'
labelFR = ['approuvé', 'refusé']
hypoFR = "Ce cas est {}."
bFR = Bart(language, set, hypoFR, labelFR)
bFR.runBart()
print(bFR.getData())
metrics.append(bFR.getData())

language = 'it'
labelIT = ['approved', 'dismissed']
hypoIT = "This case is {}."
bIT = Bart(language, set, hypoIT, labelIT)
bIT.runBart()
metrics.append(bIT.getData())

#-----------------Mdeberta-------------------
language = 'de'
labelDE = ['genehmigt', 'abgelehnt']
hypoDE = "Dieser Fall wurde {}."
mDE = Mdeberta(language, set, hypoDE, labelDE)
print(mDE)
mDE.runMdeberta()
print(mDE.getData())
metrics.append(mDE.getData())

language = 'fr'
labelFR = ['approuvé', 'refusé']
hypoFR = "Ce cas est {}."
mFR = Mdeberta(language, set, hypoFR, labelFR)
mFR.runMdeberta()
print(mFR.getData())
metrics.append(mFR.getData())

language = 'it'
labelIT = ['approved', 'dismissed']
hypoIT = "This case is {}."
mIT = Mdeberta(language, set, hypoIT, labelIT)
mIT.runMdeberta()
metrics.append(mIT.getData())

#--------------Roberta------------------
language = 'de'
labelDE = ['genehmigt', 'abgelehnt']
hypoDE = "Dieser Fall wurde {}."
rDE = Roberta(language, set, hypoDE, labelDE)
print(rDE)
rDE.runRoberta()
print(rDE.getData())
metrics.append(rDE.getData())

language = 'fr'
labelFR = ['approuvé', 'refusé']
hypoFR = "Ce cas est {}."
rFR = Roberta(language, set, hypoFR, labelFR)
rFR.runRoberta()
print(rFR.getData())
metrics.append(rFR.getData())

language = 'it'
labelIT = ['approved', 'dismissed']
hypoIT = "This case is {}."
rIT = Roberta(language, set, hypoIT, labelIT)
rIT.runRoberta()
metrics.append(rIT.getData())

print(f'Data: {metrics}')

df = pd.DataFrame(metrics, columns=['Model', 'Language', 'skf1', 'mcc', 'acc', 
                                    'TrueNegatives', 'FalsePositives', 'FalseNegatives', 'TruePositives'])
pd.options.display.max_columns = None
pd.options.display.max_rows = None
print(df)
df.to_csv('dfAllModelsTestRun1Normal.csv')