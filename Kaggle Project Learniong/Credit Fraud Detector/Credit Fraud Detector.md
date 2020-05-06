# Credit Fraud Detector

## Enviroment Build:
1.Download the note book and dataset from Kaggle
<br>Credit Fraud Detector
<br>https://www.kaggle.com/janiobachmann/credit-fraud-dealing-with-imbalanced-datasets/notebook

2.Notbook was written in Python3, So Choose the  Base(Root) Python3 enviromet in Anaconda, then launch the 
Jupyter note book.

3.install required package in Anaconda. incliude:tensorflow, tensorflow estimate, seaborn, matplotlib.

4.Use conda to install imbalanced-learn 
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

5. Solve the Kernel running error:
<br>__init__() 

