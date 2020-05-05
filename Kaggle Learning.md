# Kaggle Learning

## Plotly in Python
```
pip install plotly==4.6.0
Collecting plotly==4.6.0
  Using cached https://files.pythonhosted.org/packages/15/90/918bccb0ca60dc6d126d921e2c67126d75949f5da777e6b18c51fb12603d/plotly-4.6.0-py2.py3-none-any.whl
Collecting retrying>=1.3.3 (from plotly==4.6.0)
  Using cached https://files.pythonhosted.org/packages/44/ef/beae4b4ef80902f22e3af073397f079c96969c69b2c7d52a57ea9ae61c9d/retrying-1.3.3.tar.gz
Requirement already satisfied: six in /Users/zhanghuiqiao/anaconda3/lib/python3.7/site-packages (from plotly==4.6.0) (1.12.0)
Building wheels for collected packages: retrying
  Building wheel for retrying (setup.py) ... done
  Stored in directory: /Users/zhanghuiqiao/Library/Caches/pip/wheels/d7/a9/33/acc7b709e2a35caa7d4cae442f6fe6fbf2c43f80823d46460c
Successfully built retrying
Installing collected packages: retrying, plotly
Successfully installed plotly-4.6.0 retrying-1.3.3
Note: you may need to restart the kernel to use updated packages.
```
Installation
<br>https://plotly.com/python/getting-started/

