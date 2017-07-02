### Contents

1. [Objective](RAEDME.md#Objective)
2. [Steps](RAEDME.md#Steps)



### Steps

1. The first file batch_log.json contains past data should be used to build initial state of the entire user network, as well as the purchase history of the users. 

batch_log.json contains mainly "purchase" data as well as social network data of users termed as "befriend" and "unfriend". 

"Save_Each_Entry.py" basically saved individual entries such as user ids, transaction amounts and timestamps of "batch_log.json" into
separate files named as "shopperID.json", "transactions.json" and "timestamps.json". 


"socialNetworkv1.py" first collects user ids as list, UserA and User's 1st degree social network. Since users do multiple tarnsactions over time hence we need to figure out unique user list (UserAlist). 

After that we need to find out users 1st degree social network (usrA1stdegSocNetwork).

Now we need to find out users purchase history using users' unique ids. Since users did multiple purchases over time, so we need to find out users' highest purchase along with its timestamp since user's highest purchase will be considered as anomalous if it is (mean + 3*sd) more than that of the users' 1st degree social network's last 50 purchases.   
 

