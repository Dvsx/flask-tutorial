## 前言
这是flask基础教程的运行方法
## 命令
```
先激活虚拟环境
venv\Scripts\activate
然后运行
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run
```
## 问题
### 为什么要使用虚拟环境？
随着你的 Python 项目越来越多，你会发现不同的项目会需要 不同的版本的 Python 库。同一个 Python 库的不同版本可能不兼容。虚拟环境可以为每一个项目安装独立的 Python 库，这样就可以隔离不同项目之间的 Python 库，也可以隔离项目与操作系统之间的 Python 库。
