import numpy as np
import json
import copy

train_size_per_rule = [400, 400, 400, 2000]
dev_size_per_rule = [20, 20, 20, 100]

train_papers = {}
dev_papers = {}

num_cols_min = 3
num_cols_max = 5
num_rows_min = 2
num_rows_max = 3

min_num = 0
max_num = 100

train_count = 0
dev_count = 0

rules = ['largest', 'smallest', 'similar', 'diff']

np.random.seed(0)


def one_row_largest(datum):
    selected_row = np.random.choice(range(datum["num_rows"]))
    data = np.random.uniform(min_num, max_num, (datum["num_rows"], datum["num_cols"]))
    idx = data.argmax(axis=0)
    t = copy.deepcopy(data[selected_row,:])
    data[selected_row,:] = data.max(axis=0)
    data[idx, range(datum["num_cols"])] = t
    data = np.round(data, 3)
    data = [
        [datum["table_row_names"][i]] + 
        [str(data[i][j]) for j in range(data.shape[1])] for i in range(data.shape[0])
    ]
    datum["table_content_values"] = data
    datum["text"] = datum["table_row_names"][selected_row] + " is the largest." 

    return datum

def one_row_smallest(datum):
    selected_row = np.random.choice(range(datum["num_rows"]))
    data = np.random.uniform(min_num, max_num, (datum["num_rows"], datum["num_cols"]))
    idx = data.argmin(axis=0)
    t = copy.deepcopy(data[selected_row,:])
    data[selected_row,:] = data.min(axis=0)
    data[idx, range(datum["num_cols"])] = t
    data = np.round(data, 3)
    data = [
        [datum["table_row_names"][i]] + 
        [str(data[i][j]) for j in range(data.shape[1])] for i in range(data.shape[0])
    ]
    datum["table_content_values"] = data
    datum["text"] = datum["table_row_names"][selected_row] + " is the smallest." 

    return datum

def one_col_largest(datum):
    selected_col = np.random.choice(range(datum["num_cols"]))
    data = np.random.uniform(min_num, max_num, (datum["num_rows"], datum["num_cols"]))
    idx = data.argmax(axis=1)
    t = copy.deepcopy(data[:, selected_col])
    data[:, selected_col] = data.max(axis=1)
    data[range(datum["num_rows"]), idx] = t
    data = np.round(data, 3)
    data = [
        [datum["table_row_names"][i]] + 
        [str(data[i][j]) for j in range(data.shape[1])] for i in range(data.shape[0])
    ]
    datum["table_content_values"] = data
    datum["text"] = datum["table_column_names"][selected_col+1] + " is the largest." 

    return datum

def one_col_smallest(datum):
    selected_col = np.random.choice(range(datum["num_cols"]))
    data = np.random.uniform(min_num, max_num, (datum["num_rows"], datum["num_cols"]))
    idx = data.argmin(axis=1)
    t = copy.deepcopy(data[:, selected_col])
    data[:, selected_col] = data.min(axis=1)
    data[range(datum["num_rows"]), idx] = t
    data = np.round(data, 3)
    data = [
        [datum["table_row_names"][i]] + 
        [str(data[i][j]) for j in range(data.shape[1])] for i in range(data.shape[0])
    ]
    datum["table_content_values"] = data
    datum["text"] = datum["table_column_names"][selected_col+1] + " is the smallest." 

    return datum

def rows_similar(datum):
    selected_rows = np.random.choice(range(datum["num_rows"]), 2, replace=False)
    data = np.random.uniform(min_num, max_num, (datum["num_rows"], datum["num_cols"]))
    data[selected_rows[0], :] = np.random.normal(data[selected_rows[1], :], scale=0.01)
    data = np.clip(data, min_num, max_num)
    data = np.round(data, 3)
    data = [
        [datum["table_row_names"][i]] + 
        [str(data[i][j]) for j in range(data.shape[1])] for i in range(data.shape[0])
    ]
    datum["table_content_values"] = data
    first = min(selected_rows)
    second = max(selected_rows)
    datum["text"] = datum["table_row_names"][first] + " and " + datum["table_row_names"][second] + " are similar."

    return datum

def cols_similar(datum):
    selected_cols = np.random.choice(range(datum["num_cols"]), 2, replace=False)
    data = np.random.uniform(min_num, max_num, (datum["num_rows"], datum["num_cols"]))
    data[:, selected_cols[0]] = np.random.normal(data[:, selected_cols[1]], scale=0.01)
    data = np.clip(data, min_num, max_num)
    data = np.round(data, 3)
    data = [
        [datum["table_row_names"][i]] + 
        [str(data[i][j]) for j in range(data.shape[1])] for i in range(data.shape[0])
    ]
    datum["table_content_values"] = data
    first = min(selected_cols)
    second = max(selected_cols)
    datum["text"] = datum["table_column_names"][first+1] + " and " + datum["table_column_names"][second+1] + " are similar."

    return datum

