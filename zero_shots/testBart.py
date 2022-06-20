from bart import Bart
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

pd.options.display.max_columns = None
pd.options.display.max_rows = None

language = 'de'
labelDE = ['genehmigt', 'abgelehnt']
#labelDE = ['approved', 'dismissed']
hypoDE = "Die Beschwerde wurde {}."
#hypoDE = "The complaint was {}."
bDE = Bart(language, set, hypoDE, labelDE)
bDE.runBart()
print(bDE.getData())
""" metricsN.append(bDE.getData())
cantonsN.extend(bDE.getCanton()) """
legalsN.extend(bDE.getLegals())

#labelDE = ['genehmigt', 'abgelehnt']
labelDE = ['approved', 'dismissed']
hypoDE = "Die Beschwerde wurde {}."
#hypoDE = "The complaint was {}."
bDE = Bart(language, set, hypoDE, labelDE)
bDE.runBart()
print(bDE.getData())
""" metricsL.append(bDE.getData())
cantonsL.extend(bDE.getCanton()) """
legalsL.extend(bDE.getLegals())

labelDE = ['genehmigt', 'abgelehnt']
#labelDE = ['approved', 'dismissed']
#hypoDE = "Die Beschwerde wurde {}."
hypoDE = "The complaint was {}."
bDE = Bart(language, set, hypoDE, labelDE)
bDE.runBart()
print(bDE.getData())
""" metricsH.append(bDE.getData())
cantonsH.extend(bDE.getCanton()) """
legalsH.extend(bDE.getLegals())

#labelDE = ['genehmigt', 'abgelehnt']
labelDE = ['approved', 'dismissed']
#hypoDE = "Die Beschwerde wurde {}."
hypoDE = "The complaint was {}."
bDE = Bart(language, set, hypoDE, labelDE)
bDE.runBart()
print(bDE.getData())
""" metricsHL.append(bDE.getData())
cantonsHL.extend(bDE.getCanton()) """
legalsHL.extend(bDE.getLegals())



language = 'fr'
labelFR = ['approuvé', 'refusé']
#labelFR = ['approved', 'dismissed']
hypoFR = "La plainte était {}."
#hypoFR = "The complaint was {}."
bFR = Bart(language, set, hypoFR, labelFR)
bFR.runBart()
print(bFR.getData())
""" metricsN.append(bFR.getData())
cantonsN.extend(bFR.getCanton()) """
legalsN.extend(bFR.getLegals())

#labelFR = ['approuvé', 'refusé']
labelFR = ['approved', 'dismissed']
hypoFR = "La plainte était {}."
#hypoFR = "The complaint was {}."
bFR = Bart(language, set, hypoFR, labelFR)
bFR.runBart()
print(bFR.getData())
""" metricsL.append(bFR.getData())
cantonsL.extend(bFR.getCanton()) """
legalsL.extend(bFR.getLegals())

labelFR = ['approuvé', 'refusé']
#labelFR = ['approved', 'dismissed']
#hypoFR = "La plainte était {}."
hypoFR = "The complaint was {}."
bFR = Bart(language, set, hypoFR, labelFR)
bFR.runBart()
print(bFR.getData())
""" metricsH.append(bFR.getData())
cantonsH.extend(bFR.getCanton()) """
legalsH.extend(bFR.getLegals())

#labelFR = ['approuvé', 'refusé']
labelFR = ['approved', 'dismissed']
#hypoFR = "La plainte était {}."
hypoFR = "The complaint was {}."
bFR = Bart(language, set, hypoFR, labelFR)
bFR.runBart()
print(bFR.getData())
""" metricsHL.append(bFR.getData())
cantonsHL.extend(bFR.getCanton()) """
legalsHL.extend(bFR.getLegals())



language = 'it'
labelIT = ['approvato', 'respinto']
#labelIT = ['approved', 'dismissed']
hypoIT = "Il reclamo era {}."
#hypoIT = "The complaint was {}."
bIT = Bart(language, set, hypoIT, labelIT)
bIT.runBart()
metricsN.append(bIT.getData())
cantonsN.extend(bIT.getCanton())
legalsN.extend(bIT.getLegals())

#labelIT = ['approvato', 'respinto']
labelIT = ['approved', 'dismissed']
hypoIT = "Il reclamo era {}."
#hypoIT = "The complaint was {}."
bIT = Bart(language, set, hypoIT, labelIT)
bIT.runBart()
""" metricsL.append(bIT.getData())
cantonsL.extend(bIT.getCanton()) """
legalsL.extend(bIT.getLegals())

