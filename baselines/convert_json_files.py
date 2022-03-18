from argparse import ArgumentParser
import json


if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument("-f", "--file", help="The SciGen json file to be converted for pretrained models' input format", required=True)
    parser.add_argument("-s", "--split", help="Specify the corresponding split, i.e., train, dev, or test", required=True)
    parser.add_argument("-c", "--caption-only", help="Create dataset from only captions", type=bool, default=False, required=False)
    parser.add_argument("-t", "--table_only", help="Create dataset from only table", type=bool, default=False, required=False)
    parser.add_argument("-r", "--remove_tags", help="Remove tags", type=bool, default=False, required=False)

    args = parser.parse_args()
    file = args.file
    out = args.split
    caption_only = args.caption_only
    table_only = args.table_only
    remove_tags = args.remove_tags

    row_seperator = '<R>'
    cell_separator = '<C>'
    caption_separator = '<CAP>'

    with open(file, 'r', encoding='utf-8') as f:
        with open('{}.source'.format(out), 'w', encoding='utf-8') as source:
            with open('{}.target'.format(out), 'w', encoding='utf-8') as target:
                data = json.load(f)
                for d in data:
                    if not args.caption_only:
                        text = row_seperator + ' ' + cell_separator
                        row_len = len(data[d]['table_column_names'])
                        for i,c in enumerate(data[d]['table_column_names']):
                            text += ' ' + c
                            if i < row_len-1: 
                                text += ' ' + cell_separator

                        for row in data[d]['table_content_values']:
                            text += ' ' + row_seperator + ' ' + cell_separator
                            for i, c in enumerate(row):
                                text += ' ' + c
                                if i < row_len -1:
                                    text += ' ' + cell_separator

                        if not args.table_only:    
                            text += ' ' + caption_separator + ' ' +data[d]['table_caption'] + '\n'
                        else:
                            text += '\n'

                    else:
                        text = data[d]['table_caption'] + '\n'
                    
                    if args.remove_tags:
                        for tag in ['[BOLD]', '[EMPTY]', '[CONTINUE]', '[ITALIC]', '<bold>', '</bold>', '<italic>', '</italic>']:
                            text = text.replace(tag, '')

                    source.write(text)
                    
                    descp = data[d]['text'].replace('[CONTINUE]', '') + '\n'
                    target.write(descp)





