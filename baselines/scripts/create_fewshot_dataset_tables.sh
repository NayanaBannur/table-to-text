python3 convert_json_files.py -f ../dataset/train/few-shot/train.json -s train -t True
python3 convert_json_files.py -f ../dataset/development/few-shot/dev.json -s dev -t True
python3 convert_json_files.py -f ../dataset/test/test-CL.json -s test_CL -t True
python3 convert_json_files.py -f ../dataset/test/test-Other.json -s test_other -t True