## Trouble installing xgboost
### Build from the source code - advanced method
#### 1.Obtain libomp from Homebrew:
```
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % brew install libomp 
Warning: libomp 10.0.0 is already installed and up-to-date
To reinstall 10.0.0, run `brew reinstall libomp`
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % brew reinstall libomp 
==> Reinstalling libomp 
==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles/bottles/libomp-10.0
Already downloaded: /Users/zhanghuiqiao/Library/Caches/Homebrew/downloads/501cf6d0c117188648e8e6878bd923f674a1c15f83a6c2a71e4e29b2c8254287--libomp-10.0.0.catalina.bottle.tar.gz
==> Pouring libomp-10.0.0.catalina.bottle.tar.gz
🍺  /usr/local/Cellar/libomp/10.0.0: 9 files, 1.3MB
```
#### 2.Now clone the repository:
```
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % git clone --recursive https://github.com/dmlc/xgboost
Cloning into 'xgboost'...
remote: Enumerating objects: 31, done.
remote: Counting objects: 100% (31/31), done.
remote: Compressing objects: 100% (24/24), done.
remote: Total 35420 (delta 12), reused 17 (delta 6), pack-reused 35389
Receiving objects: 100% (35420/35420), 15.39 MiB | 24.00 KiB/s, done.
Resolving deltas: 100% (21034/21034), done.
Submodule 'cub' (https://github.com/NVlabs/cub) registered for path 'cub'
Submodule 'dmlc-core' (https://github.com/dmlc/dmlc-core) registered for path 'dmlc-core'
Submodule 'rabit' (https://github.com/dmlc/rabit) registered for path 'rabit'
Cloning into '/Users/zhanghuiqiao/xgboost/cub'...
remote: Enumerating objects: 32680, done.        
remote: Total 32680 (delta 0), reused 0 (delta 0), pack-reused 32680        
Receiving objects: 100% (32680/32680), 16.57 MiB | 23.00 KiB/s, done.
Resolving deltas: 100% (28620/28620), done.
Cloning into '/Users/zhanghuiqiao/xgboost/dmlc-core'...
remote: Enumerating objects: 24, done.        
remote: Counting objects: 100% (24/24), done.        
remote: Compressing objects: 100% (20/20), done.        
remote: Total 5984 (delta 4), reused 8 (delta 2), pack-reused 5960        
Receiving objects: 100% (5984/5984), 1.55 MiB | 23.00 KiB/s, done.
Resolving deltas: 100% (3627/3627), done.
Cloning into '/Users/zhanghuiqiao/xgboost/rabit'...
remote: Enumerating objects: 5, done.        
remote: Counting objects: 100% (5/5), done.        
remote: Compressing objects: 100% (4/4), done.        
remote: Total 3586 (delta 0), reused 2 (delta 0), pack-reused 3581        
Receiving objects: 100% (3586/3586), 1.07 MiB | 33.00 KiB/s, done.
Resolving deltas: 100% (2343/2343), done.
Submodule path 'cub': checked out 'c3cceac115c072fb63df1836ff46d8c60d9eb304'
Submodule path 'dmlc-core': checked out '5df8305fe699d3b503d10c60a231ab0223142407'
Submodule path 'rabit': checked out '4fb34a008db6437c84d1877635064e09a55c8553'
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % mkdir build 
```
#### 3.Create the build/ directory and invoke CMake. After invoking CMake, you can build XGBoost with make:
1.brew install cmake 
```
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % brew install cmake 
Updating Homebrew...
To restore the stashed changes to /usr/local/Homebrew run:
  'cd /usr/local/Homebrew && git stash pop'
To restore the stashed changes to /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core run:
  'cd /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core && git stash pop'
==> Homebrew has enabled anonymous aggregate formulae and cask analytics.
Read the analytics documentation (and how to opt-out) here:
  https://docs.brew.sh/Analytics
No analytics have been recorded yet (or will be during this `brew` run).

==> Homebrew is run entirely by unpaid volunteers. Please consider donating:
  https://github.com/Homebrew/brew#donations
==> Auto-updated Homebrew!
Updated 1 tap (homebrew/core).
==> New Formulae
claws-mail          earthly             kumactl             redo
duktape             fargatecli          openfast            vlmcsd
==> Updated Formulae
youtube-dl ✔               goreleaser                 questdb
abcmidi                    graphviz                   quickjs
ace                        gromacs                    re-flex
acpica                     gtk+3                      re2
adios2                     hlint                      rebar3
angular-cli                ipython                    recon-ng
ansible@2.8                ircd-hybrid                redex
asciidoctorj               ispc                       redis
ask-cli                    kibana                     restview
astrometry-net             kind                       rswift
audacious                  ledger                     s3ql
aws-elasticbeanstalk       libfabric                  scamper
azcopy                     libgr                      scrcpy
babel                      libmypaint                 seal
balena-cli                 libsass                    sec
ballerina                  libzt                      shyaml
bandwhich                  liquidctl                  simgrid
blackbox                   liquigraph                 snakemake
bluepill                   livestreamer               snapcraft
caddy                      maxwell                    softhsm
cfengine                   mednafen                   sonarqube
cfn-lint                   mercurial                  sonarqube-lts
cglm                       meson-internal             spoof-mac
charm-tools                mkvtomp4                   sqlmap
chronograf                 mkvtoolnix                 ssh-audit
clamav                     mlpack                     sslyze
clib                       molecule                   stellar-core
cmark                      monero                     step
cmark-gfm                  mps-youtube                supervisor
conserver                  mu                         swagger-codegen@2
coturn                     mutt                       swift
ctemplate                  ncmpc                      swiftformat
dhall-bash                 nef                        tarsnapper
django-completion          neomutt                    termius
dnstwist                   nicovideo-dl               termtosvg
dosbox-x                   nift                       terragrunt
dxpy                       node-build                 theharvester
efl                        nss                        tmux
ejdb                       nyx                        tmuxinator
elasticsearch              ocrmypdf                   tmuxinator-completion
emscripten                 oha                        tomcat-native
exploitdb                  oniguruma                  trezor-agent
faas-cli                   open-babel                 tvnamer
faudio                     openconnect                uhd
fb-client                  openimageio                unoconv
fibjs                      osc                        vault
filebeat                   osquery                    vdirsyncer
fluent-bit                 packer                     verilator
flyway                     passpie                    vit
futhark                    pastebinit                 wallpaper
fwup                       pdftk-java                 watchman
gatsby-cli                 peru                       weboob
gdal                       phpstan                    weechat
gegl                       pidgin                     whatmp3
gimme                      pius                       wpscan
git-annex                  pnpm                       wtf
git-quick-stats            ponysay                    wxmac
github-release             pre-commit                 yaegi
glib-openssl               procs                      yle-dl
glslang                    proj                       yosys
golang-migrate             pyinstaller                z
googler                    pyside                     zabbix
gopass                     python-markdown            znc
==> Deleted Formulae
deis                                     deisctl

==> Downloading https://mirrors.ustc.edu.cn/homebrew-bottles/bottles/cmake-3.17.
######################################################################## 100.0%
==> Pouring cmake-3.17.2.catalina.bottle.tar.gz
==> Caveats
Emacs Lisp files have been installed to:
  /usr/local/share/emacs/site-lisp/cmake
==> Summary
🍺  /usr/local/Cellar/cmake/3.17.2: 6,156 files, 58MB
```
2.Create the build/ directory 
```
```



### Official Guide:
Better XGBoost installation on Mac OSX? #4477
<br>https://github.com/dmlc/xgboost/issues/4477
<br>Installation Guide¶
<br>https://xgboost.readthedocs.io/en/latest/build.html
Trouble installing xgboost on OSX 10.14 #4949
<br>https://github.com/dmlc/xgboost/issues/4949


### py-xgboost install 
How to install and use XGBOOST library in anaconda on Windows 10 ?
<br>https://www.youtube.com/watch?v=lxDEkTuaz_k
<br>Install XGBoost on Mac - Machine Learning Tutorial Walkthrough
<br>https://www.youtube.com/watch?v=GjMMQ2q_Qxo
<br>py-xgboost 
<br>https://anaconda.org/anaconda/py-xgboost
<br>Write a Python program using Anaconda Prompt or terminal
<br>https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-prompt-mac
