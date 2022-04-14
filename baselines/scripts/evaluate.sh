# BART val 
# python3 evaluate.py -p results/20220317_200809/validation_predictions_17.txt -s results/20220317_200809/validation_targets_17.txt --all True
# T5 val
# python3 evaluate.py -p results/20220316_203525/validation_predictions_18.txt -s results/20220316_203525/validation_targets_18.txt --all True
# BART test CL
python3 evaluate.py -p results/20220317_200809/test_predictions_CL_0.txt -s results/20220317_200809/test_targets_CL_0.txt --all True
# BART test other
python3 evaluate.py -p results/20220317_200809/test_predictions_other_0.txt -s results/20220317_200809/test_targets_other_0.txt --all True
# BART test CL zero-shot
python3 evaluate.py -p results/20220317_231119/test_predictions_CL_0.txt -s results/20220317_231119/test_targets_CL_0.txt --all True
# BART test other zero-shot
python3 evaluate.py -p results/20220318_000415/test_predictions_other_0.txt -s results/20220318_000415/test_targets_other_0.txt --all True
# BART test CL captions only
python3 evaluate.py -p results/20220318_012143/test_predictions_CL_0.txt -s results/20220318_012143/test_targets_CL_0.txt --all True
# BART test other captions only
python3 evaluate.py -p results/20220318_012143/test_predictions_other_0.txt -s results/20220318_012143/test_targets_other_0.txt --all True
# BART test CL table only
python3 evaluate.py -p results/20220318_030910/test_predictions_CL_0.txt -s results/20220318_030910/test_targets_CL_0.txt --all True
# BART test other table only
python3 evaluate.py -p results/20220318_030910/test_predictions_other_0.txt -s results/20220318_030910/test_targets_other_0.txt --all True
# T5 test CL
python3 evaluate.py -p results/20220318_060908/test_predictions_CL_0.txt -s results/20220318_060908/test_targets_CL_0.txt --all True
# T5 test other
python3 evaluate.py -p results/20220318_060908/test_predictions_other_0.txt -s results/20220318_060908/test_targets_other_0.txt --all True
# T5 test CL captions only
# python3 evaluate.py -p results/20220315_172821/test_predictions_0.txt -s results/20220315_172821/test_targets_0.txt --all True
# T5 test other captions only
# python3 evaluate.py -p results/20220315_172821/test_predictions_0_other.txt -s results/20220315_172821/test_targets_0_other.txt --all True
# T5 test CL table only
# python3 evaluate.py -p results/20220315_172821/test_predictions_0.txt -s results/20220315_172821/test_targets_0.txt --all True
# T5 test other table only
# python3 evaluate.py -p results/20220315_172821/test_predictions_0_other.txt -s results/20220315_172821/test_targets_0_other.txt --all True
