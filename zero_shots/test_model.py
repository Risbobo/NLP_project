from numpy import rec
from torch import device
from datasets import load_dataset
from transformers import pipeline
import xlwt
from xlwt import Workbook
from datasets import load_dataset

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from sklearn.metrics import f1_score
from sklearn.metrics import (
    precision_recall_fscore_support,
    multilabel_confusion_matrix,
    classification_report,
    confusion_matrix,
    balanced_accuracy_score,
    roc_auc_score,
    average_precision_score, matthews_corrcoef
)

classifier = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli", device=0)

set = 'validation'
dataset = load_dataset('swiss_judgment_prediction', 'fr')

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(0, 0, 'Predicted')
sheet1.write(0, 1, 'Labels')
sheet1.write(0, 2, 'Scores')
sheet1.write(0, 3, 'ID')
sheet1.write(0, 4, 'Year')
sheet1.write(0, 5, 'Label')
sheet1.write(0, 6, 'Language')
sheet1.write(0, 7, 'Region')
sheet1.write(0, 8, 'Canton')
sheet1.write(0, 9, 'Legal Area')
sheet1.write(0, 10, 'Correct')
sheet1.write(0, 11, 'be')
sheet1.write(0, 12, 'ag')
sheet1.write(0, 13, 'fr')
sheet1.write(0, 14, 'ge')
sheet1.write(0, 15, 'gl')
sheet1.write(0, 16, 'gr')
sheet1.write(0, 17, 'ju')
sheet1.write(0, 18, 'lu')
sheet1.write(0, 19, 'ne')
sheet1.write(0, 20, 'sg')
sheet1.write(0, 21, 'sh')
sheet1.write(0, 22, 'sz')
sheet1.write(0, 23, 'so')
sheet1.write(0, 24, 'tg')
sheet1.write(0, 25, 'ti')
sheet1.write(0, 26, 'ur')
sheet1.write(0, 27, 'vs')
sheet1.write(0, 28, 'vd')
sheet1.write(0, 29, 'zg')
sheet1.write(0, 30, 'zh')
sheet1.write(0, 31, 'ar')
sheet1.write(0, 32, 'ai')
sheet1.write(0, 33, 'bs')
sheet1.write(0, 34, 'bl')
sheet1.write(0, 35, 'ow')
sheet1.write(0, 36, 'nw')
sheet1.write(0, 37, 'ch')
sheet1.write(0, 38, 'n/a')
sheet1.write(0, 39, 'penal law')
sheet1.write(0, 40, 'social law')
sheet1.write(0, 41, 'civil law')
sheet1.write(0, 42, 'public law')
sheet1.write(0, 43, 'de')
sheet1.write(0, 44, 'fr')
sheet1.write(0, 45, 'it')

counter = 1
count = 0
total = len(dataset[set])

sheet1.write(total+1, 0, 'Correct:')
sheet1.write(total+1, 1, 'be:')
sheet1.write(total+1, 2, 'ag')
sheet1.write(total+1, 3, 'fr')
sheet1.write(total+1, 4, 'ge')
sheet1.write(total+1, 5, 'gl')
sheet1.write(total+1, 6, 'gr')
sheet1.write(total+1, 7, 'ju')
sheet1.write(total+1, 8, 'lu')
sheet1.write(total+1, 9, 'ne')
sheet1.write(total+1, 10, 'sg')
sheet1.write(total+1, 11, 'sh')
sheet1.write(total+1, 12, 'sz')
sheet1.write(total+1, 13, 'so')
sheet1.write(total+1, 14, 'tg')
sheet1.write(total+1, 15, 'ti')
sheet1.write(total+1, 16, 'ur')
sheet1.write(total+1, 17, 'vs')
sheet1.write(total+1, 18, 'vd')
sheet1.write(total+1, 19, 'zg')
sheet1.write(total+1, 20, 'zh')
sheet1.write(total+1, 21, 'ar')
sheet1.write(total+1, 22, 'ai')
sheet1.write(total+1, 23, 'bs')
sheet1.write(total+1, 24, 'bl')
sheet1.write(total+1, 25, 'ow')
sheet1.write(total+1, 26, 'nw')
sheet1.write(total+1, 27, 'ch')
sheet1.write(total+1, 28, 'n/a')
sheet1.write(total+1, 29, 'penal law')
sheet1.write(total+1, 30, 'social law')
sheet1.write(total+1, 31, 'civil law')
sheet1.write(total+1, 32, 'public law')

