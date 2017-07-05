#!/bin/bash

python ./src/log_anomaPurchasev1.py ./sample_dataset/stream_log.json ./log_output/flagged_purchases.json

python ./src/log_user_networkv1.py ./sample_dataset/batch_log.json ./log_output/flagged_purchases_v2.json





