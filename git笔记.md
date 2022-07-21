# Git使用遇坑笔记

- ## 基本配置（提前生成并保存好需要的的SSH公钥并连接，例如GitHub，[gitee](https://gitee.com/help/articles/4181#article-header0)）

  ```c
  //进入相应的目录打开git bash
  1. git config --global user.name "xxx" //设置提交时的用户名
  2. git config --global user.email "xxx@xxx.com" //设置提交时的邮箱
  3. git config --list//查看环境变量
  4. git init//初始化新本地库，初始化后，在当前目录下会出现一个名为.git 的文件夹
  5. git add "文件名" //将文件添加到Git 暂存区
  6. git commit -m "****"//提交暂存区内容到版本库(本地库)中并添加注释
  7. git remote add origin [自己的ssh地址]//关联本地库与远程库
  8. git pull --rebase origin master//合并
  9. git push -u origin master //第一次推送   
     git push origin master 
     git push -u origin master -f //强制提交 
  
  ```

  

- ## 同步操作

  ```c
  1.git add ""   //添加当前目录的文件到暂存区
  2.git commit -m "***"    //提交暂存区内容到版本库(本地库)中并添加注释
  3.git push origin master //推送本地仓库的内容到origin这个远程仓库的master分支
    git push -f origin master//强制推送
  ```

- ------

  ## 同步出问题时

  - ### 出现nothing to commit, working tree clean时

  ```c
  1. rm -rf .git/
  2. git init
  3. git remote add origin [ssh链接]
  4. git add [文件]
  5. git commit -m “Commit message”
  6. git push -f origin master
  ```

------

- ### 出现master | REBASE 1/1

  ```c
  //被困在一个变基的中间
  1.git rebase --continue//用于完成该过程
  2.git rebase --abort//用于退出 rebase 过程而没有任何风险
  //如果git rebase --continue | --skip | --abort还是不行
  3.git reset --hard HEAD~1 //git reset --hard将丢弃您的工作，只有在您知道自己在做什么时才使用它！
  ```

  
