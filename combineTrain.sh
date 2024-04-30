#!/usr/bin/env bash
file_name=$1
vec_dim=$2
dataset=$3
epoch=$4
for ((i=10; i+10<=vec_dim; i+=10))
do
  vec_dim_dbow=$((i))
  vec_dim_dm=$((vec_dim-i))
  echo "${vec_dim_dbow}, ${vec_dim_dm}"
  source /Users/Shared/Anaconda/anaconda3/bin/activate /opt/anaconda3/envs/nlp-proj-36
  python ./paragraphvec/train.py start --data_file_name "${file_name}.csv" --num_epochs ${epoch} --batch_size 32 --num_noise_words 2 --num_workers 8 --vec_dim $vec_dim_dbow --lr 1e-3
  python ./paragraphvec/train.py start --data_file_name "${file_name}.csv" --num_epochs ${epoch} --batch_size 32 --num_noise_words 2 --num_workers 8 --vec_dim $vec_dim_dm --lr 1e-3 --model_ver dm --context_size 10
  python ./paragraphvec/export_vectors.py start --data_file_name "${file_name}.csv" --model_file_name "${file_name}_model.dbow_vecdim.${vec_dim_dbow}_intermediate.tar"
  python ./paragraphvec/export_vectors.py start --data_file_name "${file_name}.csv" --model_file_name "${file_name}_model.dm_vecdim.${vec_dim_dm}_intermediate.tar"
  source /Users/Shared/Anaconda/anaconda3/bin/activate /opt/anaconda3
  python ./csv_combine.py "${file_name}_model.dbow_vecdim.${vec_dim_dbow}_intermed.csv" "${file_name}_model.dm_vecdim.${vec_dim_dm}_intermed.csv" "${file_name}_vecdim.${vec_dim}.csv"
  python ./testTrain.py "./data/${file_name}_vecdim.${vec_dim}.csv" ${dataset} ${vec_dim_dbow} ${vec_dim_dm}
done