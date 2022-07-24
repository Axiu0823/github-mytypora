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

#### 基本语法

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

#### 基础语法

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

### 6.2.3拉取远程库内容到本地

#### **基本语法**

git pull 远程库地址别名 远程库分支名

```c#
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/note (master)
$ git pull github master
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 1), reused 3 (delta 1), pack reused 0
Unpacking objects: 100% (3/3), done.
From https://github.com/atguiguyueyue/git shTest
* branch master --> FETCH_HEAD
7cb4d02..5dabe6b master --> ori/master
Updating 7cb4d02..5dabe6b
Fast forward
hello.txt | 2
1 file changed, 1 insertion(+), 1 deletion(-）
```

#### 拉取结果：

远程库对于分支最新内容拉取后与当前本地分支直接合并，且自动提交本地库

### 6.2.4克隆远程库到本地

#### **基本语法**

git clone 远程库地址

```
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/新建文件夹
$ git clone https://github.com/Axiu0823/github-mytypora.git
Cloning into 'github-mytypora'...
remote: Enumerating objects: 73, done.
remote: Counting objects: 100% (73/73), done.
remote: Compressing objects: 100% (45/45), done.
remote: Total 73 (delta 30), reused 68 (delta 25), pack-reused 0
Receiving objects: 100% (73/73), 5.94 MiB | 75.00 KiB/s, done.
Resolving deltas: 100% (30/30), done.
```

#### 克隆结果

![image-20220724215941765](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207242159822.png)

克隆成功可以看到目录下生成了目录github-mytypora，进入该目录，可看到有 .git目录，说明本地库已经生成

![image-20220724220210260](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207242202333.png)

使用git branch -v，可看到已经remote被克隆远程库，也就是创建别名了

```c#
Axiu@LAPTOP-F1M9BDPF MINGW64 /i/Axiu/Desktop/study/新建文件夹/github-mytypora (master)
$ git remote -v
origin  https://github.com/Axiu0823/github-mytypora.git (fetch)
origin  https://github.com/Axiu0823/github-mytypora.git (push)
```

#### 总结

clone公开的远程库不需要登录也就是不需要登录凭据

clone会进行：

1. 初始化本地库
2. 创建别名
3. 拉取远程库所有内容



## 6.3 SSH免密登录

我们可以看到这里还有个ssh链接，用ssh链接我们可以进行免密访问操作，并且使用SSH链接的push和pull都会比用https链接快。

![image-20220724221631503](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207242216539.png)

### 6.3.1生成SSH密钥，参考了gitee帮助中心的[怎样生成公钥](https://gitee.com/help/articles/4181)

itee 提供了基于SSH协议的Git服务，在使用SSH协议访问仓库之前，需要先配置好账户/仓库的SSH公钥。

你可以按如下命令来生成 sshkey:

```c#
ssh-keygen -t ed25519 -C "xxxxx@xxxxx.com"  
# Generating public/private ed25519 key pair...
```

> 注意：这里的 `xxxxx@xxxxx.com` 只是生成的 sshkey 的名称，并不约束或要求具体命名为某个邮箱。
> 现网的大部分教程均讲解的使用邮箱生成，其一开始的初衷仅仅是为了便于辨识所以使用了邮箱。

按照提示完成三次回车，即可生成 ssh key。通过查看 `~/.ssh/id_ed25519.pub` 文件内容，获取到你的 public key

```c#
cat ~/.ssh/id_ed25519.pub
# ssh-ed25519 AAAAB3NzaC1yc2EAAAADAQABAAABAQC6eNtGpNGwstc....
```

![SSH生成](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207242221894.png)

### 6.3.2添加SSH公钥

图中第七行可以找到生成的public key保存的目录和文件名称，可以自行进入该目录用cat命令查看public key是多少，复制全部内容后，点击setting进入个人设置

![image-20220724222847088](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207242228121.png)

点击左边列表的SSH and GPG keys，将刚才复制的所有内容粘贴到右边key下面的框中，上面的title可以写刚刚写的邮箱

![image-20220724223048647](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207242230719.png)

### 6.3.3添加成功后

1. 打开 Git Bash。

2. 输入以下内容：

   ```shell
   $ ssh -T git@github.com
   # Attempts to ssh to GitHub
   ```

   您可能会看到类似如下的警告：

   ```shell
   > The authenticity of host 'github.com (IP ADDRESS)' can't be established.
   > RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
   > Are you sure you want to continue connecting (yes/no)?
   ```

3. 验证所看到消息中的指纹是否匹配 [GitHub 的公钥指纹](https://docs.github.com/cn/github/authenticating-to-github/githubs-ssh-key-fingerprints)。 如果是，则输入 `yes`即成功了：

   ```shell
   > Hi username! You've successfully authenticated, but GitHub does not
   > provide shell access.
   ```

   **注意：** 远程命令应以代码 1 退出。

   ### GitHub 的 SSH 密钥指纹

   公钥指纹可用于验证与远程服务器的连接。

   以下是 GitHub 的公钥指纹：

   - `SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8` (RSA)
   - `SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM` (ECDSA)
   - `SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU` (Ed25519)

4. 验证生成的消息包含您的用户名。 如果收到“权限被拒绝”消息，请参阅[“错误：权限被拒绝（公钥）”](https://docs.github.com/cn/articles/error-permission-denied-publickey)。
