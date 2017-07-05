# log_user_networkv1.py

# wc -l batch_log.json  500000

# P = purchase; 

print "running log_user_networkv1.py "

import numpy as np

fileI=open('./log_input/batch_log.json','r')

NOL=500000  # No of line
RF=2**5     # Reduction factor  
LC=int(NOL/RF)

# List for purchase record
ID_P=[]   # P for purchase; np.size(ID_P)=398 for RF=2**10 
TS_P=[]   # time stamp for purchase; np.size(TS_P)=398 for RF=2**10 
P_AD=[]   # purchase amount in dollar; np.size(P_AD)=398 for RF=2**10 

# List for record of social network

ID_U_U1stDFN=[]  # user ID plus users' 1st degree friends network id
# np.size(ID_U_U1stDFN)= 172/2 = 86 for RF=2**10  
TS_U_U1stDFN=[]  # timesatmp for users social network (friend)



ID_U_U1stDUFN=[]  # user ID plus users' 1st degree unfriends network id
# np.size(ID_U_U1stDUFN) = 6/2 = 3 for RF=2**10  
TS_U_U1stDUFN=[]  # timesatmp for users social network (friend) 



ncP=0   # number count for purchases
ncUSNF=0  # number count for user and friend's social network
ncUSNUF=0  # number count for user and unfriend's social network

for i in range(0,LC):
    line=fileI.readline()
    linesplt=line.split()
    item=linesplt[0]
    item=item[15:]
    item=item[:-2]
    if ( np.size(linesplt)==7 and item=='purchase'):
        ncP=ncP+1
        idp=linesplt[4]
        idp=idp[1:]
        idp=idp[:-2]
        ID_P.append(idp)
        tstampp=str(line[39:58])
        TS_P.append(tstampp)
        pamount=linesplt[6]
        pamount=pamount[1:]
        pamount=float(pamount[:-2])
        P_AD.append(pamount) 
    elif ( np.size(linesplt)==7 and item=='befriend'): 
        ncUSNF=ncUSNF+1 
        idU=linesplt[4]
        idU=idU[1:] 
        idU=idU[:-2]
        idF=linesplt[6]
        idF=idF[1:]
        idF=idF[:-2]
        idUidF=[idU,idF]
        ID_U_U1stDFN.append(idUidF)
        tstampSNF=str(line[39:58])
        TS_U_U1stDFN.append(tstampSNF)
    elif ( np.size(linesplt)==7 and item=='unfriend'): 
        ncUSNUF=ncUSNUF+1
        idU=linesplt[4]
        idU=idU[1:]
        idU=idU[:-2]
        idUF=linesplt[6]
        idUF=idUF[1:]
        idUF=idUF[:-2]
        idUidUF=[idU,idUF]
        ID_U_U1stDUFN.append(idUidUF)
        tstampSNUF=str(line[39:58])
        TS_U_U1stDUFN.append(tstampSNUF) 
                    
fileI.close()


# analyze 1st degree network


# ID_U_U1stDFN=[]  # user ID plus users' 1st degree friends network id
# np.size(ID_U_U1stDFN)= 172/2 = 86 for RF=2**10 


ID_U=[]  # user id; np.size(ID_U) = 86; for RF=2**10
ID_1stDF=[] # users 1st degree friend; np.size(ID_1stDF) = 86; 
for i in range(0,np.size(ID_U_U1stDFN)/2):
    ids=ID_U_U1stDFN[i]
    id1=ids[0]
    ID_U.append(id1)
    id2=ids[1]
    ID_1stDF.append(id2)
    
    
# check whether ID_U[] contains duplicate ids

ID_U_UnDup=list(set(ID_U))  #  np.size(ID_U_UnDup) = 1359 for RF=2**6  but 
# np.size(ID_U) = 1472 for  RF=2**6  
# there are some duplicate id in ID_U


# get the 1st degree network wrt unduplicated user ids  ID_U_UnDup[]; 

ID_F1stD=[]   # ID_F1stD[38] = ['7161', '3906']  for RF=2**8 since a user can 
# have multiple 1st degree friend

for i in range(0,np.size(ID_U_UnDup)):  # np.size(ID_U_UnDup) = 361; RF=2**8
    id1Un=ID_U_UnDup[i]
    id_F_user=[]
    for ii in range(0,np.size(ID_U)):
        id1=ID_U[ii]
        if ( id1Un==id1 ):
            idF1=ID_1stDF[ii]
            id_F_user.append(idF1)
    ID_F1stD.append(id_F_user)            # np.size(ID_F1stD)=361; RF=2**8 
    
            
# print ID_F1stD    # RF=2**4    

# let us get users and users network purchase hsitory

# ID_U_UnDup[]; ID_P[]; TS_P[]; P_AD=[]

