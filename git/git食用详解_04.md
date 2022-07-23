<center>Git 实习生的杀手</center>

# Git分支操作

![image-20220723173633710](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207231736863.png)

## 4.1 什么是分支

​	在版本控制过程中，同时推进多个任务，为了每个人物，我们就可以创建每个任务的的单独分支。使用分支意味着程序员可以把自己的工作从开发主线上分离开来，开发自己的分支时，不会影响主线分支的运行。（分支底层其实也是指针的引用）

![image-20220723173849773](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207231738807.png)

## 4.2 分支的好处

- 同时并行推进多个功能开发，提高开发效率。
- 各个分支再开发过程中，如果有一个分支开发失败，不会对其它分支有任何影响。失败的分支删除重修开始即可。

## 4.3分支的操作



| 命令名称             | 作用                         |
| -------------------- | ---------------------------- |
| git branch 分支名    | 创建分支                     |
| git branch -v        | 查看分支                     |
| git checkout 分支名  | 切换分支                     |
| git merge 指定分支名 | 把指定的分支合并到当前分支上 |

### 4.3.1查看分支

**基础语法**

**git branch -v** 

```c#
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git branch -v
* master 637aa14 3//*指向当前分支
```

### 4.3.2创建分支

**基础语法**

**git branch 分支名**

```c#
//创建分支
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git branch hot-fix
//查看分支
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git branch -v
  hot-fix 637aa14 3//创建的新分支，并将主分支master的内容复制了一份
* master  637aa14 3 
```

### 4.3.3修改分支

```c#
//在hot-fix分支上做修改
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (hot-fix)
$ vim xiaoying.txt
//添加到暂存区
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (hot-fix)
$ git add xiaoying.txt
//提交到本地库
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (hot-fix)
$ git commit -m "hot-fix 2" xiaoying.txt
[hot-fix 992a98c] hot-fix 2
 1 file changed, 1 insertion(+), 1 deletion(-)
//查看分支
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (hot-fix)
$ git branch -v
* hot-fix 992a98c hot-fix 2 //可看到hot-fix分支已更新到最新一次提交的版本和注释信息
  master  637aa14 3         //与上一次查看分支可看出来未做任何改变
```

### 4.3.4 切换分支

**基础语法**

**git checkou**

```c#
//切换分支
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (hot-fix)
$ git checkout master
Switched to branch 'master'
//查看分支
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git branch -v
  hot-fix 992a98c hot-fix 2
* master  637aa14 3//可看到指针指向matser，切换成功
```

## 4.3.5 合并分支

**基础语法**

git merge 指定分支名

```c#
//将分支hot-fix合并到当前分支上
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git merge hot-fix
Updating 637aa14..992a98c
Fast-forward
 xiaoying.txt | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)//一个文件改变，2行新增，2行删除
```

## 4.3.6 产生冲突

#### 冲突产生表现：后状态为MERGING

```c#
//hot-fix和master分支文件都修改后，将hot-fix分支合并到master分支
//先切换到master分支
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (hot-fix)
$ git checkout master
Switched to branch 'master'
//将hot-fix合并到当前分支
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
$ git merge hot-fix
Auto-merging hello.txt
CONFLICT (content): Merge conflict in xiaoying.txt
Automatic merge failed; fix conflicts and then commit the result.//表示自动合并失败
//产生冲突，此时显示（master丨MERGING），表示合并中，即在合并但是是还没有合并完
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master|MERGING)
 //此时查看文件内容
$ cat hello.txt
hello git! hello atguigu! 2222222222222
hello git! hello atguigu! 3333333333333
hello git! hello atguigu!
hello git! hello atguigu!
hello git! hello atguigu!
hello git! hello atguigu!
hello git! hello atguigu!
hello git! hello atguigu!
hello git! hello atguigu!
hello git! hello atguigu!
hello git! hello atguigu!
hello git! hello atguigu!
hello git! hello atguigu!
hello git! hello atguigu!
<<<<<<< HEAD
hello git! hello atguigu! master test
hello git! hello atguigu!
========
hello git! hello atguigu!
hello git! hello atguigu! hot fix test
>>>>>>> hot fix
```

#### 冲突产生原因：

​	合并分支时，两个分支在同一个文件的同一个位置有两套完全不同的修改。Git无法替我们决定使用哪一套。***此时必须人为决定新代码内容。***

```c#
//查看状态
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master|MERGING)
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)//表示可以使用命令中止合并

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   hello.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

### 4.3.7 解决冲突

1. #### 编辑有冲突的文件，删除特殊符号，决定要使用的内容

   特殊符号：***<<<<<<<HEAD 当前分支代码*** \=\=\=\=\=\=\=\= 合并过来的代码 >>>>>>>hot-fix

   ```c#
   $ cat hello.txt
   hello git! hello atguigu! 2222222222222
   hello git! hello atguigu! 3333333333333
   hello git! hello atguigu!
   hello git! hello atguigu!
   hello git! hello atguigu!
   hello git! hello atguigu!
   hello git! hello atguigu!
   hello git! hello atguigu!
   hello git! hello atguigu!
   hello git! hello atguigu!
   hello git! hello atguigu!
   hello git! hello atguigu!
   hello git! hello atguigu!
   hello git! hello atguigu!
   <<<<<<< HEAD
   hello git! hello atguigu! master test
   hello git! hello atguigu!
   ========
   hello git! hello atguigu!
   hello git! hello atguigu! hot fix test
   >>>>>>> hot fix
   ```

2. #### 添加到暂存区

   ```c#
   Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master|MERGING)
   $ git add hello.txt
   ```

3. #### 提交到本地库（注意：此时使用git commit命令不能带文件名）

   ```c#
   //若带了文件名
   Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master|MERGING)
   $ git commit -m "merge test" xiaoying.txt
   fatal: cannot do a partial commit during a merge.
   //正确提交
   Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master|MERGING)
   $ git commit -m "merge test"
   [master 3ee3154] merge test
   //GERGING消失，回到了正常状态
   Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/test (master)
   ```

   

## 4.4创建分支和切换分支图解

![image-20220723221000063](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207232210197.png)

 

master、hot-fix 其实都是指向具体版本记录的指针。当前所在的分支，其实是由HEAD决定的。所以创建分支的本质就是多创建一个指针。

HEAD 如果指向master，那么我们现在就在master 分支上。

HEAD 如果执行hotfix，那么我们现在就在hotfix 分支上。

所以切换分支的本质就是移动HEAD 指针。