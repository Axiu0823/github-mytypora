<center>Git 实习生的杀手</center>

------

# 五、Git团队协作机制

## 5.1 团队内协作

![image-20220724010718129](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207240107171.png)

## 5.2 跨团队协作



![image-20220724011330557](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207240113613.png)

------

# 六、Github操作（Gitee同理）

## 6.1 创建远程库

![image-20220724040724386](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207240407437.png)

![image-20220724041003258](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207240410325.png)

------

## 6.2 远程库操作

### 基础命令表

| 命令名称                       |                                                        |
| :----------------------------- | ------------------------------------------------------ |
| git remote -v                  | 查看当前所有远程库地址和别名                           |
| git remote add 别名 远程库地址 | 连接远程库并创建别名表示                               |
| git push 别名 本地分支         | 推送本地分支上的内容到远程库上与本地分支同名的分支     |
| git clone 远程库地址           | 将远程库的内容克隆到本地                               |
| git pull 别名 远程库分支名     | 讲远程库对于分支最新内容拉下来后与当前本地分支直接合并 |

### 6.2.1 连接远程库并创建别名

基本语法

| git remote -v                  | 查看当前所有远程库地址和别名 |
| :----------------------------- | ---------------------------- |
| git remote add 别名 远程库地址 | 连接远程库并创建别名表示     |

```c#
//查看当前所有远程库地址以及对应别名
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/note (master)
$ git remote -v 
//连接远程库并创建别名表示
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/note (master)
$ git remote add github https://github.com/Axiu0823/github-mytypora.git
//再次查看
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/note (master)
$ git remote -v
github  https://github.com/Axiu0823/github-mytypora.git (fetch)
github  https://github.com/Axiu0823/github-mytypora.git (push)
```

远程库地址是创建好远程库后自动生成的连接，在如图所示的框框中

![image-20220724044137692](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207240441728.png)

------



### 6.2.2 推送本地分支到远程库

基础语法

git push 别名 分支

```c#
//将master分支内容推送到github对应远程库的master分支上
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/note (master)
$ git push github master
Logon failed, use ctrl+c to cancel basic credential prompt.//此时会弹出一个窗口让我们登录
Username for 'https://github.com': Axiu0823
Counting objects: 3, done.
Delta compression using up to 12 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 276 bytes | 276.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/Axiu0823/github-mytypora.git
* [new branch] master --> master  

```

推送会弹出一个登录窗口，上面蓝色选项是用浏览器登录账号，框内是用口令登录

![image-20220724045013593](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207240450634.png)

------

### 6.2.3克隆远程仓库到本地