be = 0
ag = 0
fr = 0
ge = 0
gl = 0
gr = 0
ju = 0
lu = 0
ne = 0
sg = 0
sh = 0
sz = 0
so = 0
tg = 0
ti = 0
ur = 0
vs = 0
vd = 0
zg = 0
zh = 0
ar = 0
ai = 0
bs = 0
bl = 0
ow = 0
nw = 0
ch = 0
na = 0
penal = 0
social = 0
civil = 0
public = 0

scorebe = 0
scoreag = 0
scorefr = 0
scorege = 0
scoregl = 0
scoregr = 0
scoreju = 0
scorelu = 0
scorene = 0
scoresg = 0
scoresh = 0
scoresz = 0
scoreso = 0
scoretg = 0
scoreti = 0
scoreur = 0
scorevs = 0
scorevd = 0
scorezg = 0
scorezh = 0
scorear = 0
scoreai = 0
scorebs = 0
scorebl = 0
scoreow = 0
scorenw = 0
scorech = 0
scorena = 0
scorepenal = 0
scoresocial = 0
scorecivil = 0
scorepublic = 0

def cantonBE():
    global be
    be += 1
def cantonAG():
    global ag
    ag += 1
def cantonFR():
    global fr 
    fr += 1
def cantonGE():
    global ge
    ge += 1
def cantonGL():
    global gl 
    gl += 1
def cantonGR(): 
    global gr
    gr += 1
def cantonJU():
    global ju 
    ju += 1
def cantonLU():
    global lu 
    lu += 1
def cantonNE(): 
    global ne
    ne += 1
def cantonSG():
    global sg 
    sg += 1
def cantonSH():
    global sh 
    sh += 1
def cantonSZ(): 
    global sz
    sz += 1
def cantonSO():
    global so 
    so += 1
def cantonTG():
    global tg 
    tg += 1
def cantonTI():
    global ti 
    ti += 1
def cantonUR():
    global ur 
    ur += 1
def cantonVS():
    global vs 
    vs += 1
def cantonVD():
    global vd 
    vd += 1
def cantonZG():
    global zg 
    zg += 1
def cantonZH():
    global zh 
    zh += 1
def cantonAR():
    global ar 
    ar += 1
def cantonAI():
    global ai 
    ai += 1
def cantonBS():
    global bs 
    bs += 1
def cantonBL():
    global bl 
    bl += 1
def cantonOW():
    global ow 
    ow += 1
def cantonNW():
    global nw 
    nw += 1
def cantonCH():
    global ch 
    ch += 1
def cantonNA():
    global na 
    na += 1
def penalLaw():
    global penal
    penal += 1
def socialLaw():
    global social
    social += 1
def publicLaw():
    global public
    public += 1
def civilLaw():
    global civil
    civil += 1

#Scores
def ScoreCantonBE():
    global scorebe
    scorebe += 1
def ScoreCantonAG():
    global scoreag
    scoreag += 1
def ScoreCantonFR():
    global scorefr 
    scorefr += 1
def ScoreCantonGE():
    global scorege 
    scorege += 1
def ScoreCantonGL():
    global scoregl 
    scoregl += 1
def ScoreCantonGR():
    global scoregr 
    scoregr += 1
def ScoreCantonJU():
    global scoreju 
    scoreju += 1
def ScoreCantonLU():
    global scorelu
    scorelu += 1
def ScoreCantonNE():
    global scorene 
    scorene += 1
def ScoreCantonSG():
    global scoresg
    scoresg += 1
def ScoreCantonSH():
    global scoresh 
    scoresh += 1
def ScoreCantonSZ():
    global scoresz 
    scoresz += 1
def ScoreCantonSO():
    global scoreso 
    scoreso += 1
