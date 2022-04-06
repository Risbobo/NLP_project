from datasets import load_dataset
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

set = 'validation'
dataset = load_dataset('swiss_judgment_prediction', 'all_languages')
count = 0
total = dataset[set]

for data in dataset[set]:
    sequence = data['text']
    language = data['language']
    candidate_labels = ['Approved', 'Dismissed']
    hypothesis_template = "This case is {}."
    if language == 'de':
        candidate_labels = ['genehmigt', 'abgelehnt']
        hypothesis_template = "Dieser Fall wurde {}."
    if language == 'fr':
        candidate_labels = ['approuvé', 'refusé']
        hypothesis_template = "Ce cas est {}."
    if language == 'it':
        candidate_labels = ['Approved', 'Dismissed']
        hypothesis_template = "This case is {}."

    pred = classifier(sequence, candidate_labels, hypothesis_template=hypothesis_template)
    score = pred['scores']
    decision = 1 if score[0] >= score[1] else 0
    if decision == data['label']:
        count += 1

# Score
print(count/total)

