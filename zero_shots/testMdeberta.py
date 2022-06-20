from mdeberta import Mdeberta
import plotly.express as px
import pandas as pd

metricsN = list()
metricsL = list()
metricsH = list()
metricsHL = list()

cantonsN = list()
cantonsL = list()
cantonsH = list()
cantonsHL = list()

legalsN = list()
legalsL = list()
legalsH = list()
legalsHL = list()

set = 'validation'

language = 'de'
labelDE = ['genehmigt', 'abgelehnt']
#labelDE = ['approved', 'dismissed']
hypoDE = "Die Beschwerde wurde {}."
#hypoDE = "The complaint was {}."
mDE = Mdeberta(language, set, hypoDE, labelDE)
mDE.runMdeberta()
print(mDE.getData())
""" metricsN.append(mDE.getData())
cantonsN.extend(mDE.getCanton()) """
legalsN.extend(mDE.getLegals())

#labelDE = ['genehmigt', 'abgelehnt']
labelDE = ['approved', 'dismissed']
hypoDE = "Die Beschwerde wurde {}."
#hypoDE = "The complaint was {}."
mDE = Mdeberta(language, set, hypoDE, labelDE)
mDE.runMdeberta()
print(mDE.getData())
""" metricsL.append(mDE.getData())
cantonsL.extend(mDE.getCanton()) """
legalsL.extend(mDE.getLegals())

labelDE = ['genehmigt', 'abgelehnt']
#labelDE = ['approved', 'dismissed']
#hypoDE = "Die Beschwerde wurde {}."
hypoDE = "The complaint was {}."
mDE = Mdeberta(language, set, hypoDE, labelDE)
mDE.runMdeberta()
print(mDE.getData())
""" metricsH.append(mDE.getData())
cantonsH.extend(mDE.getCanton()) """
legalsH.extend(mDE.getLegals())

#labelDE = ['genehmigt', 'abgelehnt']
labelDE = ['approved', 'dismissed']
#hypoDE = "Die Beschwerde wurde {}."
hypoDE = "The complaint was {}."
mDE = Mdeberta(language, set, hypoDE, labelDE)
mDE.runMdeberta()
print(mDE.getData())
""" metricsHL.append(mDE.getData())
cantonsHL.extend(mDE.getCanton()) """
legalsHL.extend(mDE.getLegals())



language = 'fr'
labelFR = ['approuvé', 'refusé']
#labelFR = ['approved', 'dismissed']
hypoFR = "La plainte était {}."
#hypoFR = "The complaint was {}."
mFR = Mdeberta(language, set, hypoFR, labelFR)
mFR.runMdeberta()
print(mFR.getData())
""" metricsN.append(mFR.getData())
cantonsN.extend(mFR.getCanton()) """
legalsN.extend(mFR.getLegals())

#labelFR = ['approuvé', 'refusé']
labelFR = ['approved', 'dismissed']
hypoFR = "La plainte était {}."
#hypoFR = "The complaint was {}."
mFR = Mdeberta(language, set, hypoFR, labelFR)
mFR.runMdeberta()
print(mFR.getData())
""" metricsL.append(mFR.getData())
cantonsL.extend(mFR.getCanton()) """
legalsL.extend(mFR.getLegals())

labelFR = ['approuvé', 'refusé']
#labelFR = ['approved', 'dismissed']
#hypoFR = "La plainte était {}."
hypoFR = "The complaint was {}."
mFR = Mdeberta(language, set, hypoFR, labelFR)
mFR.runMdeberta()
print(mFR.getData())
""" metricsH.append(mFR.getData())
cantonsH.extend(mFR.getCanton()) """
legalsH.extend(mFR.getLegals())

#labelFR = ['approuvé', 'refusé']
labelFR = ['approved', 'dismissed']
#hypoFR = "La plainte était {}."
hypoFR = "The complaint was {}."
mFR = Mdeberta(language, set, hypoFR, labelFR)
mFR.runMdeberta()
print(mFR.getData())
""" metricsHL.append(mFR.getData())
cantonsHL.extend(mFR.getCanton()) """
legalsHL.extend(mFR.getLegals())



language = 'it'
labelIT = ['approvato', 'respinto']
#labelIT = ['approved', 'dismissed']
hypoIT = "Il reclamo era {}."
#hypoIT = "The complaint was {}."
mIT = Mdeberta(language, set, hypoIT, labelIT)
mIT.runMdeberta()
""" metricsN.append(mIT.getData())
cantonsN.extend(mIT.getCanton()) """
legalsN.extend(mIT.getLegals())

#labelIT = ['approvato', 'respinto']
labelIT = ['approved', 'dismissed']
hypoIT = "Il reclamo era {}."
#hypoIT = "The complaint was {}."
mIT = Mdeberta(language, set, hypoIT, labelIT)
mIT.runMdeberta()
""" metricsL.append(mIT.getData())
cantonsL.extend(mIT.getCanton()) """
legalsL.extend(mIT.getLegals())

