import time
import numpy as np
from datasets import load_dataset, load_metric
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer

# classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

size_few_shot = 10
dataset = load_dataset('swiss_judgment_prediction', 'all_languages')

tokenizer = AutoTokenizer.from_pretrained('joeddav/xlm-roberta-large-xnli')

model = AutoModelForSequenceClassification.from_pretrained("joeddav/xlm-roberta-large-xnli")


def label_hypo(example):
    language = example['language']
    if language == 'de':
        label = 'genehmigt' if example['label'] == 1 else 'abgelehnt'
        return f"Dieser Fall wurde {label}."
    elif language == 'fr':
        label = 'approuvé' if example['label'] == 1 else 'refusé'
        return f"Ce cas est {label}."
    elif language == 'it':
        label = 'approved' if example['label'] == 1 else 'refused'
        return f"This case is {label}."
    else :
        label = 'approved' if example['label'] == 1 else 'refused'
        return f"This case is {label}."


def tokenize_function(examples):
    premise = examples['text']
    labels = label_hypo(examples)
    return tokenizer(premise, labels, return_tensors='pt', truncation='only_first')


def tokenize_set(dataset):
    return dataset.map(tokenize_function)


tokenized_train = tokenize_set(dataset['train'])
tokenized_test = tokenize_set(dataset['test'])

small_train_dataset = tokenized_train.shuffle(seed=42).select(range(size_few_shot))
small_eval_dataset = tokenized_test.shuffle(seed=42).select(range(size_few_shot))

training_args = TrainingArguments(output_dir="test_trainer")
metric = load_metric('f1')


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=small_train_dataset,
    eval_dataset=small_eval_dataset,
    compute_metrics=compute_metrics,
)

print('Training begins')
tic = time.perf_counter()
trainer.train()
toc = time.perf_counter()
print(f"training for size {size_few_shot} in {toc - tic:0.2f} seconds")
