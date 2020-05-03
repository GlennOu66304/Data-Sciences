# Chinese Music Downlaod

## 0.Enviromet:
1.Github projec(Project Source)
<br>2.Loacal project(Place to store your project)
<br>3.Terminal(Run your python code)
<br>4.Quick Player(Play your downloas MP3 Music)

## 1.Clone the project from github (gitzip download single fold)
Data-Sciences/Python And Python Craw/API_Music_Download-master 2/
<br>https://github.com/GlennOu66304/Data-Sciences/tree/master/Python%20And%20Python%20Craw/API_Music_Download-master%202

## 2.Move to the projet to install 'requirements.txt'
```
cd /Users/zhanghuiqiao/Downloads/API_Music_Download-master 2
Users/zhanghuiqiao/Downloads/API_Music_Download-master 2 % pip3 install -r requirements.txt
```
## 3. Run "Main.py" To download the certain musci
```
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro Spiders % python3 /Users/zhanghuiqiao/Downloads/API_Music_Download-master\ 2/Spiders/main.py
******************************欢迎来到小豪音乐下载助手******************************
[请输入歌曲/FM的网址链接]:http://5sing.kugou.com/yc/4094372.html
此链接为5sing音乐
此音乐下载地址为:https://wsaudiobssdlbig.kugou.com/2005031238/CBN9x3LkkH3kmnfyy3b9PA/1588567116/bss/extname/wsaudio/03c7f489585b6d86a0c3eb804f2ee0d6.mp3
```
## Resources:
Henryhaohao/API_Music_Download
<br>https://github.com/Henryhaohao/API_Music_Download

## Comment if you run "Henryhaohao/API_Music_Download" encounter Error, Try to fix code in main.py to :
```
from API_music_cloud163 import get_music_cloud163
from API_music_1ting import get_music_1ting
from API_music_5sing import get_music_5sing
from API_music_365 import get_music_365
from API_music_changba import get_music_changba
from API_music_doubanFM import get_music_doubanfm
from API_music_echo import get_music_echo
from API_music_jiutian import get_music_jiutian
from API_music_kugou import get_music_kugou
from API_music_kuwo import get_music_kuwo
from API_music_lizhiFM import get_music_lizhifm
from API_music_migu import get_music_migu
from API_music_mvbox import get_music_mvbox
from API_music_qianqian_baidu import get_music_qianqian
from API_music_qq import get_music_qq
from API_music_xiami import get_music_xiami
from API_music_ximalayaFM import get_music_ximalayafm
```
