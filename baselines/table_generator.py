import numpy as np
import json

train_size = 200
dev_size = 10
train_papers = {}
dev_papers = {}
num_cols = 6 

for i in range (train_size+dev_size):
    paper = {}
    paper["paper"] = ""
    paper["paper_id"] = ""
    paper["table_caption"]  = "Table"
    paper["table_column_names"] = ["Col"+str(i) for i in range (num_cols)]
    difference = np.random.randint(0, 10)
    A = np.random.randint(0, 10, num_cols)
    '''
    if (i % 2 == 0):
        B = np.random.random(num_cols) * 10 + 10
        C = np.random.random(num_cols) * 10 + 20
    if (i % 2 == 1):
        B = np.random.random(num_cols) * 10 + 20
        C = np.random.random(num_cols) * 10 + 10
    '''
    B = np.random.randint(10, 20, num_cols)
    C = B + difference

    A = ['A'] + [str(round(A[i], 4)) for i in range (num_cols - 1)]
    B = ['B'] + [str(round(B[i], 4)) for i in range (num_cols - 1)] 
    C = ['C'] + [str(round(C[i], 4)) for i in range (num_cols - 1)]

    paper["table_content_values"] = [A, B, C]
    '''
    if (i % 2 == 0):
        paper["text"] = "C is larger than B"
    else:
        paper["text"] = "B is larger than C"
    '''
    paper["text"] = "C is " + str(difference) + " larger than B"
    if i < train_size:
        train_papers[str(i)] = paper
    else:
        dev_papers[str(i-train_size)] = paper

with open('train.json', 'w') as fp:
    json.dump(train_papers, fp, indent = 4)

with open('dev.json', 'w') as fp:
    json.dump(dev_papers, fp, indent = 4)
