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
Build from the source code - advanced method
<br>https://xgboost.readthedocs.io/en/latest/build.html#building-on-osx
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
CMake command not found in OSX build environment #2175
<br>https://github.com/travis-ci/travis-ci/issues/2175

2.Create the build/ directory 
```
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % cd /Users/zhanghuiqiao/xgboost 
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro xgboost % mkdir build  
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro xgboost % cd build  
```
'cd /Users/zhanghuiqiao/xgboost'  Very important!!!, You need to find location of CMakeLists.txt. Then move to there start directory build.
<br>CMake Error buildir" does not appear to contain CMakeLists.txt
<br>https://stackoverflow.com/questions/57342558/cmake-error-buildir-does-not-appear-to-contain-cmakelists-txt

3.invoke CMake. After invoking CMake, you can build XGBoost with make:
```
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro build % cmake .. 
-- The CXX compiler identification is AppleClang 11.0.3.11030032
-- The C compiler identification is AppleClang 11.0.3.11030032
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++ - works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc - works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- CMake version 3.17.2
-- Performing Test XGBOOST_MM_PREFETCH_PRESENT
-- Performing Test XGBOOST_MM_PREFETCH_PRESENT - Success
-- Performing Test XGBOOST_BUILTIN_PREFETCH_PRESENT
-- Performing Test XGBOOST_BUILTIN_PREFETCH_PRESENT - Success
-- xgboost VERSION: 1.1.0
-- Setting build type to 'Release' as none was specified.
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- Found OpenMP_C: -Xclang -fopenmp (found version "3.1") 
-- Found OpenMP_CXX: -Xclang -fopenmp (found version "3.1") 
-- Found OpenMP: TRUE (found version "3.1")  
-- Found OpenMP_C: -Xclang -fopenmp (found version "3.1") 
-- Found OpenMP_CXX: -Xclang -fopenmp (found version "3.1") 
-- Looking for clock_gettime in rt
-- Looking for clock_gettime in rt - not found
-- Looking for fopen64
-- Looking for fopen64 - not found
-- Looking for C++ include cxxabi.h
-- Looking for C++ include cxxabi.h - found
-- Looking for nanosleep
-- Looking for nanosleep - found
-- Looking for backtrace
-- Looking for backtrace - found
-- backtrace facility detected in default set of libraries
-- Found Backtrace: /Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/usr/include  
-- Check if the system is big endian
-- Searching 16 bit integer
-- Looking for sys/types.h
-- Looking for sys/types.h - found
-- Looking for stdint.h
-- Looking for stdint.h - found
-- Looking for stddef.h
-- Looking for stddef.h - found
-- Check size of unsigned short
-- Check size of unsigned short - done
-- Searching 16 bit integer - Using unsigned short
-- Check if the system is big endian - little endian
-- /Users/zhanghuiqiao/xgboost/dmlc-core/cmake/build_config.h.in -> include/dmlc/build_config.h
-- Performing Test SUPPORT_MSSE2
-- Performing Test SUPPORT_MSSE2 - Success
DMLC_ROOT point to /Users/zhanghuiqiao/xgboost/rabit/../dmlc-core
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/zhanghuiqiao/xgboost/build
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro build % make -j4 
Scanning dependencies of target dmlc
[  4%] Building CXX object dmlc-core/CMakeFiles/dmlc.dir/src/io.cc.o
[  4%] Building CXX object dmlc-core/CMakeFiles/dmlc.dir/src/data.cc.o
[  4%] Building CXX object dmlc-core/CMakeFiles/dmlc.dir/src/recordio.cc.o
[  4%] Building CXX object dmlc-core/CMakeFiles/dmlc.dir/src/config.cc.o
[  5%] Building CXX object dmlc-core/CMakeFiles/dmlc.dir/src/io/line_split.cc.o
[  6%] Building CXX object dmlc-core/CMakeFiles/dmlc.dir/src/io/recordio_split.cc.o
[  7%] Building CXX object dmlc-core/CMakeFiles/dmlc.dir/src/io/indexed_recordio_split.cc.o
[  9%] Building CXX object dmlc-core/CMakeFiles/dmlc.dir/src/io/input_split_base.cc.o
[ 10%] Building CXX object dmlc-core/CMakeFiles/dmlc.dir/src/io/filesys.cc.o
[ 11%] Building CXX object dmlc-core/CMakeFiles/dmlc.dir/src/io/local_filesys.cc.o
[ 12%] Linking CXX static library libdmlc.a
[ 12%] Built target dmlc
Scanning dependencies of target rabit_empty
Scanning dependencies of target rabit_mock_static
Scanning dependencies of target rabit
Scanning dependencies of target objxgboost
[ 13%] Building CXX object rabit/CMakeFiles/rabit_empty.dir/src/engine_empty.cc.o
[ 14%] Building CXX object rabit/CMakeFiles/rabit.dir/src/allreduce_base.cc.o
[ 15%] Building CXX object rabit/CMakeFiles/rabit_mock_static.dir/src/allreduce_base.cc.o
[ 17%] Building CXX object src/CMakeFiles/objxgboost.dir/c_api/c_api.cc.o
[ 18%] Building CXX object rabit/CMakeFiles/rabit_empty.dir/src/c_api.cc.o
[ 19%] Linking CXX static library librabit_empty.a
[ 19%] Built target rabit_empty
[ 20%] Building CXX object rabit/CMakeFiles/rabit.dir/src/allreduce_robust.cc.o
[ 21%] Building CXX object rabit/CMakeFiles/rabit_mock_static.dir/src/allreduce_robust.cc.o
Scanning dependencies of target rabit_base
[ 22%] Building CXX object rabit/CMakeFiles/rabit_base.dir/src/allreduce_base.cc.o
[ 23%] Building CXX object src/CMakeFiles/objxgboost.dir/c_api/c_api_error.cc.o
[ 25%] Building CXX object rabit/CMakeFiles/rabit_base.dir/src/engine_base.cc.o
[ 26%] Building CXX object src/CMakeFiles/objxgboost.dir/common/common.cc.o
[ 27%] Building CXX object rabit/CMakeFiles/rabit.dir/src/engine.cc.o
[ 28%] Building CXX object rabit/CMakeFiles/rabit_mock_static.dir/src/engine_mock.cc.o
[ 29%] Building CXX object rabit/CMakeFiles/rabit_base.dir/src/c_api.cc.o
[ 30%] Building CXX object src/CMakeFiles/objxgboost.dir/common/hist_util.cc.o
[ 31%] Building CXX object rabit/CMakeFiles/rabit.dir/src/c_api.cc.o
[ 32%] Linking CXX static library librabit_base.a
[ 32%] Built target rabit_base
Scanning dependencies of target rabit_mock
[ 34%] Building CXX object rabit/CMakeFiles/rabit_mock.dir/src/allreduce_base.cc.o
[ 35%] Building CXX object rabit/CMakeFiles/rabit_mock_static.dir/src/c_api.cc.o
[ 36%] Linking CXX static library librabit.a
[ 36%] Built target rabit
[ 37%] Building CXX object rabit/CMakeFiles/rabit_mock.dir/src/allreduce_robust.cc.o
[ 38%] Linking CXX static library librabit_mock_static.a
[ 38%] Built target rabit_mock_static
[ 39%] Building CXX object src/CMakeFiles/objxgboost.dir/common/host_device_vector.cc.o
[ 40%] Building CXX object src/CMakeFiles/objxgboost.dir/common/io.cc.o
[ 42%] Building CXX object rabit/CMakeFiles/rabit_mock.dir/src/engine_mock.cc.o
[ 43%] Building CXX object rabit/CMakeFiles/rabit_mock.dir/src/c_api.cc.o
[ 44%] Building CXX object src/CMakeFiles/objxgboost.dir/common/json.cc.o
[ 45%] Building CXX object src/CMakeFiles/objxgboost.dir/common/probability_distribution.cc.o
[ 46%] Linking CXX shared library librabit_mock.dylib
[ 47%] Building CXX object src/CMakeFiles/objxgboost.dir/common/survival_util.cc.o
[ 47%] Built target rabit_mock
[ 48%] Building CXX object src/CMakeFiles/objxgboost.dir/common/timer.cc.o
[ 50%] Building CXX object src/CMakeFiles/objxgboost.dir/common/version.cc.o
[ 51%] Building CXX object src/CMakeFiles/objxgboost.dir/data/data.cc.o
[ 52%] Building CXX object src/CMakeFiles/objxgboost.dir/data/ellpack_page.cc.o
[ 53%] Building CXX object src/CMakeFiles/objxgboost.dir/data/ellpack_page_source.cc.o
[ 54%] Building CXX object src/CMakeFiles/objxgboost.dir/data/simple_dmatrix.cc.o
[ 55%] Building CXX object src/CMakeFiles/objxgboost.dir/data/sparse_page_dmatrix.cc.o
[ 56%] Building CXX object src/CMakeFiles/objxgboost.dir/data/sparse_page_raw_format.cc.o
[ 57%] Building CXX object src/CMakeFiles/objxgboost.dir/gbm/gblinear.cc.o
[ 59%] Building CXX object src/CMakeFiles/objxgboost.dir/gbm/gblinear_model.cc.o
[ 60%] Building CXX object src/CMakeFiles/objxgboost.dir/gbm/gbm.cc.o
[ 61%] Building CXX object src/CMakeFiles/objxgboost.dir/gbm/gbtree.cc.o
[ 62%] Building CXX object src/CMakeFiles/objxgboost.dir/gbm/gbtree_model.cc.o
[ 63%] Building CXX object src/CMakeFiles/objxgboost.dir/learner.cc.o
[ 64%] Building CXX object src/CMakeFiles/objxgboost.dir/linear/linear_updater.cc.o
[ 65%] Building CXX object src/CMakeFiles/objxgboost.dir/linear/updater_coordinate.cc.o
[ 67%] Building CXX object src/CMakeFiles/objxgboost.dir/linear/updater_shotgun.cc.o
[ 68%] Building CXX object src/CMakeFiles/objxgboost.dir/logging.cc.o
[ 69%] Building CXX object src/CMakeFiles/objxgboost.dir/metric/elementwise_metric.cc.o
[ 70%] Building CXX object src/CMakeFiles/objxgboost.dir/metric/metric.cc.o
[ 71%] Building CXX object src/CMakeFiles/objxgboost.dir/metric/multiclass_metric.cc.o
[ 72%] Building CXX object src/CMakeFiles/objxgboost.dir/metric/rank_metric.cc.o
[ 73%] Building CXX object src/CMakeFiles/objxgboost.dir/metric/survival_metric.cc.o
[ 75%] Building CXX object src/CMakeFiles/objxgboost.dir/objective/aft_obj.cc.o
[ 76%] Building CXX object src/CMakeFiles/objxgboost.dir/objective/hinge.cc.o
[ 77%] Building CXX object src/CMakeFiles/objxgboost.dir/objective/multiclass_obj.cc.o
[ 78%] Building CXX object src/CMakeFiles/objxgboost.dir/objective/objective.cc.o
[ 79%] Building CXX object src/CMakeFiles/objxgboost.dir/objective/rank_obj.cc.o
[ 80%] Building CXX object src/CMakeFiles/objxgboost.dir/objective/regression_obj.cc.o
[ 81%] Building CXX object src/CMakeFiles/objxgboost.dir/predictor/cpu_predictor.cc.o
[ 82%] Building CXX object src/CMakeFiles/objxgboost.dir/predictor/predictor.cc.o
[ 84%] Building CXX object src/CMakeFiles/objxgboost.dir/tree/constraints.cc.o
[ 85%] Building CXX object src/CMakeFiles/objxgboost.dir/tree/param.cc.o
[ 86%] Building CXX object src/CMakeFiles/objxgboost.dir/tree/split_evaluator.cc.o
[ 87%] Building CXX object src/CMakeFiles/objxgboost.dir/tree/tree_model.cc.o
[ 88%] Building CXX object src/CMakeFiles/objxgboost.dir/tree/tree_updater.cc.o
[ 89%] Building CXX object src/CMakeFiles/objxgboost.dir/tree/updater_colmaker.cc.o
[ 90%] Building CXX object src/CMakeFiles/objxgboost.dir/tree/updater_histmaker.cc.o
[ 92%] Building CXX object src/CMakeFiles/objxgboost.dir/tree/updater_prune.cc.o
[ 93%] Building CXX object src/CMakeFiles/objxgboost.dir/tree/updater_quantile_hist.cc.o
[ 94%] Building CXX object src/CMakeFiles/objxgboost.dir/tree/updater_refresh.cc.o
[ 95%] Building CXX object src/CMakeFiles/objxgboost.dir/tree/updater_skmaker.cc.o
[ 96%] Building CXX object src/CMakeFiles/objxgboost.dir/tree/updater_sync.cc.o
[ 96%] Built target objxgboost
Scanning dependencies of target runxgboost
[ 97%] Building CXX object CMakeFiles/runxgboost.dir/src/cli_main.cc.o
[ 98%] Linking CXX executable ../xgboost
[ 98%] Built target runxgboost
Scanning dependencies of target xgboost
[100%] Linking CXX shared library ../lib/libxgboost.dylib
[100%] Built target xgboost
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro build % 
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
