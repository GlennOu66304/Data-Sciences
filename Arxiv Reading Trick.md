# Arxiv Reading Trick.
## 1.Enviroment building:
1.install homebrew:
<br>Homebrew install erro
<br>https://github.com/GlennOu66304/CS-RESOURS-CENTER/blob/master/C%20language/Homebrew%20install%20erro.md

2.install mactex:
```
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % brew cask install mactex
==> Downloading http://mirror.ctan.org/systems/mac/mactex/mactex-20200407.pkg
==> Downloading from http://mirrors.ustc.edu.cn/CTAN/systems/mac/mactex/mactex-2
######################################################################## 100.0%
==> Verifying SHA-256 checksum for Cask 'mactex'.
==> Installing dependencies: jpeg, libtiff, ghostscript
==> Installing jpeg
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles/bottles/jpeg-9d.cat
######################################################################## 100.0%
==> Pouring jpeg-9d.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/jpeg/9d: 21 files, 775.2KB
==> Installing libtiff
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles/bottles/libtiff-4.1
######################################################################## 100.0%
==> Pouring libtiff-4.1.0.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/libtiff/4.1.0: 247 files, 3.7MB
==> Installing ghostscript
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles/bottles/ghostscript
######################################################################## 100.0%
==> Pouring ghostscript-9.52.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/ghostscript/9.52: 671 files, 87.4MB
==> Installing Cask mactex
==> Running installer for mactex; your password may be necessary.
==> Package installers may write to any location; options such as --appdir are i
Password:
  
installer: Package name is MacTeX
installer: choices changes file '/var/folders/l_/j5w1kpv56tl0w12grfpd95tm0000gn/T/choices20200430-7605-1v8fgh8.xml' applied
installer: Installing at base path /
installer: The install was successful.
🍺  mactex was successfully installed!
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % 
```
3.install comparxiv
```
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip3 install comparxiv
Collecting comparxiv
  Downloading https://files.pythonhosted.org/packages/d4/d2/1ea4f2c5ec90738a7ae5e1c9b3288a65f7338e0c10206c7eef8c29759167/comparxiv-0.1.7-py3-none-any.whl
Collecting requests (from comparxiv)
  Downloading https://files.pythonhosted.org/packages/1a/70/1935c770cb3be6e3a8b78ced23d7e0f3b187f5cbfab4749523ed65d7c9b1/requests-2.23.0-py2.py3-none-any.whl (58kB)
     |████████████████████████████████| 61kB 48kB/s 
Collecting arxiv (from comparxiv)
  Downloading https://files.pythonhosted.org/packages/50/81/9714d5a4efc14edddb308c0b527fe2d9ac35840fcfa83684a52655d35d42/arxiv-0.5.3-py3-none-any.whl
Collecting tqdm (from comparxiv)
  Downloading https://files.pythonhosted.org/packages/4a/1c/6359be64e8301b84160f6f6f7936bbfaaa5e9a4eab6cbc681db07600b949/tqdm-4.45.0-py2.py3-none-any.whl (60kB)
     |████████████████████████████████| 61kB 18kB/s 
Collecting argparse (from comparxiv)
  Downloading https://files.pythonhosted.org/packages/f2/94/3af39d34be01a24a6e65433d19e107099374224905f1e0cc6bbe1fd22a2f/argparse-1.4.0-py2.py3-none-any.whl
Collecting chardet<4,>=3.0.2 (from requests->comparxiv)
  Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
     |████████████████████████████████| 143kB 26kB/s 
Requirement already satisfied: certifi>=2017.4.17 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from requests->comparxiv) (2020.4.5.1)
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 (from requests->comparxiv)
  Downloading https://files.pythonhosted.org/packages/e1/e5/df302e8017440f111c11cc41a6b432838672f5a70aa29227bf58149dc72f/urllib3-1.25.9-py2.py3-none-any.whl (126kB)
     |████████████████████████████████| 133kB 12kB/s 
Collecting idna<3,>=2.5 (from requests->comparxiv)
  Downloading https://files.pythonhosted.org/packages/89/e3/afebe61c546d18fb1709a61bee788254b40e736cff7271c7de5de2dc4128/idna-2.9-py2.py3-none-any.whl (58kB)
     |████████████████████████████████| 61kB 26kB/s 
Collecting feedparser (from arxiv->comparxiv)
  Downloading https://files.pythonhosted.org/packages/91/d8/7d37fec71ff7c9dbcdd80d2b48bcdd86d6af502156fc93846fb0102cb2c4/feedparser-5.2.1.tar.bz2 (192kB)
     |████████████████████████████████| 194kB 11kB/s 
Installing collected packages: chardet, urllib3, idna, requests, feedparser, arxiv, tqdm, argparse, comparxiv
  Running setup.py install for feedparser ... done
Successfully installed argparse-1.4.0 arxiv-0.5.3 chardet-3.0.4 comparxiv-0.1.7 feedparser-5.2.1 idna-2.9 requests-2.23.0 tqdm-4.45.0 urllib3-1.25.9
WARNING: You are using pip version 19.2.3, however version 20.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % 
```
## References Paper:
comparxiv
<br>https://github.com/temken/comparxiv
<br>查阅arXiv论文新神器，一行代码比较版本差别，Github新开源
<br>贾浩楠 发自 凹非寺 量子位 报道 | 公众号 QbitAI
<br>https://mp.weixin.qq.com/s/54dUw6vfQ35t5QZqmW0Dfg
