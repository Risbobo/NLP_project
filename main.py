from datasets import load_dataset
from transformers import pipeline

classifier = pipeline("zero-shot-classification",model="facebook/bart-large-mnli")

dataset = load_dataset('swiss_judgment_prediction', 'all_languages')
print(dataset)
sequence = dataset['train']['text'][0]
candidate_labels = ['Approved', 'Dismissed']

#sequence = "I like to party and read books"
#candidate_labels = ['Drink', 'Travel', 'Reading', 'Sleeping']

test = classifier(sequence, candidate_labels)

print(test['scores'])