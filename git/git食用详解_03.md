 ====================================================================================================Git=========================================================================================================

​				   											  工作必用，实习生的杀手

------

# 三、Git常用命令

| **命令**                               | **作用**                                                   |
| -------------------------------------- | ---------------------------------------------------------- |
| git config --global user.name [用户名] | 设置用户签名名称                                           |
| git config --global user.email [邮箱]  | 设置用户签名邮箱                                           |
| git init                               | 初始化本地库                                               |
| git status                             | 查看本地库状态                                             |
| git add [文件名]                       | 添加到暂存库                                               |
| git commit -m "文件注释" [文件名]      | 提交到本地库并注释文件                                     |
| git reflog                             | 查看历史记录                                               |
| git reset --hard [版本号]              | 版本穿梭                                                   |
| git rm --cached <file>                 | 使用命令删除缓存区（暂存区中）的<file>从而取消这个文件版本 |

## 3.1 设置用户签名

### 基本语法

```c
	git config --global user.name [用户名]

	git config --global user.email [邮箱]
    //查看
     cat ~/.gitconfig
    //窗口返回
	[user]
        name = [用户名]
        email = [邮箱]

```

说明：
签名的作用是区分不同操作者身份。用户的签名信息在每一个版本的提交信息中能够看到，以此确认本次提交是谁做的。

==**Git首次安装必须设置一下用户签名，否则无法提交代码。**==
==**※注意**==：这里设置用户签名和将来登录 GitHub（或其他代码托管中心）的账号没有任何关系。

------

## 3.2初始化本地库

### 基本语法

```c#
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test
$ git init   //初始化本地库命令
Initialized empty Git repository in I:/Axiu/Desktop/study/test/.git/

Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ ll -a  //加了’ -a ‘才能看到隐藏目录和文件，也就是 .文件
total 4
drwxr-xr-x 1 Axiu 197609 0 Jul 22 16:28 ./
drwxr-xr-x 1 Axiu 197609 0 Jul 22 16:28 ../
drwxr-xr-x 1 Axiu 197609 0 Jul 22 16:28 .git/  //(.git初始化生成的文件)

```

------

## 3.3查看本地库状态

### 3.3.1首次查看（工作区没有任何文件）

```c#
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git status (查看本地库状态命令)
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)

```

### 3.3.2新增文件（例hello.txt）

![image-20220722153934660](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207221539697.png)

### 3.3.3再次查看（检测未追踪到的文件）

```c#
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        xiaoying.txt

nothing added to commit but untracked files present (use "git add" to track)

```

------



## 3.4添加暂存区

### 3.4.1将工作区的文件添加到暂存区

```c#
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git add hello.txt
warning: LF will be replaced by CRLF in hello.txt.
The file will have its original line endings in your working directory.
```

### 3.4.2查看状态（检测到暂存区有新文件）

```c#
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)//使用命令删除缓存区（暂存区中的）<file>
        new file:   xiaoying.txt
```

------

## 3.5提交本地库

### 3.5.1 将暂存区的文件提交到本地库

```c#
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git commit -m "first" xiaoying.txt
warning: in the working copy of 'xiaoying.txt', LF will be replaced by CRLF the next time Git touches it
[master (root-commit) a568551] first  // a568551是版本号
 1 file changed, 12 insertions(+)     //一个文件被改变，12行内容被插入
 create mode 100644 xiaoying.txt
```

### 3.5.2 查看状态

```c#
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git status
On branch master //当前是主干分支master
nothing to commit, working tree clean //没有东西需要提交，工作树是干净的
 //没有文件需要提交
```

------

## 3.6 修改文件

### 修改文件过程略

### 3.6.1 查看状态

```C
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   xiaoying.txt  //这是红色表示文件没有被追踪（没有被添加到暂存区）

no changes added to commit (use "git add" and/or "git commit -a")

```

### 3.6.2将修改的文件再次添加到暂存区（将文件标记追踪）

```c#
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git add xiaoying.txt
warning: in the working copy of 'xiaoying.txt', LF will be replaced by CRLF the next time Git touches it
```

### 3.6.3 查看状态

```c#
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   xiaoying.txt  //这里边绿了，说明添加到暂存区了
```

### 3.6.4 添加到本地库

```c#
$ git commit -m "2" xiaoying.txt
warning: in the working copy of 'xiaoying.txt', LF will be replaced by CRLF the next time Git touches it
[master cf4b480] 2
 1 file changed, 1 insertion(+)

```

------

## 3.7 历史版本

### 3.7.1查看历史版本

#### 基本语法

- git reflog 查看版本信息
- git log 查看版本详细信息

```c#
//查看历史版本
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git reflog
637aa14 (HEAD -> master) HEAD@{0}: commit: 3
cf4b480 HEAD@{1}: commit: 2
a568551 HEAD@{2}: commit (initial): first
    
//查看版本详细信息
    Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git log
commit a5685513c839951d2c5ab642c1e96c1d07410f5b (HEAD -> master)
Author: Axiu0823 <393189353@qq.com>
Date:   Fri Jul 22 16:59:14 2022 +0800

    first

```

### 3.7.2 版本穿梭

#### 基本语法

- git reset --hard 版本号

```c#
//查看历史版本找版本号
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git reflog
637aa14 (HEAD -> master) HEAD@{0}: commit: 3
cf4b480 HEAD@{1}: commit: 2
a568551 HEAD@{2}: commit (initial): first
    
 //切换到第一个版本 
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git reset --hard a568551
HEAD is now at a568551 first //指针现在指向a568551，即切换成功

 //再次查看历史记录，可看到HEAD指向第一个版本
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git reflog
a568551 (HEAD -> master) HEAD@{0}: reset: moving to a568551
637aa14 HEAD@{1}: commit: 3
cf4b480 HEAD@{2}: commit: 2
a568551 (HEAD -> master) HEAD@{3}: commit (initial): first

 //再次查看文件发现内容已经发生变化
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ cat xiaoying.txt
xiaoying love yangxuewei!!
xiaoying love yangxuewei!!
xiaoying love yangxuewei!!
xiaoying love yangxuewei!!
xiaoying love yangxuewei!!
xiaoying love yangxuewei!!
xiaoying love yangxuewei!!
xiaoying love yangxuewei!!
xiaoying love yangxuewei!!!!
xiaoying love yangxuewei!!!!
xiaoying love yangxuewei!!!!
xiaoying love yangxuewei!!
```

### Git切换版本，底层其实是移动的HEAD 指针，具体原理如下图所示。

![image-20220722180155679](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207221801726.png)
