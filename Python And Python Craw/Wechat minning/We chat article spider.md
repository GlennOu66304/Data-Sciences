## Wechat article spider:  
## install the mongodb and redis on Linux system:
### 1.Mongodb:
```
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

sudo apt-get update

sudo apt-get install -y mongodb-org

ps --no-headers -o comm 1

sudo systemctl start mongod

```

Main reference:  
[nstall MongoDB Community Edition on Ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/#install-mongodb-community-edition) 

###  2. redis:  
1. install the local version:
 http://download.redis.io/redis-stable.tar.gz.
 
2. command line install
```
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
```
### Bug fixing:  You need tcl 8.5 or newer in order to run the Redis test make
```
sudo apt-get install tcl
```
[make test fails #1218](https://github.com/redis/redis/issues/1218)  

### Bug fixing:redis-server does not work
```
cd redis-stable
sudo cp src/redis-server /usr/local/bin/
sudo cp src/redis-cli /usr/local/bin/
sudo make install.
```
### Bug Start and shutdown the resdis
```
redis-server
redis-cli shutdown
```
[How can I stop redis-server?](https://stackoverflow.com/questions/6910378/how-can-i-stop-redis-server#:~:text=start%20will%20start%20the%20redis,it%20at%20login%20and%20boot.&text=if%20your%20don't%20care,to%20force%20shutdown%20the%20server.&text=Try%20killall%20redis%2Dserver%20.,it%20with%20kill%20%2D9%20here_pid_number%20.)  

Main reference:
[Installing Redis](https://redis.io/topics/quickstart)  
[How To Install and Secure Redis on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)  
[ubuntu下Fiddler抓包](https://www.jianshu.com/p/4505c732e378)  
[Welcome to the Fiddler Alpha for Mono.](http://fiddler.wikidot.com/mono)  
[How To Show Hidden Files In Linux](https://phoenixnap.com/kb/show-hidden-files-linux#:~:text=Show%20Hidden%20Files%20in%20a%20Graphical%20Interface%20(GUI),-There's%20a%20simple&text=2.,box%20to%20Show%20hidden%20files.)  
[How To Show Hidden Files on Linux](https://devconnected.com/how-to-show-hidden-files-on-linux/)   

## Anyproxy installation and use
### Bug: PM2 command not found
[PM2 command not found](https://stackoverflow.com/questions/38185590/pm2-command-not-found/38185684)  

Main reference:  
[Anyproxy installation and use](https://www.programmersought.com/article/9371990930/)  

### Node / Express: EADDRINUSE, Address already in use - Kill server
```
sudo pkill node
```
[Node / Express: EADDRINUSE, Address already in use - Kill server](https://stackoverflow.com/questions/4075287/node-express-eaddrinuse-address-already-in-use-kill-server?page=2&tab=votes#tab-top)  
### Check the web interface:  
Jsut the add the portal to the locall host:  
```
http://localhost:8002/
```
[5、安装证书，在手机或安卓模拟器中安装证书：](https://zhuanlan.zhihu.com/p/24302048)  


### install the anyproxy in the iOS and make the connection between the PC and mobile device:  
1. install the anyproxy in the iOS device:
download the certicate in the PC, then send it to the iOS via the wechat. 

2. within the mobile wechat, choose to open this file via the iOS file management app, and place it in to a single file;  

3. click this file; 

4. Go back to the iOS Setting and chooose to install this profile, and trust it in the iOS certificate place;  

5. make sure the mobile and PC are in the same wifi internet, then go to the wifi setting in this iOs device and locate the http proxy setting;
[Ubuntu 16下 AnyProxy + ios 抓包环境配置](https://blog.csdn.net/YTREE_BJ/article/details/91410282)  
[抓包工具anyproxy使用总结](https://blog.csdn.net/Love_your_life/article/details/80135702)  
6. choose the command line below to locate the PC's internet IP address;
[linux系统(ubuntu)如何查看ip地址](https://blog.csdn.net/u012269267/article/details/52260757) 
7. place this IP address and portal 8001 in this field, then you go to the wechat article to see the change on the anyproxy web interface.

Main reference:  
[持续更新，微信公众号文章批量采集系统的构建](https://zhuanlan.zhihu.com/p/24302048)  
Important reference:  
[ilongsy/anyproxy-wechat](https://github.com/lilongsy/anyproxy-wechat)  
[微信公众号文章爬虫制作01，批量采集公众号文章内容浏览量](https://www.youtube.com/watch?v=T-hVHJO0ya0&feature=youtu.be)

Reference:
[基于AnyProxy自动爬取微信公众号数据（详细部署、bug说明)](https://www.jianshu.com/p/83d8e44e04fa)  
[使用 anyproxy 二次开发的微信公众号抓取工具，可以抓阅读数，点赞数，赞赏数和回复数](https://learnku.com/articles/4352/wechat-spider) 

[anyproxy + wechat_spider配置微信公众号爬虫](https://danteng.org/anyproxy-wechat-spider-mp-wechat/)
[使用 Fiddler 抓包分析公众号请求过程](https://juejin.cn/book/6844733701339742216/section/6844733701444599815]  


[Best Tools For Taking and Editing Screenshots in Linux](https://itsfoss.com/take-screenshot-linux/)  
[What is the terminal command to take a screenshot?](https://askubuntu.com/questions/194427/what-is-the-terminal-command-to-take-a-screenshot)  
