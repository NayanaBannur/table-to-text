import numpy as np
import json

train_size = 200
dev_size = 10
train_papers = {}
dev_papers = {}
num_cols = 6
num_rows = 4
row_names = 'ABCD'

for i in range (train_size+dev_size):
    paper = {}
    paper["paper"] = ""
    paper["paper_id"] = ""
    paper["table_caption"]  = "Table"
    paper["table_column_names"] = ["Col"+str(i) for i in range (num_cols)]

    rows = []
    highest_cols = []
    for j in range (num_rows):
        perm = np.random.permutation(num_cols - 1)
        highest_cols.append("Col" + str(np.argmax(perm)+1))
        rows.append([row_names[j]] + [str(perm[k]) for k in range (len(perm))])

    paper["table_content_values"] = rows
    paper["text"] = ", ".join(highest_cols)
    if i < train_size:
        train_papers[str(i)] = paper
    else:
        dev_papers[str(i-train_size)] = paper

smallest = False
if smallest:
    for i in range (train_size+dev_size, 2*(train_size+dev_size)):
        paper = {}
        paper["paper"] = ""
        paper["paper_id"] = ""
        paper["table_caption"]  = "Table"
        paper["table_column_names"] = ["Col"+str(i) for i in range (num_cols)]

        rows = []
        for j in range(num_rows):
            rows.append(np.random.randint(100, 150, num_cols))

        rows[i%num_rows] = [x-np.random.randint(100, 150) for x in rows[i%num_rows]]

        for j in range(num_rows):
            rows[j] = [row_names[j]] + [str(rows[j][k]) for k in range (num_cols - 1)]

        paper["table_content_values"] = rows
        paper["text"] = f"{row_names[i%num_rows]} is the smallest."
        if i < 2*train_size+dev_size:
            train_papers[str(i)] = paper
        else:
            dev_papers[str(i-train_size)] = paper


with open('../data/train/few-shot/train.json', 'w') as fp:
    json.dump(train_papers, fp, indent = 4)

with open('../data/dev/few-shot/dev.json', 'w') as fp:
    json.dump(dev_papers, fp, indent = 4)
'''
with open('train.json', 'w') as fp:
    json.dump(train_papers, fp, indent = 4)

with open('dev.json', 'w') as fp:
    json.dump(dev_papers, fp, indent = 4)
'''

