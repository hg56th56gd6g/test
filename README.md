# 说明

## 加密

1.一对rsa公私钥,服务器拿私钥,公钥发给客户端(客户端发一个get请求,此连接保持存活)

2.客户端生成一个aes256密钥,使用公钥加密发给服务器

3.所有的加密数据(会写经过加密)都用这个密钥进行aes256加密

## 帐号

uid是帐号唯一不会变的标识,是int值,代表帐号注册时已注册人数(例如第一个帐号注册的uid是0),在数据库里以字符串形式储存

帐号注册时只需要密码,用户名之类的可以让用户自己写进个人主页

用户自己的主页,博客可以高度自定义,即让用户自己写html,公开一些api,用户可以调用它们来改善自己的主页,博客,比如在主页里插入博客列表

## 域名

所有不是"oiers.org"的域名统一解析到"oiers.org",包括"api.oiers.org"(前后端分离这个可以不解析到oiers.org)

## 文章

文章是以uid和文章名来标识的,所以每个用户的文章名不能有重复

评论是在文章的基础上以id标识的,仅在同一文章内不重复

## 其他

编码统一utf8

返回格式统一为json

返回的code统一0为成功,否则失败

所有json的键都是字符串

如果请求有多余的值,会忽略而不是报错

token没必要加密,因为不管加密或不加密,只要token被拿到了直接传过来就行

# 初始化

## 1.

### 请求

|路径|https://api.oiers.org/encrypt/get_key|
|--|--|
|方法|get|
|内容格式|无内容|
|其他要求|如果有加密数据需要传输,则初始化是必须的,返回json里的公钥需要储存|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|如果成功,则是公钥,否则是失败信息|str|

## 2.

### 请求

|路径|https://api.oiers.org/encrypt/send_key|
|--|--|
|方法|post|
|内容格式|经过公钥加密的aes256密钥|
|其他要求|aes256密钥需要随机生成,以后的加密数据都要用这个加密解密,这一步完了公钥就不用储存了|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|信息,直接显示即可|str|

# 帐号相关

## 注册帐号

### 请求

|路径|https://api.oiers.org/account/register|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|需要初始化|

|键|值|值类型|
|--|--|--|
|password|密码(加密)|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|如果成功,则是uid,否则是失败信息|str|

## 登录帐号

### 请求

|路径|https://api.oiers.org/account/login|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|先初始化|

|键|值|值类型|
|--|--|--|
|uid|用户uid|str|
|password|密码(加密)|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|如果成功,则是token,否则是失败信息|str|

## 使当前token失效

### 请求

|路径|https://api.oiers.org/account/logout|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|先登录|

|键|值|值类型|
|--|--|--|
|token|登录获取的token|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|信息,显示即可|str|

## 注销帐号

### 请求

|路径|https://api.oiers.org/account/cancel|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|先登录|

|键|值|值类型|
|--|--|--|
|token|登录获取的token|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|信息,显示即可|str|

## 更换密码

### 请求

|路径|https://api.oiers.org/account/change_password|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|先登录|

|键|值|值类型|
|--|--|--|
|old|旧密码(加密)|str|
|token|登录获取的token|str|
|new|新密码(加密)|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|信息,直接显示即可|str|

# 用户数据相关

## 获取个人信息(只读)

### 请求

|路径|https://api.oiers.org/user/get_rdata|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|先登录|

|键|值|值类型|
|--|--|--|
|token|登录获取的token(加密)|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|如果成功,则是用户信息(json),否则是失败信息|obj/str|

|键|值|值类型|
|--|--|--|
|uid|用户uid|str|
|time|注册时间(单位秒,以python的time.time()为标准)|str|

## 获取个人信息(可写)

### 请求

|路径|https://api.oiers.org/user/get_wdata|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|先登录|

|键|值|值类型|
|--|--|--|
|token|登录获取的token(加密)|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|如果成功,则是用户信息(json),否则是失败信息|obj/str|

|键|值|值类型|
|--|--|--|
|name|用户名(用来代替某些地方如评论区的uid)|str|
|domain|用户自定义域名列表|list|

## 更新个人可写的信息

### 请求

|路径|https://api.oiers.org/user/update|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|先登录|

|键|值|值类型|
|--|--|--|
|token|登录获取的token(加密)|str|
|name|用户名|str|
|domain|用户自定义域名列表|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|信息,显示即可|str|

## 获取用户信息(公开)

### 请求

|路径|https://api.oiers.org/user/get_adata|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|无|

|键|值|值类型|
|--|--|--|
|uid|用户uid|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|如果成功,则是用户公开的信息,否则是失败信息|obj/str|

|键|值|值类型|
|--|--|--|
|name|用户名|str|

## 用户主页

https://\<自定义域名\>/user/\<uid\>/

# 文章相关

## 获取用户文章列表

### 请求

|路径|https://api.oiers.org/blog/get_blogs|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|无|

|键|值|值类型|
|--|--|--|
|uid|被获取文章列表的uid|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|如果成功,则是该uid的文章名列表,否则是失败信息|list/str|

## 获取文章数据

### 请求

|路径|https://api.oiers.org/blog/get|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|无|

|键|值|值类型|
|--|--|--|
|uid|被获取指定文章的uid|str|
|name|文章名|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|如果成功,则是文章信息(格式由用户决定,一般直接显示即可),否则是失败信息|str|

## 更新文章数据(如果不存在则添加文章)

### 请求

|路径|https://api.oiers.org/blog/update|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|先登录|

|键|值|值类型|
|--|--|--|
|name|文章名|str|
|token|登录获取的token|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|信息,直接显示即可|str|

## 删除文章

### 请求

|路径|https://api.oiers.org/blog/delete|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|先登录|

|键|值|值类型|
|--|--|--|
|name|文章名|str|
|token|登录获取的token|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|信息,直接显示即可|str|

## 文章url

https://\<自定义域名\>/user/\<uid\>/blog/\<文章名\>/

# 评论区相关

## 获取文章的评论区信息

### 请求

|路径|https://api.oiers.org/comment/get|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|无|

|键|值|值类型|
|--|--|--|
|uid|发表此文章的用户uid|str|
|name|文章名|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|如果成功,则是该文章的评论列表(每一项是一个obj),否则是失败信息|list/str|

|键|值|值类型|
|--|--|--|
|id|标识这个评论的id(只在单个文章内不重复)|str|
|uid|评论者uid|str|
|data|评论字符串|str|
|time|评论时间(单位秒,以python的time.time()为标准)|str|

## 添加评论

### 请求

|路径|https://api.oiers.org/comment/add|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|先登录|

|键|值|值类型|
|--|--|--|
|uid|发表此文章的文章的用户uid|str|
|name|文章名|str|
|token|登录获取的token(加密)|str|
|data|评论信息(字符串即可,其他的(评论时间等)由服务器生成)|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|如果成功,则是评论id,否则是失败信息|str|

## 删除评论

### 请求

|路径|https://api.oiers.org/comment/del|
|--|--|
|方法|post|
|内容格式|json|
|其他要求|先登录|

|键|值|值类型|
|--|--|--|
|uid|发表此文章的文章的用户uid|str|
|name|文章名|str|
|token|登录获取的token(加密)|str|
|id|评论id(只能删自己的)|str|

### 响应

|键|值|值类型|
|--|--|--|
|code|状态码|int|
|data|信息,显示即可|str|

# 待补充