def ScoreCantonTG():
    global scoretg 
    scoretg += 1
def ScoreCantonTI():
    global scoreti
    scoreti += 1
def ScoreCantonUR():
    global scoreur 
    scoreur += 1
def ScoreCantonVS():
    global scorevs 
    scorevs += 1
def ScoreCantonVD():
    global scorevd 
    scorevd += 1
def ScoreCantonZG():
    global scorezg 
    scorezg += 1
def ScoreCantonZH():
    global scorezh 
    scorezh += 1
def ScoreCantonAR():
    global scorear 
    scorear += 1
def ScoreCantonAI():
    global scoreai 
    scoreai += 1
def ScoreCantonBS():
    global scorebs 
    scorebs += 1
def ScoreCantonBL():
    global scorebl 
    scorebl += 1
def ScoreCantonOW():
    global scoreow 
    scoreow += 1
def ScoreCantonNW():
    global scorenw 
    scorenw += 1
def ScoreCantonCH():
    global scorech 
    scorech += 1
def ScoreCantonNA():
    global scorena 
    scorena += 1
def ScorePenalLaw():
    global scorepenal
    scorepenal += 1
def ScoreSocialLaw():
    global scoresocial
    scoresocial += 1
def ScorePublicLaw():
    global scorepublic
    scorepublic += 1
def ScoreCivilLaw():
    global scorecivil
    scorecivil += 1

options = {'be': cantonBE,
           'ag': cantonAG,
           'fr': cantonFR,
           'ge': cantonGE,
           'gl': cantonGL,
           'gr': cantonGR,
           'ju': cantonJU,
           'lu' : cantonLU,
           'ne' : cantonNE,
           'sg' : cantonSG,
           'sh' : cantonSH,
           'sz' : cantonSZ,
           'so' : cantonSO,
           'tg' : cantonTG,
           'ti' : cantonTI,
           'ur' : cantonUR,
           'vs' : cantonVS,
           'vd' : cantonVD,
           'zg' : cantonZG,
           'zh' : cantonZH,
           'ar' : cantonAR,
           'ai' : cantonAI,
           'bs' : cantonBS,
           'bl' : cantonBL,
           'ow' : cantonOW,
           'nw' : cantonNW,
           'ch' : cantonCH,
           'n/a' : cantonNA,
           }

optionsLaw = {
    'penal law': penalLaw,
    'social law': socialLaw,
    'public law': publicLaw,
    'civil law' : civilLaw,
}

optionsScore = {'be': ScoreCantonBE,
           'ag': ScoreCantonAG,
           'fr': ScoreCantonFR,
           'ge': ScoreCantonGE,
           'gl': ScoreCantonGL,
           'gr': ScoreCantonGR,
           'ju': ScoreCantonJU,
           'lu' : ScoreCantonLU,
           'ne' : ScoreCantonNE,
           'sg' : ScoreCantonSG,
           'sh' : ScoreCantonSH,
           'sz' : ScoreCantonSZ,
           'so' : ScoreCantonSO,
           'tg' : ScoreCantonTG,
           'ti' : ScoreCantonTI,
           'ur' : ScoreCantonUR,
           'vs' : ScoreCantonVS,
           'vd' : ScoreCantonVD,
           'zg' : ScoreCantonZG,
           'zh' : ScoreCantonZH,
           'ar' : ScoreCantonAR,
           'ai' : ScoreCantonAI,
           'bs' : ScoreCantonBS,
           'bl' : ScoreCantonBL,
           'ow' : ScoreCantonOW,
           'nw' : ScoreCantonNW,
           'ch' : ScoreCantonCH,
           'n/a' : ScoreCantonNA,
           }

optionsLawScore = {
    'penal law': ScorePenalLaw,
    'social law': ScoreSocialLaw,
    'public law': ScorePublicLaw,
    'civil law' : ScoreCivilLaw,
}

#approved = Positive = 1
#dismissed = Negative = 0

#tp = true positives
tp = 0
#fp = false positves
fp = 0
#fn = false negatives
fn = 0
#tn = true negatives
tn = 0