labelIT = ['approvato', 'respinto']
#labelIT = ['approved', 'dismissed']
#hypoIT = "Il reclamo era {}."
hypoIT = "The complaint was {}."
mIT = Mdeberta(language, set, hypoIT, labelIT)
mIT.runMdeberta()
""" metricsH.append(mIT.getData())
cantonsH.extend(mIT.getCanton()) """
legalsH.extend(mIT.getLegals())

#labelIT = ['approvato', 'respinto']
labelIT = ['approved', 'dismissed']
#hypoIT = "Il reclamo era {}."
hypoIT = "The complaint was {}."
mIT = Mdeberta(language, set, hypoIT, labelIT)
mIT.runMdeberta()
""" metricsHL.append(mIT.getData())
cantonsHL.extend(mIT.getCanton()) """
legalsHL.extend(mIT.getLegals())

print(f'Data: {metricsN}')

pd.options.display.max_columns = None
pd.options.display.max_rows = None

""" dfN = pd.DataFrame(metricsN, columns=['Model', 'Language', 'skf1', 'mcc', 'acc', 
                                    'TrueNegatives', 'FalsePositives', 'FalseNegatives', 'TruePositives'])
dfCantonsN = pd.DataFrame(cantonsN, columns=['Model', 'Language', 'Canton', 'Score', 'Amount', 'Accuracy']) """
dfLegalsN = pd.DataFrame(legalsN, columns=['Model', 'Language', 'Legal Area', 'Score', 'Amount', 'Accuracy'])
""" print(dfN)
print(dfCantonsN) """
print(dfLegalsN)

#print("TestRun 2 but new hypothesis on german set")
""" dfN.to_csv('dfMdebertaTestRun3Normal.csv')
dfCantonsN.to_csv('dfCantonsMdebertaTestRun3Normal.csv') """
dfLegalsN.to_csv('dfLegalsMdebertaTestRun3Normal.csv')

""" dfL = pd.DataFrame(metricsL, columns=['Model', 'Language', 'skf1', 'mcc', 'acc', 
                                    'TrueNegatives', 'FalsePositives', 'FalseNegatives', 'TruePositives'])
dfCantonsL = pd.DataFrame(cantonsL, columns=['Model', 'Language', 'Canton', 'Score', 'Amount', 'Accuracy']) """
dfLegalsL = pd.DataFrame(legalsL, columns=['Model', 'Language', 'Legal Area', 'Score', 'Amount', 'Accuracy'])
""" print(dfL)
print(dfCantonsL) """
print(dfLegalsL)

""" dfL.to_csv('dfMdebertaTestRun3EngLabel.csv')
dfCantonsL.to_csv('dfCantonsMdebertaTestRun3EngLabel.csv') """
dfLegalsL.to_csv('dfLegalsMdebertaTestRun3EngLabel.csv')

""" dfH = pd.DataFrame(metricsH, columns=['Model', 'Language', 'skf1', 'mcc', 'acc', 
                                    'TrueNegatives', 'FalsePositives', 'FalseNegatives', 'TruePositives'])
dfCantonsH = pd.DataFrame(cantonsH, columns=['Model', 'Language', 'Canton', 'Score', 'Amount', 'Accuracy']) """
dfLegalsH = pd.DataFrame(legalsH, columns=['Model', 'Language', 'Legal Area', 'Score', 'Amount', 'Accuracy'])
""" print(dfH)
print(dfCantonsH) """
print(dfLegalsH)

""" dfH.to_csv('dfMdebertaTestRun3EngHypo.csv')
dfCantonsH.to_csv('dfCantonsMdebertaTestRun3EngHypo.csv') """
dfLegalsH.to_csv('dfLegalsMdebertaTestRun3EngHypo.csv')

""" dfHL = pd.DataFrame(metricsHL, columns=['Model', 'Language', 'skf1', 'mcc', 'acc', 
                                    'TrueNegatives', 'FalsePositives', 'FalseNegatives', 'TruePositives'])
dfCantonsHL = pd.DataFrame(cantonsHL, columns=['Model', 'Language', 'Canton', 'Score', 'Amount', 'Accuracy']) """
dfLegalsHL = pd.DataFrame(legalsHL, columns=['Model', 'Language', 'Legal Area', 'Score', 'Amount', 'Accuracy'])
""" print(dfHL)
print(dfCantonsHL) """
print(dfLegalsHL)

""" dfHL.to_csv('dfMdebertaTestRun3EngHypoLabel.csv')
dfCantonsHL.to_csv('dfCantonsMdebertaTestRun3EngHypoLabel.csv') """
dfLegalsHL.to_csv('dfLegalsMdebertaTestRun3EngHypoLabel.csv')