# Scrapy Python Craw
## Coding Enviroment Building
1. Python enviroment:
<br>https://github.com/GlennOu66304/Data-Sciences/blob/master/Python%20And%20Python%20Craw/1.Python.md

2. Anaconda enviroment:
<br>https://github.com/GlennOu66304/Data-Sciences/blob/master/3.Data%20Analysis%20in%20Python%20Enviroment%20.md

3. Scrapy Installation
```
(base) ztdeMacBook-Air:~ zt$ conda install -c conda-forge scrapy
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /opt/anaconda3

  added / updated specs:
    - scrapy


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    automat-20.2.0             |             py_0          30 KB  conda-forge
    bcrypt-3.1.7               |   py37h9bfed18_1          42 KB  conda-forge
    conda-4.8.3                |   py37hc8dfbb8_1         3.0 MB  conda-forge
    constantly-15.1.0          |             py_0           9 KB  conda-forge
    cssselect-1.1.0            |             py_0          18 KB  conda-forge
    hyperlink-19.0.0           |     pyh9f0ad1d_0          35 KB  conda-forge
    incremental-17.5.0         |             py_0          14 KB  conda-forge
    parsel-1.5.2               |             py_0          14 KB  conda-forge
    pyasn1-0.4.8               |             py_0          53 KB  conda-forge
    pyasn1-modules-0.2.7       |             py_0          60 KB  conda-forge
    pydispatcher-2.0.5         |             py_1          12 KB  conda-forge
    pyhamcrest-2.0.2           |             py_0          29 KB  conda-forge
    python_abi-3.7             |          1_cp37m           4 KB  conda-forge
    queuelib-1.5.0             |     pyh9f0ad1d_0          13 KB  conda-forge
    scrapy-1.6.0               |           py37_0         323 KB
    service_identity-18.1.0    |             py_0          12 KB  conda-forge
    twisted-20.3.0             |   py37h9bfed18_0         5.0 MB  conda-forge
    w3lib-1.20.0               |             py_0          21 KB  conda-forge
    zope.interface-5.1.0       |   py37h9bfed18_0         288 KB  conda-forge
    ------------------------------------------------------------
                                           Total:         9.0 MB

The following NEW packages will be INSTALLED:

  automat            conda-forge/noarch::automat-20.2.0-py_0
  bcrypt             conda-forge/osx-64::bcrypt-3.1.7-py37h9bfed18_1
  constantly         conda-forge/noarch::constantly-15.1.0-py_0
  cssselect          conda-forge/noarch::cssselect-1.1.0-py_0
  hyperlink          conda-forge/noarch::hyperlink-19.0.0-pyh9f0ad1d_0
  incremental        conda-forge/noarch::incremental-17.5.0-py_0
  parsel             conda-forge/noarch::parsel-1.5.2-py_0
  pyasn1             conda-forge/noarch::pyasn1-0.4.8-py_0
  pyasn1-modules     conda-forge/noarch::pyasn1-modules-0.2.7-py_0
  pydispatcher       conda-forge/noarch::pydispatcher-2.0.5-py_1
  pyhamcrest         conda-forge/noarch::pyhamcrest-2.0.2-py_0
  python_abi         conda-forge/osx-64::python_abi-3.7-1_cp37m
  queuelib           conda-forge/noarch::queuelib-1.5.0-pyh9f0ad1d_0
  scrapy             pkgs/main/osx-64::scrapy-1.6.0-py37_0
  service_identity   conda-forge/noarch::service_identity-18.1.0-py_0
  twisted            conda-forge/osx-64::twisted-20.3.0-py37h9bfed18_0
  w3lib              conda-forge/noarch::w3lib-1.20.0-py_0
  zope.interface     conda-forge/osx-64::zope.interface-5.1.0-py37h9bfed18_0

The following packages will be UPDATED:

  conda                       pkgs/main::conda-4.8.3-py37_0 --> conda-forge::conda-4.8.3-py37hc8dfbb8_1


Proceed ([y]/n)? 


Downloading and Extracting Packages
pyasn1-0.4.8         | 53 KB     | ##################################### | 100% 
service_identity-18. | 12 KB     | ##################################### | 100% 
parsel-1.5.2         | 14 KB     | ##################################### | 100% 
incremental-17.5.0   | 14 KB     | ##################################### | 100% 
conda-4.8.3          | 3.0 MB    | ##################################### | 100% 
queuelib-1.5.0       | 13 KB     | ##################################### | 100% 
hyperlink-19.0.0     | 35 KB     | ##################################### | 100% 
zope.interface-5.1.0 | 288 KB    | ##################################### | 100% 
pyhamcrest-2.0.2     | 29 KB     | ##################################### | 100% 
scrapy-1.6.0         | 323 KB    | ##################################### | 100% 
pyasn1-modules-0.2.7 | 60 KB     | ##################################### | 100% 
constantly-15.1.0    | 9 KB      | ##################################### | 100% 
bcrypt-3.1.7         | 42 KB     | ##################################### | 100% 
automat-20.2.0       | 30 KB     | ##################################### | 100% 
pydispatcher-2.0.5   | 12 KB     | ##################################### | 100% 
cssselect-1.1.0      | 18 KB     | ##################################### | 100% 
w3lib-1.20.0         | 21 KB     | ##################################### | 100% 
python_abi-3.7       | 4 KB      | ##################################### | 100% 
twisted-20.3.0       | 5.0 MB    | ##################################### | 100% 
Preparing transaction: done
Verifying transaction: | WARNING conda.core.path_actions:verify(963): Unable to create environments file. Path not writable.
  environment location: /Users/zt/.conda/environments.txt

done
Executing transaction: done
(base) ztdeMacBook-Air:~ zt$ 
```
conda-forge / packages / scrapy
<br>https://anaconda.org/conda-forge/scrapy
