from torch import device
from datasets import load_dataset
from transformers import pipeline
import xlwt
from xlwt import Workbook
from datasets import load_dataset
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd

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


class Roberta:
    def __init__(self, language, set, hypo, labels) -> None:
        self.language = language
        self.set = set
        self.hypo = hypo
        self.labels = labels
        self.access_token = "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"
        #self.classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli", device=0)
        self.classifier = pipeline("zero-shot-classification", 
            model = AutoModelForSequenceClassification.from_pretrained("tuni/xlm-roberta-large-xnli-finetuned-mnli-SJP-v2", use_auth_token=self.access_token, num_labels=2, ignore_mismatched_sizes=True),
            device=0, 
            tokenizer = AutoTokenizer.from_pretrained("tuni/xlm-roberta-large-xnli-finetuned-mnli-SJP-v2", use_auth_token=self.access_token))
        self.dataset = load_dataset('swiss_judgment_prediction', language)
        self.counter = 1
        self.count = 0
        self.total = len(self.dataset[self.set])

        self.cantons = ['BE','AG', 'FR', 'GE', 'GL', 'GR', 'JU', 'LU', 'NE', 'SG', 'SH', 'SZ', 'SO', 'TG', 'TI', 'UR', 'VS', 'VD', 'ZG', 'ZH', 'AR', 'AI', 'BS', 'BL', 'OW', 'NW', 'CH', 'NA']
        self.legalAreas = ["penal", "social", "public", "civil"]

        self.be = self.ag = self.fr = self.ge = self.gl = self.gr = self.ju = self.lu = self.ne = self.sg = self.sh = self.sz = self.so = self.tg = self.ti = self.ur = self.vs = self.vd = self.zg = self.zh = self.ar = self.ai = 0
        self.bs = self.bl = self.ow = self.nw = self.ch = self.na = 0
        
        self.scorebe = self.scoreag = self.scorefr = self.scorege = self.scoregl = self.scoregr = self.scoreju = self.scorelu = self.scorene = self.scoresg = self.scoresh = self.scoreso = 0
        self.scoretg = self.scoreti = self.scoreur = self.scorevs = self.scorevd = self.scorezg = self.scorezh = self.scorear = self.scoreai = self.scorebs = self.scorebl = self.scoreow = 0
        self.scorenw = self.scorech = self.scorena = self.scoresz = 0
        
        #assert len(self.cantonAmounts) == len(self.cantonScores)

        self.penal = self.social = self.civil = self.public = 0

        self.scorepenal = self.scoresocial = self.scorecivil = self.scorepublic = 0
 
    def runRoberta(self):
        options = {'be': self.be,
                   'ag': self.ag,
                   'fr': self.fr,
                   'ge': self.ge,
                   'gl': self.gl,
                   'gr': self.gr,
                   'ju': self.ju,
                   'lu': self.lu,
                   'ne': self.ne,
                   'sg': self.sg,
                   'sh': self.sh,
                   'sz': self.sz,
                   'so': self.so,
                   'tg': self.tg,
                   'ti': self.ti,
                   'ur': self.ur,
                   'vs': self.vs,
                   'vd': self.vd,
                   'zg': self.zg,
                   'zh': self.zh,
                   'ar': self.ar,
                   'ai': self.ai,
                   'bs': self.bs,
                   'bl': self.bl,
                   'ow': self.ow,
                   'nw': self.nw,
                   'ch': self.ch,
                   'n/a': self.na,
                   }

        optionsLaw = {
            'penal law': self.penal,
            'social law': self.social,
            'public law': self.public,
            'civil law': self.civil,
        }

        optionsScore = {'be': self.scorebe,
                        'ag': self.scoreag,
                        'fr': self.scorefr,
                        'ge': self.scorege,
                        'gl': self.scoregl,
                        'gr': self.scoregr,
                        'ju': self.scoreju,
                        'lu': self.scorelu,
                        'ne': self.scorene,
                        'sg': self.scoresg,
                        'sh': self.scoresh,
                        'sz': self.scoresz,
                        'so': self.scoreso,
                        'tg': self.scoretg,
                        'ti': self.scoreti,
                        'ur': self.scoreur,
                        'vs': self.scorevs,
                        'vd': self.scorevd,
                        'zg': self.scorezg,
                        'zh': self.scorezh,
                        'ar': self.scorear,
                        'ai': self.scoreai,
                        'bs': self.scorebs,
                        'bl': self.scorebl,
                        'ow': self.scoreow,
                        'nw': self.scorenw,
                        'ch': self.scorech,
                        'n/a': self.scorena,
                        }

        optionsLawScore = {
            'penal law': self.scorepenal,
            'social law': self.scoresocial,
            'public law': self.scorepublic,
            'civil law': self.scorecivil,
        }

        #approved = Positive = 1
        #dismissed = Negative = 0

        # tp = true positives
        tp = 0
        # fp = false positves
        fp = 0
        # fn = false negatives
        fn = 0
        # tn = true negatives
        tn = 0

        labelList = list()
        predList = list()

        for data in self.dataset[self.set]:
            sequence = data['text']
            language = data['language']
            #candidate_labels = ['Approved', 'Dismissed']
            #hypothesis_template = "This case is {}."
            if language == 'de':
                #candidate_labels = ['genehmigt', 'abgelehnt']
                candidate_labels = self.labels
                hypothesis_template = self.hypo
                #print(f'Hypothesis: {hypothesis_template}')
            if language == 'fr':
                #candidate_labels = ['approuvé', 'refusé']
                candidate_labels = self.labels
                #hypothesis_template = "Ce cas est {}."
                hypothesis_template = self.hypo
                #print(f'Hypothesis: {hypothesis_template}')
            if language == 'it':
                candidate_labels = self.labels
                hypothesis_template = self.hypo
                #print(f'Hypothesis: {hypothesis_template}')

            # This block counts every element
            options[data['canton']] = options.get(data['canton']) + 1
            optionsLaw[data['legal area']] = optionsLaw.get(data['legal area']) + 1

            pred = self.classifier(sequence, candidate_labels,
                            hypothesis_template=hypothesis_template)
            #print(data['id'])
            #print(pred)

            self.counter += 1
            labelList.append(data['label'])

            if (pred['labels'][0] == "abgelehnt") or (pred['labels'][0] == "dismissed") or (pred['labels'][0] == "refusé") or (pred['labels'][0] == "respinto"):
                predList.append(0)
                if int(data['label']) == 0:
                    self.count += 1
                    optionsScore[data['canton']] = optionsScore.get(data['canton']) + 1
                    optionsLawScore[data['legal area']] = optionsLawScore.get(data['legal area']) + 1
                    tn += 1
                else:
                    fn += 1
            elif (pred['labels'][0] == "genehmigt") or (pred['labels'][0] == "approved") or (pred['labels'][0] == "approuvé") or (pred['labels'][0] == "approvato"):
                predList.append(1)
                if int(data['label']) == 1:
                    self.count += 1
                    optionsScore[data['canton']] = optionsScore.get(data['canton']) + 1
                    optionsLawScore[data['legal area']] = optionsLawScore.get(data['legal area']) + 1
                    tp += 1
                else:
                    fp += 1
            #print(pred['scores'])
            #print(pred['labels'])

        precision = tp/(tp+fp)
        recall = tp/(tp+fn)
        #fscore = 2 * (precision*recall) / (precision+recall)

        print("Roberta")

        # Score
        print(self.count)
        print(self.total)
        self.acc = self.count / self.total
        print(self.acc)

        print(f"True positives: {tp}")
        print(f"True negatives: {tn}")
        print(f"False positives: {fp}")
        print(f"False negatives: {fn}")

        #print(f"F1 score: {fscore}")
        #print(f"precision: {precision}")
        #print(f"recall: {recall}")
        self.skFScore = f1_score(labelList, predList, average='macro')
        print(f"Sklearn F1 score: {self.skFScore}")
        self.mcc = matthews_corrcoef(labelList, predList)
        print(f"sklearn mcc: {self.mcc}")
        self.skprecision, self.skrecall, self.skf1_macro, _ = precision_recall_fscore_support(
            labelList, predList, average='macro')
        print(f"Sklearn Precision: {self.skprecision}")
        print(f"Sklearn Recall: {self.skrecall}")
        print(f"Sklearn F1 macro: {self.skf1_macro}")

        print(confusion_matrix(labelList, predList))
        self.tn, self.fp, self.fn, self.tp = confusion_matrix(labelList, predList).ravel()
        print(tn, fp, fn, tp)
        #print(self.ti)
        self.cantonAmounts = list()
        self.cantonScores = list()
        self.legals = list()
        self.legalScores = list()
        for amount in options.values():
            self.cantonAmounts.append(amount)
        for scores in optionsScore.values():
            self.cantonScores.append(scores)
        for amount in optionsLaw.values():
            self.legals.append(amount)
        for scores in optionsLawScore.values():
            self.legalScores.append(scores)
        
        print(self.cantonAmounts)
        print(self.cantonScores)
        print(self.legals)
        print(self.legalScores)

    def getData(self):
        return 'Roberta', self.language, self.skf1_macro, self.mcc, self.acc, self.tn, self.fp, self.fn, self.tp

    def getCanton(self):
        cantonList = list()
        print(self.cantons)
        for i in range(len(self.cantons)):
            if(self.cantonAmounts[i] == 0):
                accuracy = 0
            else:
                accuracy = self.cantonScores[i] / self.cantonAmounts[i]
            cantonList.append(('Roberta', self.language, self.cantons[i], self.cantonScores[i], self.cantonAmounts[i], accuracy))
        print(cantonList)
        return cantonList

    def getLegals(self):
        legalsList = list()
        for i in range(len(self.legalAreas)):
            if(self.legals[i] == 0):
                accuracy = 0
            else:
                accuracy = self.legalScores[i] / self.legals[i]
            legalsList.append(('Roberta', self.language, self.legalAreas[i], self.legalScores[i], self.legals[i], accuracy))
        print(legalsList)
        return  legalsList