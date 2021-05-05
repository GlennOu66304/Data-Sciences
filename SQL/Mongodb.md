## Mongodb, Redis, docker
[install the mongodb and redis on Linux system:](https://github.com/GlennOu66304/Data-Sciences/blob/master/Python%20And%20Python%20Craw/Wechat%20minning/We%20chat%20article%20spider.md)   
[MongDB Database:](https://github.com/GlennOu66304/bucket-list-mevn)    
[2.connect to database:](https://github.com/GlennOu66304/Fullstack-Enterprise-MEVN-Mongo-Express-Vue-and-Node)  

## Connect with the Database

open a new terminal :
1.run the mongodb

```
brew services start mongodb-community@4.4
```

2.Change the dbpath

```
mkdir -p /System/Volumes/Data/data/db
mongod --dbpath /System/Volumes/Data/data/db
```

[[Help] Can't create data/db directory](https://www.reddit.com/r/mongodb/comments/d723b0/help_cant_create_datadb_directory/)  
3.open a new terminal,make sure the mongod tab is live:

```
mongod
```

4.relaunch the the backend project again

## Use the mongod to debug the mongod issue:
