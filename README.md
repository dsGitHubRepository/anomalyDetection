### Contents

[Approach](RAEDME.md#approach)

Two input files named as batch_log.json and stream_log.json are provided in the project.  

The first file, batch_log.json , contains past data that should be used to build the initial state of the entire user
network, as well as the purchase history of the users.

Data in the second file, stream_log.json , should be used to determine whether a purchase is anomalous. If a
purchase is flagged as anomalous, it should be logged in the flagged_purchases.json file. As events come in, both the
social network and the purchase history of users should get updated.

### Approach



