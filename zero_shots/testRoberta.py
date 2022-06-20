from roberta import Roberta
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
rDE = Roberta(language, set, hypoDE, labelDE)
rDE.runRoberta()
print(rDE.getData())
metricsN.append(rDE.getData())
cantonsN.extend(rDE.getCanton())
legalsN.extend(rDE.getLegals())

#labelDE = ['genehmigt', 'abgelehnt']
labelDE = ['approved', 'dismissed']
hypoDE = "Die Beschwerde wurde {}."
#hypoDE = "The complaint was {}."
rDE = Roberta(language, set, hypoDE, labelDE)
rDE.runRoberta()
print(rDE.getData())
metricsL.append(rDE.getData())
cantonsL.extend(rDE.getCanton())
legalsL.extend(rDE.getLegals())

labelDE = ['genehmigt', 'abgelehnt']
#labelDE = ['approved', 'dismissed']
#hypoDE = "Die Beschwerde wurde {}."
hypoDE = "The complaint was {}."
rDE = Roberta(language, set, hypoDE, labelDE)
rDE.runRoberta()
print(rDE.getData())
metricsH.append(rDE.getData())
cantonsH.extend(rDE.getCanton())
legalsH.extend(rDE.getLegals())

#labelDE = ['genehmigt', 'abgelehnt']
labelDE = ['approved', 'dismissed']
#hypoDE = "Die Beschwerde wurde {}."
hypoDE = "The complaint was {}."
rDE = Roberta(language, set, hypoDE, labelDE)
rDE.runRoberta()
print(rDE.getData())
metricsHL.append(rDE.getData())
cantonsHL.extend(rDE.getCanton())
legalsHL.extend(rDE.getLegals())



language = 'fr'
labelFR = ['approuvé', 'refusé']
#labelFR = ['approved', 'dismissed']
hypoFR = "La plainte était {}."
#hypoFR = "The complaint was {}."
rFR = Roberta(language, set, hypoFR, labelFR)
rFR.runRoberta()
print(rFR.getData())
metricsN.append(rFR.getData())
cantonsN.extend(rFR.getCanton())
legalsN.extend(rFR.getLegals())

#labelFR = ['approuvé', 'refusé']
labelFR = ['approved', 'dismissed']
hypoFR = "La plainte était {}."
#hypoFR = "The complaint was {}."
rFR = Roberta(language, set, hypoFR, labelFR)
rFR.runRoberta()
print(rFR.getData())
metricsL.append(rFR.getData())
cantonsL.extend(rFR.getCanton())
legalsL.extend(rFR.getLegals())

labelFR = ['approuvé', 'refusé']
#labelFR = ['approved', 'dismissed']
#hypoFR = "La plainte était {}."
hypoFR = "The complaint was {}."
rFR = Roberta(language, set, hypoFR, labelFR)
rFR.runRoberta()
print(rFR.getData())
metricsH.append(rFR.getData())
cantonsH.extend(rFR.getCanton())
legalsH.extend(rFR.getLegals())

#labelFR = ['approuvé', 'refusé']
labelFR = ['approved', 'dismissed']
#hypoFR = "La plainte était {}."
hypoFR = "The complaint was {}."
rFR = Roberta(language, set, hypoFR, labelFR)
rFR.runRoberta()
print(rFR.getData())
metricsHL.append(rFR.getData())
cantonsHL.extend(rFR.getCanton())
legalsHL.extend(rFR.getLegals())



language = 'it'
labelIT = ['approvato', 'respinto']
#labelIT = ['approved', 'dismissed']
hypoIT = "Il reclamo era {}."
#hypoIT = "The complaint was {}."
rIT = Roberta(language, set, hypoIT, labelIT)
rIT.runRoberta()
metricsN.append(rIT.getData())
cantonsN.extend(rIT.getCanton())
legalsN.extend(rIT.getLegals())

#labelIT = ['approvato', 'respinto']
labelIT = ['approved', 'dismissed']
hypoIT = "Il reclamo era {}."
#hypoIT = "The complaint was {}."
rIT = Roberta(language, set, hypoIT, labelIT)
rIT.runRoberta()
metricsL.append(rIT.getData())
cantonsL.extend(rIT.getCanton())
legalsL.extend(rIT.getLegals())

labelIT = ['approvato', 'respinto']
#labelIT = ['approved', 'dismissed']
#hypoIT = "Il reclamo era {}."
hypoIT = "The complaint was {}."
rIT = Roberta(language, set, hypoIT, labelIT)
rIT.runRoberta()
metricsH.append(rIT.getData())
cantonsH.extend(rIT.getCanton())
legalsH.extend(rIT.getLegals())

