# Kaggle Learning 2.

## jupyter kernal keeps dying #1892
uninstalling all of:ipykernel,ipython,jupyter_client,jupyter_core,traitlets,ipython_genutils include pip3 and pip then reinstall it.
```
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip3 uninstall ipykernel  
Uninstalling ipykernel-5.2.1:
  Would remove:
    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/ipykernel-5.2.1.dist-info/*
    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/ipykernel/*
    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/ipykernel_launcher.py
    /Library/Frameworks/Python.framework/Versions/3.8/share/jupyter/kernels/python3/kernel.json
    /Library/Frameworks/Python.framework/Versions/3.8/share/jupyter/kernels/python3/logo-32x32.png
    /Library/Frameworks/Python.framework/Versions/3.8/share/jupyter/kernels/python3/logo-64x64.png
Proceed (y/n)? y
  Successfully uninstalled ipykernel-5.2.1
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip3 uninstall ipython
Uninstalling ipython-7.14.0:
  Would remove:
    /Library/Frameworks/Python.framework/Versions/3.8/bin/iptest
    /Library/Frameworks/Python.framework/Versions/3.8/bin/iptest3
    /Library/Frameworks/Python.framework/Versions/3.8/bin/ipython
    /Library/Frameworks/Python.framework/Versions/3.8/bin/ipython3
    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/IPython/*
    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/ipython-7.14.0.dist-info/*
    /Library/Frameworks/Python.framework/Versions/3.8/share/man/man1/ipython.1.gz
Proceed (y/n)? y
  Successfully uninstalled ipython-7.14.0
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip3 uninstall jupyter_client
Uninstalling jupyter-client-6.1.3:
  Would remove:
    /Library/Frameworks/Python.framework/Versions/3.8/bin/jupyter-kernel
    /Library/Frameworks/Python.framework/Versions/3.8/bin/jupyter-kernelspec
    /Library/Frameworks/Python.framework/Versions/3.8/bin/jupyter-run
    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/jupyter_client-6.1.3.dist-info/*
    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/jupyter_client/*
Proceed (y/n)? y
  Successfully uninstalled jupyter-client-6.1.3
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip3 uninstall jupyter_core
Uninstalling jupyter-core-4.6.3:
  Would remove:
    /Library/Frameworks/Python.framework/Versions/3.8/bin/jupyter
    /Library/Frameworks/Python.framework/Versions/3.8/bin/jupyter-migrate
    /Library/Frameworks/Python.framework/Versions/3.8/bin/jupyter-troubleshoot
    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/jupyter.py
    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/jupyter_core-4.6.3.dist-info/*
    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/jupyter_core/*
Proceed (y/n)? y
  Successfully uninstalled jupyter-core-4.6.3
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip3 uninstall traitles 
WARNING: Skipping traitles as it is not installed.
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip3 uninstall ipython_genutils
Uninstalling ipython-genutils-0.2.0:
  Would remove:
    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/ipython_genutils-0.2.0.dist-info/*
    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/ipython_genutils/*
Proceed (y/n)? y
  Successfully uninstalled ipython-genutils-0.2.0
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip unstall ipykernel 
ERROR: unknown command "unstall" - maybe you meant "uninstall"
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip uninstall ipykernel  
Found existing installation: ipykernel 5.1.4
Uninstalling ipykernel-5.1.4:
  Would remove:
    /Users/zhanghuiqiao/opt/anaconda3/lib/python3.7/site-packages/ipykernel-5.1.4.dist-info/*
    /Users/zhanghuiqiao/opt/anaconda3/lib/python3.7/site-packages/ipykernel/*
    /Users/zhanghuiqiao/opt/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py
    /Users/zhanghuiqiao/opt/anaconda3/share/jupyter/kernels/python3/kernel.json
    /Users/zhanghuiqiao/opt/anaconda3/share/jupyter/kernels/python3/logo-32x32.png
    /Users/zhanghuiqiao/opt/anaconda3/share/jupyter/kernels/python3/logo-64x64.png
Proceed (y/n)? y
  Successfully uninstalled ipykernel-5.1.4
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip uninstall ipython 
WARNING: Skipping ipython as it is not installed.
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip uninstall jupyter_client 
Found existing installation: jupyter-client 5.3.4
Uninstalling jupyter-client-5.3.4:
  Would remove:
    /Users/zhanghuiqiao/opt/anaconda3/bin/jupyter-kernel
    /Users/zhanghuiqiao/opt/anaconda3/bin/jupyter-kernelspec
    /Users/zhanghuiqiao/opt/anaconda3/bin/jupyter-run
    /Users/zhanghuiqiao/opt/anaconda3/lib/python3.7/site-packages/jupyter_client-5.3.4.dist-info/*
    /Users/zhanghuiqiao/opt/anaconda3/lib/python3.7/site-packages/jupyter_client/*
Proceed (y/n)? y
  Successfully uninstalled jupyter-client-5.3.4
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip uninstall jupyter_core 
Found existing installation: jupyter-core 4.6.1
Uninstalling jupyter-core-4.6.1:
  Would remove:
    /Users/zhanghuiqiao/opt/anaconda3/bin/jupyter
    /Users/zhanghuiqiao/opt/anaconda3/bin/jupyter-migrate
    /Users/zhanghuiqiao/opt/anaconda3/bin/jupyter-troubleshoot
    /Users/zhanghuiqiao/opt/anaconda3/lib/python3.7/site-packages/jupyter.py
    /Users/zhanghuiqiao/opt/anaconda3/lib/python3.7/site-packages/jupyter_core-4.6.1.dist-info/*
    /Users/zhanghuiqiao/opt/anaconda3/lib/python3.7/site-packages/jupyter_core/*
Proceed (y/n)? y
  Successfully uninstalled jupyter-core-4.6.1
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip uninstall traitlets 
Found existing installation: traitlets 4.3.3
Uninstalling traitlets-4.3.3:
  Would remove:
    /Users/zhanghuiqiao/opt/anaconda3/lib/python3.7/site-packages/traitlets-4.3.3.dist-info/*
    /Users/zhanghuiqiao/opt/anaconda3/lib/python3.7/site-packages/traitlets/*
Proceed (y/n)? y
  Successfully uninstalled traitlets-4.3.3
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip uninstall ipython_genutils 
Found existing installation: ipython-genutils 0.2.0
ERROR: Cannot uninstall 'ipython-genutils'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip3 install ipykernel 
Collecting ipykernel
  Using cached https://files.pythonhosted.org/packages/ed/5d/cf47741fa80826f8edf435d9bcf0e84eef2d6d02953ff85e0563b3ab3f0b/ipykernel-5.2.1-py3-none-any.whl
Collecting jupyter-client (from ipykernel)
  Using cached https://files.pythonhosted.org/packages/34/0b/2ebddf775f558158ca8df23b35445fb15d4b1558a9e4a03bc7e75b13476e/jupyter_client-6.1.3-py3-none-any.whl
Requirement already satisfied: appnope; platform_system == "Darwin" in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipykernel) (0.1.0)
Requirement already satisfied: traitlets>=4.1.0 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipykernel) (4.3.3)
Collecting ipython>=5.0.0 (from ipykernel)
  Using cached https://files.pythonhosted.org/packages/b0/00/afc3968a3cdf5f30c5c9dfb8e6a61e63231d6869a461dc1ff418280c5ea4/ipython-7.14.0-py3-none-any.whl
Requirement already satisfied: tornado>=4.2 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipykernel) (5.0)
Requirement already satisfied: python-dateutil>=2.1 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from jupyter-client->ipykernel) (2.8.1)
Collecting jupyter-core>=4.6.0 (from jupyter-client->ipykernel)
  Using cached https://files.pythonhosted.org/packages/63/0d/df2d17cdf389cea83e2efa9a4d32f7d527ba78667e0153a8e676e957b2f7/jupyter_core-4.6.3-py2.py3-none-any.whl
Requirement already satisfied: pyzmq>=13 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from jupyter-client->ipykernel) (19.0.0)
Requirement already satisfied: decorator in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from traitlets>=4.1.0->ipykernel) (4.0.11)
Requirement already satisfied: six in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from traitlets>=4.1.0->ipykernel) (1.14.0)
Collecting ipython-genutils (from traitlets>=4.1.0->ipykernel)
  Using cached https://files.pythonhosted.org/packages/fa/bc/9bd3b5c2b4774d5f33b2d544f1460be9df7df2fe42f352135381c347c69a/ipython_genutils-0.2.0-py2.py3-none-any.whl
Requirement already satisfied: setuptools>=18.5 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (41.2.0)
Requirement already satisfied: pygments in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (2.6.1)
Requirement already satisfied: jedi>=0.10 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (0.17.0)
Requirement already satisfied: backcall in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (0.1.0)
Requirement already satisfied: pickleshare in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (0.7.5)
Requirement already satisfied: pexpect; sys_platform != "win32" in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (4.8.0)
Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython>=5.0.0->ipykernel) (3.0.5)
Requirement already satisfied: parso>=0.7.0 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from jedi>=0.10->ipython>=5.0.0->ipykernel) (0.7.0)
Requirement already satisfied: ptyprocess>=0.5 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pexpect; sys_platform != "win32"->ipython>=5.0.0->ipykernel) (0.6.0)
Requirement already satisfied: wcwidth in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=5.0.0->ipykernel) (0.1.9)
Installing collected packages: jupyter-core, jupyter-client, ipython, ipykernel, ipython-genutils
Successfully installed ipykernel-5.2.1 ipython-7.14.0 ipython-genutils-0.2.0 jupyter-client-6.1.3 jupyter-core-4.6.3
WARNING: You are using pip version 19.2.3, however version 20.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip3 install traitlets 
Requirement already satisfied: traitlets in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (4.3.3)
Requirement already satisfied: ipython-genutils in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from traitlets) (0.2.0)
Requirement already satisfied: decorator in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from traitlets) (4.0.11)
Requirement already satisfied: six in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from traitlets) (1.14.0)
WARNING: You are using pip version 19.2.3, however version 20.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip3 ipython 
ERROR: unknown command "ipython"
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip3 install ipython 
Requirement already satisfied: ipython in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (7.14.0)
Requirement already satisfied: jedi>=0.10 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython) (0.17.0)
Requirement already satisfied: traitlets>=4.2 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython) (4.3.3)
Requirement already satisfied: pickleshare in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython) (0.7.5)
Requirement already satisfied: backcall in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython) (0.1.0)
Requirement already satisfied: pexpect; sys_platform != "win32" in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython) (4.8.0)
Requirement already satisfied: setuptools>=18.5 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython) (41.2.0)
Requirement already satisfied: pygments in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython) (2.6.1)
Requirement already satisfied: decorator in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython) (4.0.11)
Requirement already satisfied: appnope; sys_platform == "darwin" in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython) (0.1.0)
Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from ipython) (3.0.5)
Requirement already satisfied: parso>=0.7.0 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from jedi>=0.10->ipython) (0.7.0)
Requirement already satisfied: six in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from traitlets>=4.2->ipython) (1.14.0)
Requirement already satisfied: ipython-genutils in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from traitlets>=4.2->ipython) (0.2.0)
Requirement already satisfied: ptyprocess>=0.5 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from pexpect; sys_platform != "win32"->ipython) (0.6.0)
Requirement already satisfied: wcwidth in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython) (0.1.9)
WARNING: You are using pip version 19.2.3, however version 20.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip3 install jupyter_client 
Requirement already satisfied: jupyter_client in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (6.1.3)
Requirement already satisfied: traitlets in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from jupyter_client) (4.3.3)
Requirement already satisfied: pyzmq>=13 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from jupyter_client) (19.0.0)
Requirement already satisfied: tornado>=4.1 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from jupyter_client) (5.0)
Requirement already satisfied: jupyter-core>=4.6.0 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from jupyter_client) (4.6.3)
Requirement already satisfied: python-dateutil>=2.1 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from jupyter_client) (2.8.1)
Requirement already satisfied: six in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from traitlets->jupyter_client) (1.14.0)
Requirement already satisfied: ipython-genutils in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from traitlets->jupyter_client) (0.2.0)
Requirement already satisfied: decorator in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from traitlets->jupyter_client) (4.0.11)
WARNING: You are using pip version 19.2.3, however version 20.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip3 install jupyter_core 
Requirement already satisfied: jupyter_core in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (4.6.3)
Requirement already satisfied: traitlets in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from jupyter_core) (4.3.3)
Requirement already satisfied: decorator in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from traitlets->jupyter_core) (4.0.11)
Requirement already satisfied: ipython-genutils in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from traitlets->jupyter_core) (0.2.0)
Requirement already satisfied: six in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from traitlets->jupyter_core) (1.14.0)
WARNING: You are using pip version 19.2.3, however version 20.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip3 install ipython_genutils 
Requirement already satisfied: ipython_genutils in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (0.2.0)
WARNING: You are using pip version 19.2.3, however version 20.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip install ipykernel 
Collecting ipykernel
  Using cached ipykernel-5.2.1-py3-none-any.whl (118 kB)
Collecting ipython>=5.0.0
  Using cached ipython-7.14.0-py3-none-any.whl (782 kB)
Collecting jupyter-client
  Using cached jupyter_client-6.1.3-py3-none-any.whl (106 kB)
Collecting traitlets>=4.1.0
  Using cached traitlets-4.3.3-py2.py3-none-any.whl (75 kB)
Requirement already satisfied: appnope; platform_system == "Darwin" in ./opt/anaconda3/lib/python3.7/site-packages (from ipykernel) (0.1.0)
Requirement already satisfied: tornado>=4.2 in ./opt/anaconda3/lib/python3.7/site-packages (from ipykernel) (6.0.3)
Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in ./opt/anaconda3/lib/python3.7/site-packages (from ipython>=5.0.0->ipykernel) (3.0.3)
Requirement already satisfied: pygments in ./opt/anaconda3/lib/python3.7/site-packages (from ipython>=5.0.0->ipykernel) (2.5.2)
Requirement already satisfied: pickleshare in ./opt/anaconda3/lib/python3.7/site-packages (from ipython>=5.0.0->ipykernel) (0.7.5)
Requirement already satisfied: jedi>=0.10 in ./opt/anaconda3/lib/python3.7/site-packages (from ipython>=5.0.0->ipykernel) (0.14.1)
Requirement already satisfied: setuptools>=18.5 in ./opt/anaconda3/lib/python3.7/site-packages (from ipython>=5.0.0->ipykernel) (46.0.0.post20200309)
Requirement already satisfied: decorator in ./opt/anaconda3/lib/python3.7/site-packages (from ipython>=5.0.0->ipykernel) (4.4.1)
Requirement already satisfied: pexpect; sys_platform != "win32" in ./opt/anaconda3/lib/python3.7/site-packages (from ipython>=5.0.0->ipykernel) (4.8.0)
Requirement already satisfied: backcall in ./opt/anaconda3/lib/python3.7/site-packages (from ipython>=5.0.0->ipykernel) (0.1.0)
Collecting jupyter-core>=4.6.0
  Using cached jupyter_core-4.6.3-py2.py3-none-any.whl (83 kB)
Requirement already satisfied: python-dateutil>=2.1 in ./opt/anaconda3/lib/python3.7/site-packages (from jupyter-client->ipykernel) (2.8.1)
Requirement already satisfied: pyzmq>=13 in ./opt/anaconda3/lib/python3.7/site-packages (from jupyter-client->ipykernel) (18.1.1)
Requirement already satisfied: six in ./opt/anaconda3/lib/python3.7/site-packages (from traitlets>=4.1.0->ipykernel) (1.14.0)
Requirement already satisfied: ipython-genutils in ./opt/anaconda3/lib/python3.7/site-packages (from traitlets>=4.1.0->ipykernel) (0.2.0)
Requirement already satisfied: wcwidth in ./opt/anaconda3/lib/python3.7/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=5.0.0->ipykernel) (0.1.8)
Requirement already satisfied: parso>=0.5.0 in ./opt/anaconda3/lib/python3.7/site-packages (from jedi>=0.10->ipython>=5.0.0->ipykernel) (0.5.2)
Requirement already satisfied: ptyprocess>=0.5 in ./opt/anaconda3/lib/python3.7/site-packages (from pexpect; sys_platform != "win32"->ipython>=5.0.0->ipykernel) (0.6.0)
Installing collected packages: traitlets, ipython, jupyter-core, jupyter-client, ipykernel
Successfully installed ipykernel-5.2.1 ipython-7.14.0 jupyter-client-6.1.3 jupyter-core-4.6.3 traitlets-4.3.3
```
2. Then open the Jupyter again, Notebook will work normal
<br>jupyter kernal keeps dying #1892(Comment of takluyver commented on Nov 15, 2016)
<br>https://github.com/jupyter/notebook/issues/1892




Jupiter Notebook cannot package folium
<br>https://stackoverflow.com/questions/60387988/jupiter-notebook-cannot-package-folium
<br>No module named 'gensim' but already installed it
<br>https://stackoverflow.com/questions/60318511/no-module-named-gensim-but-already-installed-it
<br>Using Virtual Environments in Jupyter Notebook and Python
<br>https://janakiev.com/blog/jupyter-virtual-envs/
<br>python-visualization/folium
<br>https://github.com/python-visualization/folium
<br>python-visualization/folium Python 3 support #21
<br>https://github.com/python-visualization/folium/pull/21


