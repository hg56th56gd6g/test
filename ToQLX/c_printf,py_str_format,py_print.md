# c printf函数

## 原型定义

#include <stdio.h>

```c_cpp
int printf (const char *__format, ...);
```

## 参数

### __format

包含n个格式化标签的字符串

c的字符串是一个uint8指针,从这个指针指向的地址开始,直到一个"\x00"(包括起始地址,不包括"\x00")

这里的const(常量标记)其实没什么用,不仅可以输入预设的字符串(储存在rdata,是它的起始地址指针,即:"String"),还可以输入你自己声明的字符串,甚至只要是一个指针就可以,printf会打印直到"\x00"

### ...

可变参数的意思,需要__format里有几个格式化标签,这里就输入对应的几个参数

例如以十进制打印一个uint:

```c_cpp
printf("%d",123);
//输出"123"
```

打印一个字符串,后面跟百分号,十进制uint:

```c_cpp
printf("%s%%%d","String__",321);
//输出"String__%321"
```

格式化标签很多,还有各种flag~~我也记不全~~,一般常用的记住就行了,其他的需要的时候再查

## 返回值

如果成功,返回写入的字符总数,否则返回负数~~但是一般都不用看返回值~~

# python %格式化字符串

和printf很相似,但有区别

## 用法

```python
str % tuple
#或者
str % value
```

tuple内对象数量需要等于str内格式化标签数量

第二种用法仅适用于只有一个格式化标签时,也可以用只有一个对象的tuple(建议用这个,统一语法)

例如以十进制打印一个int:

```python
"%d" % (123,)
#"123"
```

打印一个字符串,后面跟百分号,十进制int:

```python
"%s%%%d" % ("String__",-321)
#String__%-321
```

格式化标签同样很多,但没有flag什么的~~我还是记不全~~

# python str.format()格式化字符串

跟printf完全不一样了

格式化标签变成了"{}"

~~我用的不多~~

会解析大括号内的内容,然后去参数里找对应对象,最后把它(包括左右大括号)替换成解析完的内容

## 用法

```python
str.format(*args,**kwargs)
```

## 大括号里的内容

### 可以是没有内容

会从0开始,从左到右给每个大括号编号

匹配*args里对应下标的对象

### 或者一个数组下标

即不用自动分配,手动指定编号

匹配*args里对应下标的对象

在同一个字符串内

没有内容不能和数组下标一起用

### 或者一个名称,**<u>不一定要变量名,例如数字开头字母结尾的也可以</u>**

匹配**kwargs里对应key的对象

如果输入多余,不会报错,但如果输入不足则会报错

## 例子

```python
"{}{}{}".format(0,"1",[789])
#01[789]
"{0}{q1qq}{1}".format(0,2,q1qq="1q11")
#01q112
"{0}{3}{01qw}".format(0,1,2,3,4,5,6,**{"qwer":"_qwer","01qw":"01qw__"})
#0301qw__
"{}{}{qwe}{2}".format(0,1,2,3,4,qwe=67,rty=78)
#ValueError: cannot switch from automatic field numbering to manual field specification
```

# python f-string格式化字符串

## ~~需要python3,没用过,感觉不如str.format~~

# python print函数

## 原型定义

flush在python2没有

没有返回值

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

## 参数

### *objects

要打印的对象列表

### sep

用什么分开每个对象,可以不是一个字符,例如没有""或者"-\_-\_-_-"

### end

所有对象打印完后打印这个,可以不是一个字符

### file

写入到什么文件,默认是标准输出

### flush

写入完是否强制刷新文件

## 关于编码

文件有一个"encoding"属性,它指定了文件的编码

如果要打印的对象是unicode,那么print函数会观察文件的这个属性

如果属性不是None,则编码成对应的编码,否则报错

## 关于对象如何打印

除了unicode,其他对象都相当于str(object)

![screen-capture](https://github.com/hg56th56gd6g/test/ToQLX/print_objects.png)

str(object)的返回值被限定为str,如果返回unicode,则使用ascii编码将其编码为字符串

![screen-capture](https://github.com/hg56th56gd6g/test/ToQLX/str_unicode_ascii.png)

![screen-capture](https://github.com/hg56th56gd6g/test/ToQLX/str_unicode_gbk.png)

报错

![screen-capture](https://github.com/hg56th56gd6g/test/ToQLX/str_int_123.png)
