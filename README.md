## Contents

[Approach](RAEDME.md#approach)

Two input files named as batch_log.json and stream_log.json are provided in the project.  

The first file, batch_log.json , contains past data that should be used to build the initial state of the entire user
network, as well as the purchase history of the users.

Data in the second file, stream_log.json , should be used to determine whether a purchase is anomalous. If a
purchase is flagged as anomalous, it should be logged in the flagged_purchases.json file. As events come in, both the
social network and the purchase history of users should get updated.

## Approach

### Analysis regarding 1st input file batch_log.json

#### log_user_networkv1.py

log_user_networkv1.py uses 1st input file batch_log.json having 500,000 line data entry. For quicker check of user network analysis through various steps of this code initially I have introduced a reduction afctor (RF = 2, 4, 8, 16 etc) that basically give us a option to test the code with relatively smaller input data. 

Since the input data consists of user social network (such as "befriend" or "unfriend") and user purchases as well as purchases of social network of various degrees such as 1st degree friend (D=1); 2nd degree friend (D=2); etc.

#### Users

At the beginning log_user_networkv1.py collects user ids from "event_type": "friend". After that it collects ids, timesatmps and purchase amount for purchase event while it collects [id1, id2], timestamps for social network events such as befriend or unfriend. Now [id1] are not unique since social network expands with time.  





