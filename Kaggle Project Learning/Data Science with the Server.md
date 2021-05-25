# Data Science with the Server

## Install the anacoda on the Aliclound Server

## c-bash: conda: command not found
```
vim ~/.bashrc
#added by Anaconda3 4.4.0 installer
export PATH="/root/anaconda3/bin:$PATH"
source ~/.bashrc
```
[阿里云服务器使用的坑：安装anaconda步骤以及问题处理](https://blog.csdn.net/weixin_43781538/article/details/104920370)   
## Main refernce:
[python数据分析之路——购买并在自己的云服务器上配置anaconda](https://zhuanlan.zhihu.com/p/106320410)
[CentOS 7安装Anaconda3](https://blog.csdn.net/jh0218/article/details/85097061)
Other Reference:
[云服务器上安装Anaconda3 (亲测有效)](https://blog.csdn.net/qq_40644291/article/details/102637750)   
[在腾讯云上搭建Python环境](https://zhuanlan.zhihu.com/p/344963251)

## Upgrade the Python 2 to python3
### 若报错 ln: failed to create symbolic link ‘/usr/bin/python’: File exists
```
ln -sf /usr/local/python3/bin/python3 /usr/bin/python
```
[阿里云服务器将python2升级到python3](https://blog.csdn.net/weixin_43523640/article/details/115725972)  
Main refernce:
[阿里云服务器中CentOS7升级Python环境](jianshu.com/p/6ec123426787)   
[在阿里云上的centos服务器自带python版本 2.7，如何更改成python3呢](https://www.cnblogs.com/bronyaa/p/14072876.html)   
## Conda activate not working?
[Conda activate not working?](https://stackoverflow.com/questions/47246350/conda-activate-not-working)  
## Can not run the jupyter
编辑jupyter notebook配置文件
```
c.NotebookApp.ip='0.0.0.0' #设置所有ip皆可访问
c.NotebookApp.password = u'sha1:df4a1....' # 复制刚才生成的那个密文'，注意前面有个 u
c.NotebookApp.open_browser = False # 禁止自动打开浏览器
c.NotebookApp.port =8889 
```
[4. 修改配置文件](https://www.pythonf.cn/read/101121#4__86)  
[CentOS7下Anaconda3配置Jupyter Notebook](https://blog.csdn.net/qq_41982466/article/details/116670984?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-9.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-9.control)  
Main reference:
[阿里云 centos 8 安装jupyter notebook](https://blog.csdn.net/StevenAC/article/details/109278188)
