from argparse import ArgumentParser
import json
import os
import itertools
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument("-d", "--data_dir", help="Data dir", required=True)
    parser.add_argument("-f", "--file", help="The SciGen json file to be converted for pre-trained models' input format",
                        required=True)
    parser.add_argument("-s", "--split", help="Specify the corresponding split, i.e., train, dev, or test",
                        required=True)
    parser.add_argument("-r", "--remove_tags", help="Remove tags", type=bool, default=False, required=False)

    args = parser.parse_args()
    file = os.path.join(args.data_dir, args.file)
    out = args.split
    remove_tags = args.remove_tags

    cell_separator = '<C>'
    caption_separator = '<CAP>'

    source_lens = []

    with open(file, 'r', encoding='utf-8') as f:
        with open('{}.source'.format(out), 'w', encoding='utf-8') as source:
            with open('{}.target'.format(out), 'w', encoding='utf-8') as target:
                data = json.load(f)
                for d in data:
                    num_cols = len(data[d]['table_column_names'])
                    num_rows = len(data[d]['table_content_values'])
                    if num_rows <= 1000:
                        text = cell_separator + ' '
                        for i, j in itertools.product(range(1, num_cols), range(num_rows)):
                            text += data[d]['table_column_names'][i] \
                                    + ' ' + data[d]['table_content_values'][j][0] \
                                    + ' ' + data[d]['table_content_values'][j][i]
                            text += ' ' + cell_separator + ' '
                        text = text[:-3]  # Remove last cell separator
                        text += ' ' + caption_separator + ' ' + data[d]['table_caption'] + '\n'

                        if args.remove_tags:
                            for tag in ['[BOLD]', '[EMPTY]', '[CONTINUE]', '[ITALIC]', '<bold>', '</bold>', '<italic>', '</italic>']:
                                text = text.replace(tag, '')

                        source.write(text)

                        source_lens.append(len(text.split(' ')))

                        descp = data[d]['text'].replace('[CONTINUE]', '') + '\n'
                        target.write(descp)

    # print(min(source_lens))
    # print(max(source_lens))
    # print(np.mean(source_lens))
    # plt.hist(source_lens)
    # plt.show()
