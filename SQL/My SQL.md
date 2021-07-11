
## Install and run the My SQL on Mac

### install:
[ MySQL Community Downloads](https://dev.mysql.com/downloads/mysql/).  
[Installing MySQL on macOS Using Native Packages](https://dev.mysql.com/doc/refman/5.7/en/macos-installation-pkg.html).   

## GUI tool:MySQL Workbench
[MySQL Workbench](https://dev.mysql.com/downloads/workbench/).  

## MySQL shell
[MySQL Shell](https://dev.mysql.com/downloads/shell/).   

## Mysql can not find
```
$ vim ~/.bash_profile  
PATH=$PATH:/usr/local/mysql/bin 
source ~/.bash_profile  
vim .zshrc
source ~/.bash_profile 
```
[设置环境变量：](https://juejin.cn/post/6844903633436278792).  
[How to Save a File in Vim / Vi and Quit the Editor](https://linuxize.com/post/how-to-save-file-in-vim-quit-editor/#:~:text=The%20command%20to%20save%20a%20file%20in%20Vim%20and%20quit,type%20%3Awq%20and%20hit%20Enter%20.&text=Another%20command%20to%20save%20a%20file%20and%20quit%20Vim%20is%20%3Ax%20.).  
```
Press Esc
Type :w
Press Enter
```
## Access denied for user 'root@localhost' (using password:NO)
```
mysql -u root -p
```
[Access denied for user 'root@localhost' (using password:NO)](https://stackoverflow.com/questions/2995054/access-denied-for-user-rootlocalhost-using-passwordno). 

## Run the SQL script in the workbench
[workbench How to run SQL script in MySQL?](https://www.tutorialspoint.com/how-to-run-sql-script-in-mysql).   
[How to run SQL script in MySQL?](https://stackoverflow.com/questions/8940230/how-to-run-sql-script-in-mysql). 



## Error Code: 1046. No database selected Select the default DB to be used by double clicking its name
Work bench[Error Code: 1046. No database selected Select the default DB to be used by double clicking its name](https://www.programmersought.com/article/26507710508/).  
[SQL “with” clause - Error Code: 1046. No database selected Select the default DB to be used by double-clicking its name in the SCHEMAS](https://stackoverflow.com/questions/51791618/sql-with-clause-error-code-1046-no-database-selected-select-the-default-db)

## .SQL File Extension
[.SQL File Extension](https://fileinfo.com/extension/sql).  

## Table check
[8.2.3 Schema and Table Inspector](https://dev.mysql.com/doc/workbench/en/wb-develop-object-management-inspector.html). 
[.SQL File Extension](https://fileinfo.com/extension/sql).   

## Usage exmple
[Build Node.js Rest APIs with Express & MySQL](https://bezkoder.com/node-js-rest-api-express-mysql/#Configure_038_Connect_to_MySQL_database).   

## My SQl:How To Allow Remote Access to MySQL
```
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
```
[How To Allow Remote Access to MySQL](https://www.digitalocean.com/community/tutorials/how-to-allow-remote-access-to-mysql)  
[Ubuntu 16.04 mysql安装配置](https://www.jianshu.com/p/3111290b87f4)  
[How to Allow MySQL Remote Access in Ubuntu Server](https://www.configserverfirewall.com/ubuntu-linux/enable-mysql-remote-access-ubuntu/#:~:text=Enable%20MySQL%20Server%20Remote%20Connection%20in%20Ubuntu&text=To%20enable%20remote%20connections%20to,d%2Fmysqld.https://www.configserverfirewall.com/ubuntu-linux/enable-mysql-remote-access-ubuntu/#:~:text=Enable%20MySQL%20Server%20Remote%20Connection%20in%20Ubuntu&text=To%20enable%20remote%20connections%20to,d%2Fmysqld.)
[Install MySQL in Ubuntu 20.04 Focal Fossa](http://www.alessioligabue.it/blog/installare-mysql-in-ubuntu-focal-fossahttp://www.alessioligabue.it/blog/installare-mysql-in-ubuntu-focal-fossa)   


## Video:
Managing Big Data With MySQL
<br>https://www.coursera.org/learn/analytics-mysql/lecture/qdPFO/what-you-will-learn-in-this-course
