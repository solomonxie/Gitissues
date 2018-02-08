# 总之对于这个我唯一认定的事就是：Python里要是弄不明白编码，那这个语言就放弃吧！

下面是目前收获到的一些内容，没写完，再议吧。。。

首先要在文件第一行写上`编码声明`

```
#coding:utf-8
```
![caso sgs c 01 bdrip 1280x720 x264_aac -0005](https://user-images.githubusercontent.com/14041622/35965316-80a9ebd0-0cf5-11e8-8f96-ab103fbb0243.jpg)

编码声明的格式其实很随意的，coding=utf-8, -_\- Coding:Utf-8 -_\- 等等都行，  
Python只识别关键的字。  
如果不写编码声明，那么文件中出现的任何中文都会报错：  
`SyntaxError: Non-ASCII character '\xe5' in file xx.py on line 2, 
    but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details`





Python 2.x 系列对中文真是弱爆了，查了巨多的文献，还是不那么明了。  
本来想要练习开发个什么小程序，结果全都被扼杀在编码的坑里了。  
随便搜一搜"Python 编码"就知道，所有作者们都遇到了一毛一样的问题。。。  
据说，

```
除非把整个编码系统从古至今的历史熟透，各编码的原理通透，
相互之间的转换了熟于胸，Python的这个坑是跨不过去的。小看了这小玩意儿！  
```

下面开始正式研究下吧，争取能做到practical。

这是原始汉字数据：

```
chinese = '你好' # 普通中文字符串
uni = u'你好' # 字符串前加u代表转换为unicode变量类型
```
# 研究一个原始的中文字符串






数组中必须所有的元素都是字符串，且都是统一的编码才能合并，否则报错。统一后，如果全是unicode，那么返回的字符串就是unicode；如果元素全是str，那么返回的就是str。
![i wore makeup for a week and here s what happened screenshot 4](https://user-images.githubusercontent.com/14041622/35965325-8b453b12-0cf5-11e8-9b34-5785dd35dd0e.png)