labelIT = ['approvato', 'respinto']
#labelIT = ['approved', 'dismissed']
#hypoIT = "Il reclamo era {}."
hypoIT = "The complaint was {}."
bIT = Bart(language, set, hypoIT, labelIT)
bIT.runBart()
""" metricsH.append(bIT.getData())
cantonsH.extend(bIT.getCanton()) """
legalsH.extend(bIT.getLegals())

#labelIT = ['approvato', 'respinto']
labelIT = ['approved', 'dismissed']
#hypoIT = "Il reclamo era {}."
hypoIT = "The complaint was {}."
bIT = Bart(language, set, hypoIT, labelIT)
bIT.runBart()
""" metricsHL.append(bIT.getData())
cantonsHL.extend(bIT.getCanton()) """
legalsHL.extend(bIT.getLegals())

print(f'Data: {metricsN}')



""" dfN = pd.DataFrame(metricsN, columns=['Model', 'Language', 'skf1', 'mcc', 'acc', 
                                    'TrueNegatives', 'FalsePositives', 'FalseNegatives', 'TruePositives'])
dfCantonsN = pd.DataFrame(cantonsN, columns=['Model', 'Language', 'Canton', 'Score', 'Amount', 'Accuracy']) """
dfLegalsN = pd.DataFrame(legalsN, columns=['Model', 'Language', 'Legal Area', 'Score', 'Amount', 'Accuracy'])
""" print(dfN)
print(dfCantonsN) """
print(dfLegalsN)

#print("TestRun 2 but new hypothesis on german set")
""" dfN.to_csv('dfBartTestRun3Normal.csv')
dfCantonsN.to_csv('dfCantonsBartTestRun3Normal.csv') """
dfLegalsN.to_csv('dfLegalsBartTestRun3Normal.csv')

""" dfL = pd.DataFrame(metricsL, columns=['Model', 'Language', 'skf1', 'mcc', 'acc', 
                                    'TrueNegatives', 'FalsePositives', 'FalseNegatives', 'TruePositives'])
dfCantonsL = pd.DataFrame(cantonsL, columns=['Model', 'Language', 'Canton', 'Score', 'Amount', 'Accuracy']) """
dfLegalsL = pd.DataFrame(legalsL, columns=['Model', 'Language', 'Legal Area', 'Score', 'Amount', 'Accuracy'])
""" print(dfL)
print(dfCantonsL) """
print(dfLegalsL)

""" dfL.to_csv('dfBartTestRun3EngLabel.csv')
dfCantonsL.to_csv('dfCantonsBartTestRun3EngLabel.csv') """
dfLegalsL.to_csv('dfLegalsBartTestRun3EngLabel.csv')

""" dfH = pd.DataFrame(metricsH, columns=['Model', 'Language', 'skf1', 'mcc', 'acc', 
                                    'TrueNegatives', 'FalsePositives', 'FalseNegatives', 'TruePositives'])
dfCantonsH = pd.DataFrame(cantonsH, columns=['Model', 'Language', 'Canton', 'Score', 'Amount', 'Accuracy']) """
dfLegalsH = pd.DataFrame(legalsH, columns=['Model', 'Language', 'Legal Area', 'Score', 'Amount', 'Accuracy'])
""" print(dfH)
print(dfCantonsH) """
print(dfLegalsH)

""" dfH.to_csv('dfBartTestRun3EngHypo.csv')
dfCantonsH.to_csv('dfCantonsBartTestRun3EngHypo.csv') """
dfLegalsH.to_csv('dfLegalsBartTestRun3EngHypo.csv')

""" dfHL = pd.DataFrame(metricsHL, columns=['Model', 'Language', 'skf1', 'mcc', 'acc', 
                                    'TrueNegatives', 'FalsePositives', 'FalseNegatives', 'TruePositives'])
dfCantonsHL = pd.DataFrame(cantonsHL, columns=['Model', 'Language', 'Canton', 'Score', 'Amount', 'Accuracy']) """
dfLegalsHL = pd.DataFrame(legalsHL, columns=['Model', 'Language', 'Legal Area', 'Score', 'Amount', 'Accuracy'])
""" print(dfHL)
print(dfCantonsHL) """
print(dfLegalsHL)

""" dfHL.to_csv('dfBartTestRun3EngHypoLabel.csv')
dfCantonsHL.to_csv('dfCantonsBartTestRun3EngHypoLabel.csv') """
dfLegalsHL.to_csv('dfLegalsBartTestRun3EngHypoLabel.csv')