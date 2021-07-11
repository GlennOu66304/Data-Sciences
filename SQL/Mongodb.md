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
mongo
```

4.relaunch the the backend project again

## Use the mongod to debug the mongod issue:

## Linux install the mongodb compass:
```
sudo dpkg -i mongodb-compass_1.26.1_amd64.deb
mongodb-compass
```
[Download and Install Compass](https://docs.mongodb.com/compass/master/install/)

## How to use the command to import a database file into the mongodb
1.first install the mongotool 
```
brew install mongodb-database-tools
```
[mongodump and mongorestore command not found mac](https://stackoverflow.com/questions/63255620/mongodump-and-mongorestore-command-not-found-mac). 
2.make sure the database is running:
```
mongod --dbpath /System/Volumes/Data/data/db 
```
3.restore to a new database:
do not run it in the mongoshell, run it after the mongod --dbpath /System/Volumes/Data/data/db
```
mongorestore -d elem --verbose /Users/glenn/Downloads/elm
```
[restore to a new database:](https://stackoverflow.com/questions/18931668/how-to-restore-the-dump-into-your-running-mongodb).  

4.reference
[mongoD通过命令行批量导入json/bson数据](https://blog.csdn.net/c_zyer/article/details/76531859?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-7.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-7.control).   
[mongorestore](https://docs.mongodb.com/database-tools/mongorestore/).  
[Mongo导入json或者bson格式的文件](https://blog.csdn.net/weixin_44151887/article/details/106916153).  
[MongoDB 导入Json和Bson](https://blog.csdn.net/lwc5411117/article/details/79675326).   

