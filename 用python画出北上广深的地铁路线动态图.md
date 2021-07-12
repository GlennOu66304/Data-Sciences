# 用python画出北上广深的地铁路线动态图

## Can not see the shanghai and shenzheng map 

You need to head to the code snipte, and change the code below to the lattitude and lotitude of the shanghai and shengzheng 

```
subway.py
.add_schema(
        baidu_ak = '2RZvKw6tc8vq2dEvVA6GaSMLM09uebVZ', #百度地图开发应用appkey
        center = [121.4762, 31.2297], #当前视角的中心点
        zoom = 10, #当前视角的缩放比例
        is_roam = True, #开启鼠标缩放和平移漫游
    )
```
## Bug:百度未授权使用地图API，可能是因为您提供的密钥不是有效的百度LBS开放平台密钥，或此密钥未对本应用的百度地图JavaScriptAPI授权。您可以访问如下网址了解如何获取有效的密钥
[百度未授权使用地图API，可能是因为您提供的密钥不是有效的百度LBS开放平台密钥，或此密钥未对本应用的百度地图JavaScriptAPI授权。您可以访问如下网址了解如何获取有效的密钥](https://ask.shopxo.net/article/142)

## package issue:
[pyecharts](https://pyecharts.org/#/zh-cn/quickstart)    
[NameError: name 'requests' is not defined [closed]](https://stackoverflow.com/questions/26895371/nameerror-name-requests-is-not-defined)
[Python 库引用提示：name ‘json‘ is not defined. 问题解决办法](https://blog.csdn.net/qq_38161040/article/details/91410095)  
[百度地图开发mapStyle个性化地图styleJson的配色解决方案](https://blog.csdn.net/weixin_41290949/article/details/106379134)   


## resource:
[用python画出北上广深的地铁路线动态图](https://mp.weixin.qq.com/s/zoIPvS04VP45y_eKT4lxJg)   

