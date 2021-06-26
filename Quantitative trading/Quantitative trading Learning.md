## 量化交易
##  Django
### Bug:Command 'django-admin' not found, but can be installed with: Linux
```
pip uninstall django
sudo pip install django
django-admin startproject example
```

You need to createa a vitural enviroment, then install the django in this enviroment. and type the code in this enviroment
[django-admin --version can not find installed version](https://askubuntu.com/questions/1190547/django-admin-version-can-not-find-installed-versionhttps://askubuntu.com/questions/1190547/django-admin-version-can-not-find-installed-version)  
[Command not found: django-admin.py](https://stackoverflow.com/questions/8250086/command-not-found-django-admin-py#:~:text=If%20you%20come%20across%20command,install%20the%20framework%20using%20pip.&text=After%20that%20look%20at%20the,admin.py%20exist%20or%20not.)



Version check:
```
>>> import django
>>> django.VERSION
(2, 0, 0, 'final', 0)
```
[How to check Django version](https://stackoverflow.com/questions/6468397/how-to-check-django-version#:~:text=Simply%20type%20python%20%2Dm%20django,of%20installed%20modules%20including%20Django.)

Main reference:  
[39 | Django：搭建监控平台](https://time.geekbang.org/column/article/113533)  

### Bug:No module named 'websocket'No module named 'websocket'
```
pip install websocket-client
```
[No module named 'websocket'No module named 'websocket'](https://stackoverflow.com/questions/47665760/no-module-named-websocket/47666357)  

## ImportError: No module named 'thread'
```
import _threadimport _thread
```
## the reason why you can not see the 36.py content come out, because you did not put the BTCUSD_GEMINI.csv file under the project folder:

and missing the code below:
```
import os.path as path
import pandas as pdimport os.path as path
import pandas as pd
```
[ImportError: No module named 'thread'](https://stackoverflow.com/questions/36809788/importerror-no-module-named-thread)  
[Python Multiline Comments](https://realpython.com/python-comments-guide/)  

[GeekTimePythonClass](https://github.com/Eyelidstl/GeekTimePythonClass/blob/master/class_36/utils.py)  

## Bug fxing:Unable to use matplotlib

Just hit the short cut"Ctrl+Alt+S" to view the Python interpret function, then you can decide to install the " matplotlib" package

[Install, uninstall, and upgrade packages](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html)  
[Configure a Python interpreter](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.htmlhttps://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)  
[Unable to use matplotlibUnable to use matplotlib](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360003732899-Unable-to-use-matplotlib)  

Main reference:    
[带你初探量化世界](https://time.geekbang.org/column/article/109128)  

Reference:   
[学习量化投资，看这篇文章就够了](https://zhuanlan.zhihu.com/p/20750993)  
[量化研究每周精选](https://www.zhihu.com/column/c_109014466)    

## How to set word wrap in the latest version of pycharm
[How to set word wrap in the latest version of pycharm](https://www.programmersought.com/article/29724237816/)
## Bug fxing:Unable to use matplotlib

Just hit the short cut"Ctrl+Alt+S" to view the Python interpret function, then you can decide to install the " matplotlib" package

[Install, uninstall, and upgrade packages](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.htmlhttps://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html)  
[Configure a Python interpreter](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.htmlhttps://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)  
[Unable to use matplotlibUnable to use matplotlib](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360003732899-Unable-to-use-matplotlib)  

Main reference:    
[带你初探量化世界](https://time.geekbang.org/column/article/109128)  

Reference:   
[学习量化投资，看这篇文章就够了](https://zhuanlan.zhihu.com/p/20750993)  
[量化研究每周精选](https://www.zhihu.com/column/c_109014466)  
