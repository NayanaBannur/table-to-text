python train_table2text_bart.py \
--data_dir=./ \
--model_name_or_path=bart-large \
--learning_rate=3e-5 \
--num_train_epochs 30 \
--train_batch_size=2 \
--eval_batch_size=2 \
--test_batch_size=2 \
--n_gpu 1 \
--do_predict \
--test_type='other' \
--output_dir='./results/20220318_012143/' \
--early_stopping_patience 10 \
--max_source_length 152 \
--max_target_length 384 \