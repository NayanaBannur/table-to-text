from argparse import ArgumentParser
import json
import os

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument("-d", "--data_dir", help="Data dir", required=True)
    parser.add_argument("-f", "--file", help="Input", required=True)
    parser.add_argument("-s", "--split", help="Specify the corresponding split (train, dev, or test)", required=True)
    parser.add_argument("-l", "--low", help="lower number of rows in table", required=False, default=2)
    parser.add_argument("-u", "--high", help="upper number of rows in table", required=False, default=2)

    args = parser.parse_args()
    file = os.path.join(args.data_dir, args.file)
    outfile = os.path.join(args.data_dir, f'{args.split}_filtered.json')
    low, high = args.low, args.high

    filtered = {}

    num_rows_list = []

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for idx, d in data.items():
            num_rows = len(d['table_content_values'])
            if low <= num_rows <= high:
                d["num_rows"] = num_rows
                filtered[idx] = d

    print(len(filtered))
    with open(outfile, 'w', encoding='utf-8') as f:
        json.dump(filtered, f, indent=4)
