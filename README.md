### Contents

1. [Objective](RAEDME.md#Objective)
2. [Steps](RAEDME.md#Steps)



### Steps

1. The first file batch_log.json contains past data should be used to build initial state of the entire user network, as well as the purchase history of the users. 

batch_log.json contains mainly "purchase" data as well as social network data of users termed as "befriend" and "unfriend". 

"Save_Each_Entry.py" basically saved individual entries such as user ids, transaction amounts and timestamps of "batch_log.json" into
separate files named as "shopperID.json", "transactions.json" and "timestamps.json". 


"socialNetworkv1.py" first collects user ids as list, UserA and UserB. 


