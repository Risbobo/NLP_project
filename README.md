# NLP_project

## Zero-shot

## Few-shots

We didn't manage to make the few-shots works. With the zero-shot, the APIs available on hugginface are really straightforward and with examples, but there is a lot less available for fine-tuning. We tried to use https://huggingface.co/docs/transformers/training#trainer to set-up the few-shot model, following this post (https://discuss.huggingface.co/t/new-pipeline-for-zero-shot-text-classification/681/15) and this blog post (https://joeddav.github.io/blog/2020/05/29/ZSL.html) to adapt it to our task, but with no success. We think the problem is in the format of the task ; the example for the fine-tuning is a classic inference with a text and the corresponding label (such as emotion classification) but our task asks for a premise, a hypothesis and a label. 