def rows_comp(datum):
    selected_rows = np.random.choice(range(datum["num_rows"]), 2, replace=False)
    selected_col = np.random.choice(range(datum["num_cols"]))
    
    first_rh, second_rh = datum["table_row_names"][selected_rows[0]], datum["table_row_names"][selected_rows[1]]
    col_name = datum["table_column_names"][selected_col+1]
    datum["table_caption"] = f"Table shows {first_rh} and {second_rh} given {col_name}"

    data = np.random.uniform(min_num, max_num, (datum["num_rows"], datum["num_cols"]))
    data = np.round(data, 3)
    first, second = data[selected_rows[0], selected_col], data[selected_rows[1], selected_col]
    data = [
        [datum["table_row_names"][i]] + 
        [str(data[i][j]) for j in range(data.shape[1])] for i in range(data.shape[0])
    ]
    datum["table_content_values"] = data

    diff = int(np.round(np.abs(first-second)))
    if first < second:
        datum["text"] = f"{second_rh} is around {diff} greater than {first_rh} given {col_name}"
    else:
        datum["text"] = f"{first_rh} is around {diff} greater than {second_rh} given {col_name}"

    return datum

def cols_comp(datum):
    selected_cols = np.random.choice(range(datum["num_cols"]), 2, replace=False)
    selected_row = np.random.choice(range(datum["num_rows"]))
    
    first_ch, second_ch = datum["table_column_names"][selected_cols[0]+1], datum["table_column_names"][selected_cols[1]+1]
    row_name = datum["table_row_names"][selected_row]
    datum["table_caption"] = f"Table shows {first_ch} and {second_ch} given {row_name}"

    data = np.random.uniform(min_num, max_num, (datum["num_rows"], datum["num_cols"]))
    data = np.round(data, 3)
    first, second = data[selected_row, selected_cols[0]], data[selected_row, selected_cols[1]]
    data = [
        [datum["table_row_names"][i]] + 
        [str(data[i][j]) for j in range(data.shape[1])] for i in range(data.shape[0])
    ]
    datum["table_content_values"] = data

    diff = int(np.round(np.abs(first-second)))
    if first < second:
        datum["text"] = f"{second_ch} is around {diff} greater than {first_ch} given {row_name}"
    else:
        datum["text"] = f"{first_ch} is around {diff} greater than {second_ch} given {row_name}"

    return datum


def create_datum(rule, dim):
    datum = {}
    datum["paper"] = ""
    datum["paper_id"] = ""
    datum["table_caption"] = "Table"

    num_cols = np.random.randint(num_cols_min, num_cols_max+1)
    num_rows = np.random.randint(num_rows_min, num_rows_max+1)

    datum["num_rows"] = num_rows
    datum["num_cols"] = num_cols

    datum["table_column_names"] = ["Col" + str(i) for i in range(num_cols+1)]
    datum["table_row_names"] = ["Row" + str(i) for i in range(num_rows)]
    
    if rule == "largest" and dim == "col":
        datum = one_col_largest(datum)
    elif rule == "largest" and dim == "row":
        datum = one_row_largest(datum)
    elif rule == "smallest" and dim == "col":
        datum = one_col_smallest(datum)
    elif rule == "smallest" and dim == "row":
        datum = one_row_smallest(datum)
    elif rule == "similar" and dim == "row":
        datum = rows_similar(datum)
    elif rule == "similar" and dim == "col":
        datum = cols_similar(datum)
    elif rule == "diff" and dim == "row":
        datum = rows_comp(datum)
    elif rule == "diff" and dim == "col":
        datum = cols_comp(datum)

    del datum["table_row_names"]
    del datum["num_rows"]
    del datum["num_cols"]

    return datum
    

for i, rule in enumerate(rules):
    for j in range(train_size_per_rule[i]):
        dim = "col"
        if j < train_size_per_rule[i] / 2:
            dim = "row"

        train_papers[train_count] = create_datum(rule, dim)
        train_count += 1

    for j in range(dev_size_per_rule[i]):
        dim = "col"
        if j < dev_size_per_rule[i] / 2:
            dim = "row"

        dev_papers[dev_count] = create_datum(rule, dim)
        dev_count += 1


with open('../dataset/pretrain/train.json', 'w') as fp:
    json.dump(train_papers, fp, indent=4)

with open('../dataset/pretrain/dev.json', 'w') as fp:
    json.dump(dev_papers, fp, indent=4)
