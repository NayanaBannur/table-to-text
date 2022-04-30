import torch
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import sys
import json
from tqdm import tqdm
import re

plt.rcParams['figure.figsize'] = [100, 60]

from adjustText import adjust_text

from transformers import BartTokenizer, BartForConditionalGeneration

import logging
logging.basicConfig(level=logging.INFO)

model_path = 'facebook/bart-large'

# Load BART.
model = BartForConditionalGeneration.from_pretrained(model_path)
# Set the model to eval mode.
model.eval()
# This notebook assumes CPU execution. If you want to use GPUs, put the model on cuda and modify subsequent code blocks.
#model.to('cuda')
# Load tokenizer.
tokenizer = BartTokenizer.from_pretrained(model_path)

# tokenizer.save_vocabulary(save_directory='.')

wordembs = model.get_input_embeddings()

print("Vocab size")
print(model.config.vocab_size)

# Convert the vocabulary embeddings to numpy.
allinds = np.arange(0,model.config.vocab_size,1)
inputinds = torch.LongTensor(allinds)
bartwordembs = wordembs(inputinds).detach().numpy()

print("Embed shape")
print(bartwordembs.shape)

def loadLines(filename):
    print("Loading lines from file", filename)
    f = open(filename,'r')
    vocab = json.load(f)
    lines = np.array([])
    indices = []
    for line in tqdm(vocab):
        if bool(re.search(r'\d', line)):
            indices.append(vocab[line])
        lines = np.append(lines, line.rstrip())
        # if len(indices)>100:
        #     break
    print("Done. ", len(lines)," lines loaded!")
    return lines, indices

bartwords, indices = loadLines('vocab.json')
print(indices)

print("Words shape")
print(bartwords.shape)

# Determine vocabulary to use for t-SNE/visualization. The indices are hard-coded based partially on inspection:
# bart_char_indices_to_use = np.arange(999, 1063, 1)
# bart_voc_indices_to_plot = np.append(bart_char_indices_to_use, np.arange(1996, 5932, 1))
# bart_voc_indices_to_use = np.append(bart_char_indices_to_use, np.arange(1996, 11932, 1))

bart_voc_indices_to_plot = np.array(indices)
bart_voc_indices_to_use = np.array(indices)

print(len(bart_voc_indices_to_plot))
print(len(bart_voc_indices_to_use))

print(bartwords[bart_voc_indices_to_use])

bart_voc_indices_to_use_tensor = torch.LongTensor(bart_voc_indices_to_use)
bart_word_embs_to_use = wordembs(bart_voc_indices_to_use_tensor).detach().numpy()

# Run t-SNE on the BART vocabulary embeddings we selected:
mytsne_words = TSNE(n_components=2,early_exaggeration=12,verbose=2,metric='cosine',init='pca',n_iter=2500)
bart_word_embs_to_use_tsne = mytsne_words.fit_transform(bart_word_embs_to_use)

bart_words_to_plot = bartwords[bart_voc_indices_to_plot]
print(len(bart_words_to_plot))

# Plot the transformed BART vocabulary embeddings:
fig = plt.figure()
alltexts = list()
for i, txt in enumerate(bart_words_to_plot):
    plt.scatter(bart_word_embs_to_use_tsne[i,0], bart_word_embs_to_use_tsne[i,1], s=10)
    currtext = plt.text(bart_word_embs_to_use_tsne[i,0], bart_word_embs_to_use_tsne[i,1], 
        txt, family='sans-serif', fontsize=25)
    alltexts.append(currtext)
    

# Save the plot before adjusting.
plt.savefig('viz-bart-voc-tsne10k-viz4k-noadj.pdf', format='pdf', bbox_inches="tight")
print('now running adjust_text')
# Using autoalign often works better in my experience, but it can be very slow for this case, so it's false by default below:
#numiters = adjust_text(alltexts, autoalign=True, lim=50)
numiters = adjust_text(alltexts, autoalign=False, lim=50)
print('done adjust text, num iterations: ', numiters)
plt.savefig('viz-bart-voc-tsne10k-viz4k-adj50.pdf', format='pdf', bbox_inches="tight")
