#!/usr/bin/env bash
file_name=$1
vec_dim=$2
vec_dim_dm=$((vec_dim/2))
vec_dim_dbow=$((vec_dim/2))
conda init
conda activate nlp-proj-36
python ./paragraphvec/train.py start --data_file_name "${file_name}.csv" \
--num_epochs 3 --batch_size 32 --num_noise_words 2 \
--vec_dim $vec_dim_dbow --lr 1e-3
python ./paragraphvec/train.py start --data_file_name "${file_name}.csv" \
--num_epochs 3 --batch_size 32 --num_noise_words 2 \
--vec_dim $vec_dim_dm --lr 1e-3 --model_ver dm --context_size 10
python ./paragraphvec/export_vectors.py start --data_file_name "${file_name}.csv" \
--model_file_name "${file_name}_model.dbow_vecdim.${vec_dim_dbow}_intermediate.tar"
python ./paragraphvec/export_vectors.py start --data_file_name "${file_name}.csv" \
--model_file_name "${file_name}_model.dm_vecdim.${vec_dim_dm}_intermediate.tar"