labelList = list()
predList = list()

for data in dataset[set]:
    sequence = data['text']
    language = data['language']
    #candidate_labels = ['Approved', 'Dismissed']
    #hypothesis_template = "This case is {}."
    if language == 'de':
        #candidate_labels = ['genehmigt', 'abgelehnt']
        candidate_labels = ['approved', 'dismissed']
        hypothesis_template = "The court decides {}."
        print(f'Hypothesis: {hypothesis_template}')
    if language == 'fr':
        #candidate_labels = ['approuvé', 'refusé']
        candidate_labels = ['approved', 'dismissed']
        #hypothesis_template = "Ce cas est {}."
        hypothesis_template = "The court decides {}."
        print(f'Hypothesis: {hypothesis_template}')
    if language == 'it':
        candidate_labels = ['approved', 'dismissed']
        hypothesis_template = "The court decides {}."
        print(f'Hypothesis: {hypothesis_template}')

    #This block counts every element
    options[data['canton']]()
    optionsLaw[data['legal area']]()
    

    pred = classifier(sequence, candidate_labels, hypothesis_template=hypothesis_template)
    print(data['id'])
    print(pred)
    sheet1.write(counter, 1, pred['labels'])
    sheet1.write(counter, 2, str(pred['scores']))
    sheet1.write(counter, 3, data['id'])
    sheet1.write(counter, 4, data['year'])
    sheet1.write(counter, 5, data['label'])
    sheet1.write(counter, 6, data['language'])
    sheet1.write(counter, 7, data['region'])
    sheet1.write(counter, 8, data['canton'])
    sheet1.write(counter, 9, data['legal area'])

    counter += 1
    labelList.append(data['label'])

    if (pred['labels'][0] == "abgelehnt") or (pred['labels'][0] == "dismissed") or (pred['labels'][0] == "refusé"):
      print("dismissed")
      predList.append(0)
      if int(data['label']) == 0:
        count += 1
        optionsScore[data['canton']]()
        optionsLawScore[data['legal area']]()
        tn += 1
        print("+1")
      else:
          fn += 1
    elif (pred['labels'][0] == "genehmigt") or (pred['labels'][0] == "approved") or (pred['labels'][0] == "approuvé"):
      print("approved")
      predList.append(1)
      if int(data['label']) == 1:
        count += 1
        optionsScore[data['canton']]()
        optionsLawScore[data['legal area']]()
        tp += 1
        print("+1")
      else:
          fp += 1
    print(pred['scores'])
    print(pred['labels'])
    #score = pred['scores']
    #decision = 1 if score[0] >= score[1] else 0
    #if decision == data['label']:
    #    count += 1


sheet1.write(total+2, 0, count)
sheet1.write(total+2, 1, scorebe)
sheet1.write(total+2, 2, scoreag)
sheet1.write(total+2, 3, scorefr)
sheet1.write(total+2, 4, scorege)
sheet1.write(total+2, 5, scoregl)
sheet1.write(total+2, 6, scoregr)
sheet1.write(total+2, 7, scoreju)
sheet1.write(total+2, 8, scorelu)
sheet1.write(total+2, 9, scorene)
sheet1.write(total+2, 10, scoresg)
sheet1.write(total+2, 11, scoresh)
sheet1.write(total+2, 12, scoresz)
sheet1.write(total+2, 13, scoreso)
sheet1.write(total+2, 14, scoretg)
sheet1.write(total+2, 15, scoreti)
sheet1.write(total+2, 16, scoreur)
sheet1.write(total+2, 17, scorevs)
sheet1.write(total+2, 18, scorevd)
sheet1.write(total+2, 19, scorezg)
sheet1.write(total+2, 20, scorezh)
sheet1.write(total+2, 21, scorear)
sheet1.write(total+2, 22, scoreai)
sheet1.write(total+2, 23, scorebs)
sheet1.write(total+2, 24, scorebl)
sheet1.write(total+2, 25, scoreow)
sheet1.write(total+2, 26, scorenw)
sheet1.write(total+2, 27, scorech)
sheet1.write(total+2, 28, scorena)
sheet1.write(total+2, 29, scorepenal)
sheet1.write(total+2, 30, scoresocial)
sheet1.write(total+2, 31, scorecivil)
sheet1.write(total+2, 32, scorepublic)

