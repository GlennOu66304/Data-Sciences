# Credit Fraud Detector

## Enviroment Build:
### 1.Download the note book and dataset from Kaggle
<br>Credit Fraud Detector
<br>https://www.kaggle.com/janiobachmann/credit-fraud-dealing-with-imbalanced-datasets/notebook

### 2.Notbook was written in Python3, So Choose the  Base(Root) Python3 enviromet in Anaconda, then launch the 
Jupyter note book.

### 3.install required package in Anaconda. incliude:tensorflow, tensorflow estimate, seaborn, matplotlib.

### 4.Use conda to install imbalanced-learn 
```
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % conda install -c conda-forge imbalanced-learn
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /Users/zhanghuiqiao/opt/anaconda3

  added / updated specs:
    - imbalanced-learn


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    imbalanced-learn-0.6.2     |             py_0          95 KB  conda-forge
    ------------------------------------------------------------
                                           Total:          95 KB

The following NEW packages will be INSTALLED:

  imbalanced-learn   conda-forge/noarch::imbalanced-learn-0.6.2-py_0
  python_abi         conda-forge/osx-64::python_abi-3.7-1_cp37m

The following packages will be UPDATED:

  conda                       pkgs/main::conda-4.8.3-py37_0 --> conda-forge::conda-4.8.3-py37hc8dfbb8_1


Proceed ([y]/n)? y


Downloading and Extracting Packages
imbalanced-learn-0.6 | 95 KB     | ##################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % 
```
conda-forge / packages / imbalanced-learn 0.6.2
<br>https://anaconda.org/conda-forge/imbalanced-learn

### 5. Solve the Kernel running error:
1.<br>__init__() error, Solved with :
```
# --upgrade option can be used as downgrade also ;)
$ pip3 install --upgrade --user prompt_toolkit==2.0.10
Collecting prompt_toolkit==2.0.10
  Downloading https://files.pythonhosted.org/packages/87/61/2dfea88583d5454e3a64f9308a686071d58d59a55db638268a6413e1eb6d/prompt_toolkit-2.0.10-py3-none-any.whl (340kB)
     |████████████████████████████████| 348kB 27kB/s 
Requirement already satisfied, skipping upgrade: wcwidth in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from prompt_toolkit==2.0.10) (0.1.9)
Requirement already satisfied, skipping upgrade: six>=1.9.0 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from prompt_toolkit==2.0.10) (1.14.0)
Installing collected packages: prompt-toolkit
Successfully installed prompt-toolkit-2.0.10
WARNING: You are using pip version 19.2.3, however version 20.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % pip install --upgrade pip 
Collecting pip
  Downloading pip-20.1-py2.py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 18 kB/s 
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 20.0.2
    Uninstalling pip-20.0.2:
      Successfully uninstalled pip-20.0.2
Successfully installed pip-20.1
(base) zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % 

```
TypeError: __init__() got an unexpected keyword argument 'inputhook' #11962(Comment of lijunzh commented on Dec 3, 2019)
<br>https://github.com/ipython/ipython/issues/11962

2.Ratio erro
<br>imblearn.over_sampling.SMOTE
<br>https://imbalanced-learn.readthedocs.io/en/stable/generated/imblearn.over_sampling.SMOTE.html

## Final Version:
1. Code file is here
<br>Credit Fraud __ Dealing with Imbalanced Datasets.ipynb
<br>https://github.com/GlennOu66304/Data-Sciences/blob/master/Kaggle%20Project%20Learniong/Credit%20Fraud%20Detector/Credit%20Fraud%20%20__%20Dealing%20with%20Imbalanced%20Datasets.ipynb

2. Dataset is here:
<br>Credit Card Fraud Detection (Dataset is 150 MB, Can not be uploaded into Github, So you need to Zip it or provide dataset link here.)
<br>https://www.kaggle.com/mlg-ulb/creditcardfraud
