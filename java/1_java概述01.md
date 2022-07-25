[TOC]



# 一、Java概述

## 1.1 什么是程序

程序：计算机执行某些操作或解决某个问题而编写的一系列==有序指令的集合==

------

## 1.2 Java诞生小故事

创始人是[ 詹姆斯·高斯林](https://zh.wikipedia.org/wiki/詹姆斯·高斯林)

- 1990 sun公司启动绿色计划
- 1992 创建oka（橡树语言）
- 1994 gosling参加硅谷大会，演示Java功能，震惊世界
- ==1995sun正式发布java第一个版本==
- 2009年甲骨文公司宣布正式收购sun。2011发布Java7
- ==Java8 11为长期维护版本，也是公司最常用版本==

## 1.3 Java技术体系平台

| Java SE（Java Standard Edition）==标准版==                   |
| ------------------------------------------------------------ |
| 支持桌面级应用（如Windows下的应用程序）的Java平台，提供了完整的Java核心API，此版本以前成为J2SE |
| Java EE（Java Enterprise Edition）==企业版==                 |
| 是为开发企业环境下的应用程序提供的一套解决方案。该技术体系中包含的技术如：Servlet、Jsp等，主要针对于Web应用程序开发。版本以前成为J2EE |
| Java ME（Java Micro Edition）==小型版==                      |
| 针对Java程序运行再移动终端（手机端、PDA）上的平台，对Java API有所精简，并加入了针对移动终端的支持，此版本以前称为J2ME |

------

## 1.4 Java重要特点

1. Java语言是面向对象的（oop）

2. Java语言是健壮的。Java的强类型机制、异常处理、垃圾的自动收集等是Java程序健壮的重要保证

3. Java语言是跨平台性的。

   ==跨平台性：一个编译后的.class文件可以在不同的操作系统运行==

4. Java语言是解释型的

   解释性语言：JavaScript，php，Java

   编程性语言：c/c++

   区别：解释性语言，编译后的代码，不能直接被机器运行，需要解释器来执行

   ​			编程性语言，编译后的代码，可以直接被机器运行

------

## 1.5 Java的运行机制及过程

### 1.5.1 Java语言的特点：跨平台性

![202207220105246](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207221024439.png)

​		 说明：因为有了JVM，同一个Java程序在三个不同的操作系统中都可以执行，这样Java程序就有了跨平台性。

### 1.5.2 Java核心机制——Java虚拟机【JVM Java virtual machine】

1. JVM是一个虚拟的计算机，具有指令集并使用不同的储存区域。负责执行指令，管理数据、内存、寄存器，包含==JDK中==
2. 对于不同平台有不同的虚拟机。
3. Java虚拟机屏蔽了底层运行平台的差别，实现了“==一次编译，到处运行==”

​	![202207220105283](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207221025297.png)

------

## 1.6什么是JDK、JRE

### 1.6.1 JDK基本介绍

1. JDK的全程（Java Development Kit ==Java开发工具包==）

   JDK=JRE+Java的开发工具【Java，javac，javadoc，javap等】

2. JDK是提供给开发人员使用的，其中包括了Java的开发工具，也包括了JRE。所以安装了JDK就不用再单独安装JRE了。

### 1.6.2 JRE的基本介绍

1. JRE（Java Runtime Environment ==Java运行环境==）

2. JRE=JAM+Java核心类库【类】

3. 包含Java虚拟机（JVM Java Virtual Machine）和Java程序所需的核心类库等，如果想要运行一个开发好的Java程序，计算机中只需要安装JRE即可。

   ------

### 1.6.3JDK、JRE、JVM的包含关系

1. JDK=JRE+开发工具集（例如javac，Java编译工具等）
2. JRE=JVM+Java SE标准类库（java核心类库）
3. 如果只是想运行开发好的.class文件只需要JRE

------

## 1.7安装JDK和配置环境变量

### 1.7.1安装JDK

- ### 我不傻就不写安装步骤了，注意事项：

  1. 企业常用多用==JDK8和JDK11==，但是在官网下载这两个版本的话天杀的甲骨文还要你注册账号和登录。
  2. ==安装的时候把全部东西安装上，安装目录或者路径不要带有中文，空格和特殊符号，正常点纯英文就好了==
  3. 提示安装JRE时可以选择不装也可以选择装，空间够就装，不缺那点空间

------

### ==1.7.2 配置环境变量==

1. ## 在环境变量中增加JAVA_HOME环境变量，指向你按照的jdk目录，例如：H:\Program\Java\jdk8

2. 编辑path环境变量，增加%JAVA_HOME%\bin

3. 如果jdk目录下的lib里有dt.jar和tools.jar，就增加CLASSPATH变量，输入值

   .;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;
   
   ------

## 1.8 工具选择

### 1.8.1 如何选择开发工具

​	我们先使用简单的文本编辑器[sublime](https://www.sublimetext.com/download)，到对了Java有一定了解后，再使用智障的idea开发工具

### 1.8.2 为什么呢

方便更深刻理解Java技术，培养代码感，培养手感。【面试时往往需要手写代码】

------

### 1.8.3 sublime4的汉化与激活

#### 	安装这么简单的事就不写了，直接上汉化

首先先安装Package Control，第一次安装是没有的，按Shift + Ctrl + P 或者点击工具栏中的Tools再点击Command Palette呼出命令窗口，

​	![202207220105144](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207221025375.png)

然后输入install 在列出的选中选择：Install Package Control即开始安装，安装完后会弹出一个窗口

![202207220105173](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207221025760.png)

这样就是安装成功了，然后在 Preferences 菜单下可以看到 Package Control 这个选项了

![202207220105206](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207221025788.png)

点击它然后在弹出来的窗口输入install package选择Package Control:install Package 稍等数弹出命令框，然后输入ChineseLocalizations选择第一个。

![image-20220725170342144](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207251703207.png)

------

#### 激活

1）在软件的安装目录找到 sublime_text.exe 文件。

2）这里推荐使用： 【[hexed](https://hexed.it/)】 在线十六进制编辑器，打开 sublime_text.exe 文件。

3）然后查找以下字节并且替换（不同的软件版本替换的内容略有不同，一定要看好软件版本）。

|     软件版本 4113 依此替换下方 2 组字节！      |
| :--------------------------------------------: |
|      C3 C6 01 00 C3 替换为 C3 C6 01 01 C3      |
|      51 31 C0 88 05 替换为 51 b0 01 88 05      |
|       软件版本：4107 替换下方 1 组字节！       |
|   80 38 00 74 2C 49 替换为 FE 00 90 74 2C 49   |
|        软件版本：4126替换下方一组字节！        |
| 80 78 05 00 0f 94 c1更改为c6 40 05 01 48 85 c9 |

4）先粘贴要搜索的字节，然后替换！最后保存并替换旧的 sublime_text.exe 文件即可！（最好保存一下原文件）

------

#### 增加GBK编码

在Package Control:install Package弹出的命令框中输入convertToUTF8进行搜索安装，然后点击File，找到如下图

![image-20220725170759127](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207251707200.png)
