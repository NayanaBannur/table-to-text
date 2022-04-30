python3 convert_json_files.py -d ../dataset/train/few-shot/ -f train.json -s train -m both
python3 convert_json_files.py -d ../dataset/development/few-shot/ -f dev.json -s dev -m both
python3 convert_json_files.py -d ../dataset/test/ -f test-CL.json -s test_CL -m both
python3 convert_json_files.py -d ../dataset/test/ -f test-Other.json -s test_other -m both
