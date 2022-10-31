# Bias Measurement
For a detailed description of our project and results see our [Final Report](Project_Report.pdf).

## Project Description

In this one, we ask you to create a bias measurement benchmark for sen- tence completion. Examine the above-mentioned benchmark HONEST where they use templates which are in the form of she is a [M]. and compare these to he is a [M]. while looking for hurtful completions. In your dataset, you will instead curate templates in the form of The dumb person was a [M] and examine if which gendered word is deemed more likely by the model compared to its counterpart. The number of tem- plates should be at least 1000 (the more the merrier). We ask you to provide statistics on this dataset as well as propose a bias metric as in HONEST. Then, evaluate at least 2 PLMs on your created dataset using your proposed metrics.

## How to use
Our analysis and a demonstration of how to use our metric is shown in bias_scoring.ipynb. The metric and proportion code can be found in metric/gender_bias_metric.py. The code for creation of templates is in templates.ipynb. The final templates are in templates.csv.

## Resources
* [Hugging Face Gender Words](https://huggingface.co/datasets/md_gender_bias)
* [Honest Measurement Paper](https://dnozza.github.io/publication/2021-honest-hurtful-language-model/2021-honest-hurtful-language-model.pdf)
* [Honest Templates](https://github.com/MilaNLProc/honest/blob/main/resources/en_template.tsv)
* [Honest Measurement Code](https://github.com/MilaNLProc/honest)