U_P_R=[]  # user purchase record; [user_id, purchase_id,time_purchase,purchase amount], 
# np.size(U_P_R) = 260/5=52  # user_id, purchase_id be the same

for i in range(0, np.size(ID_U_UnDup)):
    idu=ID_U_UnDup[i] # user id
    for ii in range(0, np.size(ID_P)):
        idp=ID_P[ii]
        if ( idu==idp ):
            upid=idp # user purchase id
            upa=P_AD[ii] # user purchase amount
            upt=TS_P[ii] # user purchase time
            uprec=[ID_U_UnDup[i],TS_P[ii],P_AD[ii]] # user purchase rec
            U_P_R.append(uprec)

# print np.size(U_P_R)/3    

# now we will find out users 1st degree fireinds purchases U_P_R[] since all user 
# ids may not have a purchase record

def stddev(x):
    import numpy as np
    from math import sqrt
    xmean=np.mean(x)
    dssum=0
    for i in range(0,np.size(x)):
        stditem=(x[i]-xmean)**2
        dssum=dssum+stditem
    stddev=sqrt(dssum/np.size(x))
    return stddev 
    
#  np.size(U_P_R)/3=7;  {np.size(ID_U_UnDup)=178; np.size(ID_F1stD)=178} 

print "writing output"

fileO=open('./log_output/flagged_purchases_v2.json','wb')

# string for printing output
s1=" \"event_type\":\"purchase\", \"timestamp\": \" "
s2=" \", \"id\": \" "
s3=" \", \"amount\": \" "
s4=" \", mean\": \" "
s4=" \", mean\": \" "
s5=" \", \"sd\": \" "
s6=" \" "

T =5 # number of purchases made by D=1
for i in range(0, np.size(U_P_R)/np.size(uprec)):   # np.size(U_P_R)/5 = 52
    eitem=U_P_R[i]  # each item
    uid=eitem[0]   # user id
    tstampUP=eitem[1] # time stamp of user purchase
    upa=eitem[2]   # user purchase amount
    format(upa, '.2f')
    PBFN=[]  # purchase by friends network for corresponding user
    for j in range(0, np.size(ID_U_UnDup)):
        uidUn=ID_U_UnDup[j] # user original unduplicated id 
        if ( uid==uidUn ):
            F1stdList=ID_F1stD[j] # F1stdList[] contains multiple ids  # 1st degree friends list
            for jf in range(0, np.size(F1stdList)):
                idf=F1stdList[jf] # friend id 
                PfeF=[]  # purchase for each friend
                nc=0 
                for k in range(0, np.size(ID_P)):
                    idp=ID_P[k]
                    if ( idf==idp ):
                        nc=nc+1
                        pamount=P_AD[k]# purchase amount in $
                        tstamFp=TS_P[k]; # timestamp for Friends' purchases
                        PfeF.append(pamount)
                        if ( np.size(PfeF)>T ):   # this can be varied 
                            mean_P1stDFN=sum(PfeF)/nc  # mean purchase of 1st degree friends network
                            sd_P1stDFN=stddev(PfeF)  # std dev of purchases of 1st degree friends network
                            da_APC=mean_P1stDFN+(3*sd_P1stDFN)  # $ amount for Anomalous purchase condition
                            #print tstamFp, tstampUP
                            if ( upa> da_APC ):
                                format(mean_P1stDFN, '.2f')
                                format(sd_P1stDFN, '.2f')
                                fileO.write('%s%s%s%s%s%s%s%s%s%s%s\n'%(s1,tstampUP,s2,uid,s3,upa,s4,mean_P1stDFN,s5,sd_P1stDFN,s6))
                                #print "timestamp",tstampUP,"id",uid,"amount",upa,"mean",mean_P1stDFN,"sd",sd_P1stDFN
fileO.close()
                    
# above analysis of anomalous purchase was done in comparison to user 1st degree
# friends network. This can be done with users 2nd degree friends network as well                        
                
                    
# print "let us find users 2nd degree social network "

# ID_U_U1stDFN => {L88: ID_U[], ID_1stDF[]}; 

U_F1st_F2nd_N=[] # users and users' 1st and 2nd degree friends network
for i in range(0, np.size(ID_1stDF)):
    idF=ID_1stDF[i]
    for j in range(0,np.size(ID_U)):
        idU=ID_U[j]
        if ( idF==idU ):
            u1stdF2nddF=[ID_U[i],ID_U[j],ID_1stDF[j]]
            #print "user id",ID_U[i],"friend id",ID_U[j],"2nd degree friend id",ID_1stDF[j]
            U_F1st_F2nd_N.append(u1stdF2nddF)
        
# print U_F1st_F2nd_N
  
                    
    
    
    



















