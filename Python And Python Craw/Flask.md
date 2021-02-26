## Python Flask

### Bug fixing:Error: Failed to find Flask application or factory in module "flaskr". Use "FLASK_APP=flaskr:name to specify one.

Change the _init_.py to the __init.__.py

### Can not run the http://127.0.0.1:5000/

You need to add the hello at the end of the url link:
http://127.0.0.1:5000/hello

### Create the ven and indtall the Flask:
Create the ven
```
mkdir flask-tutorial
cd flask-tutorial
sudo apt-get install python3-venv
python3 -m venv venv
```
install the Flask
```
. venv/bin/activate
pip install Flask
```
[Installation](https://flask.palletsprojects.com/en/1.1.x/installation/)  

### Learning Resouce: 
[Python3 Flask Tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/#tutorial)  
[Installation](https://flask.palletsprojects.com/en/1.1.x/installation/#installation)  
[Quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstarthttps://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart)  
[怎样才能彻底掌握Flask？怎样的学习顺序比较合理？](https://www.zhihu.com/question/20135205)  
