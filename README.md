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

log_user_networkv1.py uses 1st input file batch_log.json having 500,000 line data entry. For quicker check of user network analysis through various steps of this code, initially I have introduced a reduction factor (RF = 2, 4, 8, 16 etc) that basically give us a option to test the code with relatively smaller input data. 

Since the input data consists of user social network (such as "befriend" or "unfriend") and user purchases as well as purchases of social network of various degrees such as 1st degree friend (D=1); 2nd degree friend (D=2); etc.

At the beginning log_user_networkv1.py collects user ids from "event_type": "friend". After that it collects ids, timesatmps and purchase amount for purchase event while it collects [id1, id2], timestamps for social network events such as befriend or unfriend. Here [id1] are not unique since social network expands with time. 

So we determine unique user list (unduplicated). With respect to this unique user lsit we sort out users (ID_U_UnDup[]) 1st degree friends network "ID_U_U1stDFN[]". "ID_U_U1stDFN[]" basically lists user ids and corresponding friend ids labelled as 1st degree friend.


Each each id was compared with purchase id to sort out users purchases. "U_P_R[]" lists [user id, user purchase time, purchase amount].
User can make multiple purchase, however for sorting the anomalous purchases only user purchases was list where the purchase amount is greater than the user Dth degree friends network last (T purchases mean + 3*sd).

Now some of the friends ids exists in the user id list that provides the clue for finding 2nd degree social network. "U_F1st_F2nd_N[]" is a list with [user id, user 1st degree friend id, user 2nd degree friend id].

log_user_networkv1.py can be run with various RF with varyping parameter such as T. Additional reported output "flagged_purchases_v2.json" is done with T=5, RF=2^5. 


### Analysis regarding 2nd input file stream_log.json

#### log_anomaPurchasev1.py

In log_anomaPurchasev1.py does similar analysis for detecting anomalous purchase. since this file is relatively smaller in size (line entry only 1001) so it performs and presents the features within a click. Anomalous purchase deetcted here has been reported as required output "flagged_purchases.json". 






