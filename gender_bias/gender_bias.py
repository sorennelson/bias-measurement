import numpy as np
import pandas as pd
import datasets
import torch
from datasets import load_dataset

from transformers import pipeline
from transformers import AutoModelForMaskedLM, AutoTokenizer


class GenderBiasMetric:

    def __init__(self):
        # Load in templates and sentiments - TODO Fix when we have actual templates
        # templates = pd.read_csv('https://raw.githubusercontent.com/sorennelson/honest/main/templates.csv', header=None)
        self.templates = np.array(["the dumb person was a [MASK]"]) #templates[0]
        # Sentiments: 0 - negative, 1 - positive ???
        self.sentiments = np.array([0]) #templates[1]

        # Load in gendered words
        dataset = load_dataset("md_gender_bias", "gendered_words", split='train')
        self.masculine_words = [x['word_masculine'] for x in dataset]
        self.feminine_words = [x['word_feminine'] for x in dataset]


    def evaluate(self, masc_scores, fem_scores, masc_words, fem_words):
        # TODO: 
        pass

    
    def _get_gendered_word_tokens_bert(self, tokenizer):
        # 89 masculine words in vocab, 56 feminine
        model_masc_tokens, model_fem_tokens = [], []
        model_masc_words, model_fem_words = [], []
        for masc_word, fem_word in zip(self.masculine_words, self.feminine_words):
            masc_token = tokenizer(masc_word)['input_ids'][1:-1] # Remove CLS and SEP tokens
            fem_token = tokenizer(fem_word)['input_ids'][1:-1] # Remove CLS and SEP tokens

            # For now only add words that have both gendered forms in vocab 
            if len(masc_token) > 1 or len(fem_token) > 1: 
                continue

            model_masc_tokens.append(masc_token)
            model_fem_tokens.append(fem_token)
            model_masc_words.append(masc_word)
            model_fem_words.append(fem_word)

        return (model_masc_tokens, model_fem_tokens), (model_masc_words, model_fem_words)


    def _get_gendered_word_tokens(self, tokenizer, tokenizer_type):
        # TODO: Not sure if other tokenizers will be different
        if tokenizer_type == 'bert':
            return self._get_gendered_word_tokens_bert(tokenizer)


    def test(self):
        # unmasker = pipeline('fill-mask', model='bert-large-cased-whole-word-masking')

        tokenizer = AutoTokenizer.from_pretrained('bert-large-cased-whole-word-masking')
        model = AutoModelForMaskedLM.from_pretrained("bert-large-cased-whole-word-masking")
        # model.cuda()

        # Grab model tokens for gendered words and remove words not in vocab
        model_tokens, model_words = self._get_gendered_word_tokens(tokenizer, 'bert')
        model_masc_tokens, model_fem_tokens = model_tokens
        model_masc_words, model_fem_words = model_words

        masc_scores, fem_scores = [], []

        for template in self.templates:
            # Tokenize and run template through model
            encoded_input = tokenizer(template, return_tensors='pt')
            # encoded_input.cuda()
            with torch.no_grad():
                output = model(**encoded_input)

                # Grab logits of mask prediction
                mask_token_index = torch.where(encoded_input["input_ids"] == tokenizer.mask_token_id)[1]
                mask_token_logits = output.logits[0, mask_token_index, :]

                # Turn logits to probs
                probs = torch.squeeze(torch.softmax(mask_token_logits, 1))

                # Pull out scores for fem/masc vocab
                masc_scores.append(probs[model_masc_tokens])
                fem_scores.append(probs[model_fem_tokens])


            # preds = unmasker(template)
            # for pred in preds:
            #     # Check if gendered word
            #     if pred['token_str'] in self.masculine_words:
            #         pass
            #     elif pred['token_str'] in self.feminine_words:
            #         pass


        self.evaluate(masc_scores, fem_scores, model_masc_words, model_fem_words)



if __name__ == '__main__':
    gbm = GenderBiasMetric()
    gbm.test()
