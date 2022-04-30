# BART original val
python3 evaluate.py -p results/bart/validation_predictions_17.txt -s results/bart/validation_targets_17.txt --all True
# BART concat val 384
python3 evaluate.py -p results/bart_concat_384/validation_predictions_19.txt -s results/bart_concat_384/validation_targets_19.txt --all True
# BART concat val 768
python3 evaluate.py -p results/bart_concat_768/validation_predictions_14.txt -s results/bart_concat_768/validation_targets_14.txt --all True
# BART tuples val
python3 evaluate.py -p results/bart_tuples/validation_predictions_9.txt -s results/bart_tuples/validation_targets_9.txt --all True

