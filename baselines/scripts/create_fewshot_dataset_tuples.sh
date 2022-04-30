python3 convert_json_files_tuples.py -d ../dataset/train/few-shot/ -f train_filtered.json -s train
python3 convert_json_files_tuples.py -d ../dataset/dev/few-shot/ -f dev_filtered.json -s dev
python3 convert_json_files_tuples.py -d ../dataset/test/ -f test-CL.json -s test_CL
python3 convert_json_files_tuples.py -d ../dataset/test/ -f test-Other.json -s test_other