#labelIT = ['approvato', 'respinto']
labelIT = ['approved', 'dismissed']
#hypoIT = "Il reclamo era {}."
hypoIT = "The complaint was {}."
rIT = Roberta(language, set, hypoIT, labelIT)
rIT.runRoberta()
metricsHL.append(rIT.getData())
cantonsHL.extend(rIT.getCanton())
legalsHL.extend(rIT.getLegals())

print(f'Data: {metricsN}')

pd.options.display.max_columns = None
pd.options.display.max_rows = None

dfN = pd.DataFrame(metricsN, columns=['Model', 'Language', 'skf1', 'mcc', 'acc', 
                                    'TrueNegatives', 'FalsePositives', 'FalseNegatives', 'TruePositives'])
dfCantonsN = pd.DataFrame(cantonsN, columns=['Model', 'Language', 'Canton', 'Score', 'Amount', 'Accuracy'])
dfLegalsN = pd.DataFrame(legalsN, columns=['Model', 'Language', 'Legal Area', 'Score', 'Amount', 'Accuracy'])
print(dfN)
print(dfCantonsN)
print(dfLegalsN)

#print("TestRun 2 but new hypothesis on german set")
dfN.to_csv('dfRobertaTestRun3Normal-mnli-SJP-v2.csv')
dfCantonsN.to_csv('dfCantonsRobertaTestRun3Normal-mnli-SJP-v2.csv')
dfLegalsN.to_csv('dfLegalsRobertaTestRun3Normal-mnli-SJP-v2.csv')

dfL = pd.DataFrame(metricsL, columns=['Model', 'Language', 'skf1', 'mcc', 'acc', 'TrueNegatives', 'FalsePositives', 'FalseNegatives', 'TruePositives'])
dfCantonsL = pd.DataFrame(cantonsL, columns=['Model', 'Language', 'Canton', 'Score', 'Amount', 'Accuracy'])
dfLegalsL = pd.DataFrame(legalsL, columns=['Model', 'Language', 'Legal Area', 'Score', 'Amount', 'Accuracy'])
#print(dfL)
#print(dfCantonsL)
print(dfLegalsL)

dfL.to_csv('dfRobertaTestRun3EngLabel-mnli-SJP-v2.csv')
dfCantonsL.to_csv('dfCantonsRobertaTestRun3EngLabel-mnli-SJP-v2.csv')
dfLegalsL.to_csv('dfLegalsRobertaTestRun3EngLabel-mnli-SJP-v2.csv')

dfH = pd.DataFrame(metricsH, columns=['Model', 'Language', 'skf1', 'mcc', 'acc', 'TrueNegatives', 'FalsePositives', 'FalseNegatives', 'TruePositives'])
dfCantonsH = pd.DataFrame(cantonsH, columns=['Model', 'Language', 'Canton', 'Score', 'Amount', 'Accuracy'])
dfLegalsH = pd.DataFrame(legalsH, columns=['Model', 'Language', 'Legal Area', 'Score', 'Amount', 'Accuracy'])
#print(dfH)
#print(dfCantonsH)
#print(dfLegalsH)

dfH.to_csv('dfRobertaTestRun3EngHypo-mnli-SJP-v2.csv')
dfCantonsH.to_csv('dfCantonsRobertaTestRun3EngHypo-mnli-SJP-v2.csv')
dfLegalsH.to_csv('dfLegalsRobertaTestRun3EngHypo-mnli-SJP-v2.csv')

dfHL = pd.DataFrame(metricsHL, columns=['Model', 'Language', 'skf1', 'mcc', 'acc', 'TrueNegatives', 'FalsePositives', 'FalseNegatives', 'TruePositives'])
dfCantonsHL = pd.DataFrame(cantonsHL, columns=['Model', 'Language', 'Canton', 'Score', 'Amount', 'Accuracy'])
dfLegalsHL = pd.DataFrame(legalsHL, columns=['Model', 'Language', 'Legal Area', 'Score', 'Amount', 'Accuracy'])
#print(dfHL)
#print(dfCantonsHL)
print(dfLegalsHL)

dfHL.to_csv('dfRobertaTestRun3EngHypoLabel-mnli-SJP-v2.csv')
dfCantonsHL.to_csv('dfCantonsRobertaTestRun3EngHypoLabel-mnli-SJP-v2.csv')
dfLegalsHL.to_csv('dfLegalsRobertaTestRun3EngHypoLabel-mnli-SJP-v2.csv')