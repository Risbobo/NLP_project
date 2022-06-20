How to use Zero-shot models on the swiss_judgment_prediction dataset:

On ubelix:
    For Roberta model: copy and paste the files "roberta.py", "testRoberta.py", "roberta.sh" in your ubelix storage
    Then you can run the zero shot model on the dataset with the command: sbatch roberta.sh
    There will be 12 csv files as output.
    For example: "dfCantonsRobertaTestRun3EngHypo.csv"
    This file shows the prediction scores and accuracy for every canton. That means if a canton has a high accuracy the model performs better court decisions for that canton.
    "TestRun3": We have experimented with 3 Hypothesis and TestRun3 means that we used the 3rd hypothesis for this model.
    "EngHypo": means that we used the english version of the hypothesis. The "Normal" version is the original version of the hypothesis. Meaning we have for every language (de,fr,it) hypotheses in their respective language. "EngLabel" means that we used english labels. "EngHypoLabel" means that hypotheses and labels are in english
    "dfLegalsRobertaTestRun..." shows the scores for the 4 legal areas.
    "dfRobertaTestRun..." shows more metrics like: mcc, macro f1 score from sklearn (skf1), true/false negatives/positives


    For Mdeberta model: copy and paste the files "mdeberta.py", "testMdeberta.py", "test_model_job.sh" in your ubelix storage
    Then you can run the zero shot model on the dataset with the command: test_model_job.sh


    For Bart model: copy and paste the files "bart.py", "testBart.py", "bart.sh" in your ubelix storage
    Then you can run the zero shot model on the dataset with the command: bart.sh