sheet1.write(total+3, 0, total)
sheet1.write(total+3, 1, be)
sheet1.write(total+3, 2, ag)
sheet1.write(total+3, 3, fr)
sheet1.write(total+3, 4, ge)
sheet1.write(total+3, 5, gl)
sheet1.write(total+3, 6, gr)
sheet1.write(total+3, 7, ju)
sheet1.write(total+3, 8, lu)
sheet1.write(total+3, 9, ne)
sheet1.write(total+3, 10, sg)
sheet1.write(total+3, 11, sh)
sheet1.write(total+3, 12, sz)
sheet1.write(total+3, 13, so)
sheet1.write(total+3, 14, tg)
sheet1.write(total+3, 15, ti)
sheet1.write(total+3, 16, ur)
sheet1.write(total+3, 17, vs)
sheet1.write(total+3, 18, vd)
sheet1.write(total+3, 19, zg)
sheet1.write(total+3, 20, zh)
sheet1.write(total+3, 21, ar)
sheet1.write(total+3, 22, ai)
sheet1.write(total+3, 23, bs)
sheet1.write(total+3, 24, bl)
sheet1.write(total+3, 25, ow)
sheet1.write(total+3, 26, nw)
sheet1.write(total+3, 27, ch)
sheet1.write(total+3, 28, na)
sheet1.write(total+3, 29, penal)
sheet1.write(total+3, 30, social)
sheet1.write(total+3, 31, civil)
sheet1.write(total+3, 32, public)

sheet1.write(total+5, 0, 'tp:')
sheet1.write(total+6, 0, tp)
sheet1.write(total+5, 1, 'tn:')
sheet1.write(total+6, 1, tn)
sheet1.write(total+5, 2, 'fp:')
sheet1.write(total+6, 2, fp)
sheet1.write(total+5, 3, 'fn:')
sheet1.write(total+6, 3, fn)

precision = tp/(tp+fp)
recall = tp/(tp+fn)
fscore = 2 * (precision*recall) / (precision+recall)

sheet1.write(total+7, 0, 'precision:')
sheet1.write(total+7, 1, precision)
sheet1.write(total+7, 3, 'recall:')
sheet1.write(total+7, 4, recall)
sheet1.write(total+8, 0, 'F1 score:')
sheet1.write(total+8, 1, fscore)

print("mDEBERTA")

# Score
print(count)
print(total)
print(count/total)

print(f"True positives: {tp}")
print(f"True negatives: {tn}")
print(f"False positives: {fp}")
print(f"False negatives: {fn}")

print(f"F1 score: {fscore}")
print(f"precision: {precision}")
print(f"recall: {recall}")
skFScore = f1_score(labelList, predList, average='macro')
print(f"Sklearn F1 score: {skFScore}")
mcc = matthews_corrcoef(labelList, predList)
print(f"sklearn mcc: {mcc}")
skprecision, skrecall, skf1_macro, _ = precision_recall_fscore_support(labelList, predList, average='macro')
print(f"Sklearn Precision: {skprecision}")
print(f"Sklearn Recall: {skrecall}")
print(f"Sklearn F1 macro: {skf1_macro}")

sheet1.write(total+8, 3, 'Sklearn F1 score:')
sheet1.write(total+8, 4, skFScore)
sheet1.write(total+9, 0, 'MCC:')
sheet1.write(total+9, 1, mcc)
sheet1.write(total+10, 0, 'Sklearn Precision:')
sheet1.write(total+10, 1, skprecision)
sheet1.write(total+10, 3, 'Sklearn Recall:')
sheet1.write(total+10, 4, skrecall)
sheet1.write(total+10, 6, 'Sklearn F1 macro score:')
sheet1.write(total+10, 7, skf1_macro)

#Save Excel file
wb.save('ResultsMDEBERTA2EngHypoLabelFR.xls')