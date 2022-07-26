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

### ==1.6.3JDK、JRE、JVM的包含关系==

1. **JDK=JRE+开发工具集（例如javac，Java编译工具等）**
2. **JRE=JVM+Java SE标准类库（java核心类库）**
3. **如果只是想运行开发好的.class文件只需要JRE**

------

## 1.7安装JDK和配置环境变量

### 1.7.2安装JDK

- ### 我不傻就不写安装步骤了，注意事项：

  1. 企业常用多用==JDK8和JDK11==，但是在官网下载这两个版本的话天杀的甲骨文还要你注册账号和登录。
  2. ==安装的时候把全部东西安装上，安装目录或者路径不要带有中文，空格和特殊符号，正常点纯英文就好了==
  3. 提示安装JRE时可以选择不装也可以选择装，空间够就装，不缺那点空间

------

### 1.7.3 配置环境变量的作用

为了在dos的任意目录可以使用java命令以及其他java有关的命令。

### ==1.7.3 配置环境变量==

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

------

## 1.9 Java快速入门

### 1.9.1 编写一个hello.java

```java
//演示Java开发步骤
//1.public class hello表示hello是一个类，是一个public公有的类
//2.hello{}表示一个类的开始和结束
//3.public static void mian(String[] args)表示一个主方法，即我们程序的入口
//4.main(){}的{}表示主方法的开始和结束
//5.System.out.println("hello,world~");表示输出"hello,world~"到屏幕上
//6. “ ; ”表示语句结束
//7.编译后每一个类都对应生成一个.class文件
public class hello{		//public类类名必须与文件名相同					
    //编写一个mian方法
    public static void main(String[] args){   //
        System.out.println("hello,world~");
    }
}
```

 ***PS：使用cmd.exe的话文件要以GBK编码保存,特别是有中文的时候，因为cmd.exe属性里显示当前代码页的编码为GBK，使用windows powershell则不需要。***

![image-20220725111331899](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207261034786.png)

运行时需要先用javac编译.java文件，再执行我们编译后的htllo.class文件，==注意此处不需要加.class后缀==，因为java运行的默认就是我们编写的类，加上了.class反而无法运行，java控制台显示如下

```java
PS I:\Axiu\Desktop\study\javacode> javac hello.java
PS I:\Axiu\Desktop\study\javacode> java hello 
hello,world~
PS I:\Axiu\Desktop\study\javacode> java hello.class
错误: 找不到或无法加载主类 hello.class
```

------

### 1.9.2什么是编译

javac hello.java

1. 有了java源文件，通过编译器可以将其编译成JVM可以识别的字节码文件。
2. 在该源文件目录下，通过javac编译工具对hello.java文件进行编译。
3. 如果程序没有错误，没有任何提示，但在当前目录下会出现一个hello.class文件，该文件称为字节码文件，也是可以执行的java程序。
4. 编译后每一个类都对应生成一个.class文件

### 1.9.3 什么是运行

1. 有了可以执行的java程序（hello.java字节码文件）

2. 通过运行工具java.exe对字节码文件进行执行，本质是.class装载到JVM执行。

   - java程序开发注意事项

     对修改后的hello.java源文件需要重新编译，生成新的.class文件后，再进行执行，才能生效。

------

## ==1.10 java开发规范==

1. Java源文件以 java 为扩展名。源文件的基本组成部分是类(class)，如本类中的Hello类。

2. Java应用程序的执行入口是main()方法。它有固定的书写格式;
   public static void main(String[] args){...}

3. Java语言严格区分大小写。

4. Java方法由一条条语句构成，每个语句以“:”结束。

5. 大括号都是成对出现的，缺一不可。[习惯先写{}再写代码]

6. **一个源文件中最多只能有一个public类。其它类的个数不限。**

7. **如果源文件包含一个public类，则文件名必须按该类名命名!**

  ```java
I:\Axiu\Desktop\study\javacode>javac hello02.java
hello02.java:1: 错误: 类hello01是公共的, 应在名为 hello01.java 的文件中声明
public class hello01{
       ^
1 个错误
  ```

8. 一个源文件中最多只能有一个public类。其它类的个数不限，也可以将main方法写在非public类中，然后指定运行非public 类，这样入口方法就是非public 的main方法。

```java
//代码如下
public class hello01{
	public static void main(String[] args){
		System.out.println("小颖 I love you");
	}
}
class xiaoying{
	public static void main(String[] args){
		System.out.println("hello 小颖");
	}
}
//命令框显示
I:\Axiu\Desktop\study\javacode>javac hello01.java

I:\Axiu\Desktop\study\javacode>java hello01
小颖 I love you

I:\Axiu\Desktop\study\javacode>java xiaoying
hello 小颖
```

------

## 1.11 Java转义字符

### 1.11.1 Java常用的转义字符

- 在命令行点击tab键可以实现自动补全

1. \t :一个制表位，实现对齐的功能

2. \n ：换行符

3. \\\\ ：一个\

4. \\" ："

5. \\' ：一个'

6. \r ：一个回车 

   **PS： \r 是回车，光标挪到当前行最前面，将后面的内容对前面的内容进行逐字覆盖，与“\n”不一样。**

```java
//代码如下：
public class changechar {
	public static void main(String[] args){
// \t :一个制表位，实现对齐的功能
		System.out.println("小颖\t傻宝\t小颖");
// \n ：换行符
		System.out.println("小颖\n傻宝\n小颖");
// \\ ：一个\
		System.out.println("小颖\\傻宝\\小颖");
// \" ："
		System.out.println("我说：\"小颖是一个傻宝，我爱小颖\"");
// \' ：一个'
		System.out.println("我说：\'小颖是一个傻宝，我爱小颖\'");
// \r ：一个回车
		System.out.println("傻宝傻宝\r小颖");
	}

}
//cmd显示：
I:\Axiu\Desktop\study\javacode>java changechar
    //System.out.println("小颖\t傻宝\t小颖");
小颖    傻宝    小颖
	//System.out.println("小颖\n傻宝\n小颖");
小颖
傻宝
小颖
    //System.out.println("小颖\\傻宝\\小颖");
小颖\傻宝\小颖
    //System.out.println("我说：\"小颖是一个傻宝，我爱小颖\"");
我说："小颖是一个傻宝，我爱小颖"
    //System.out.println("我说：\'小颖是一个傻宝，我爱小颖\'");
我说：'小颖是一个傻宝，我爱小颖'
    //System.out.println("傻宝傻宝\r小颖");  
   	// “\r”是回车，光标挪到当前行最前面，将后面的内容对前面的内容进行逐字覆盖，与“\n”不一样。
小颖傻宝
```

------

## 1.12 初学Java易犯错误

### 1.12.1 找不到文件

![image-20220725174351183](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207261034855.png)

原因：

- 源文件名不存
- 写错源文件名
- 当前路径错误

### 1.12.2 public主类名和文件名不一致

![image-20220725174405272](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207261034843.png)

解决方法：声明为public的主类应与文件名一致

### 1.12.3 缺少分号

![image-20220725174419645](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207261034840.png)

解决方法：注意错误提示的行数，再到源代码中指定的位置修改错误

### 1.12.4 拼写错误

![image-20220725175606271](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207261034946.png)

解决方法：找到提示的单词改正拼写

### 1.12.5 常见错误总结

 学习编程最容易犯的错是语法错误(初学者)。Java要求你必须按照语法规则编写代码。如果你的程序违反了语法规则，例如:忘记了分号、大括号、引号，或者拼错了单词， java编译器都会报语法错误。尝试着去看懂编译器会报告的错误信息。

举例:

1. 1->1
2. 0->o
3. 英文符号写中文符号 英文;中文；英文"中文”
4. void -> viod main -> mian拼写错误
5. 代码不报错，但是运行不对——这种情况其实是业务逻辑错误

***在自己的开发环境能用，但是到了其他地方就不行了——这种情况是环境错误***

------

## 1.13 注释（comment）

### 1.13.1 介绍

用于注解说明解释程序的文字就是注释，注释提高了代码的阅读性（可读性）；注释是一个程序员必须要具有的良
好编程习惯。将自己的思想通过注释先整理出来，再用代码去体现。

### 1.13.2 Java中的注释类型

1. 单行注释 

   /内容/

2. 多行注释 

   /\*

   ​	*@author

   ​	*@version

   \*/

3. 文档注释/\*\*内容\*/

### 1.13.3 使用细节

1. 被注释的文字，不会被JVM解释执行
2. 多行注释里面不允许有多行注释嵌套

### 1.13.4 文档注释

#### 介绍

文档注释注释的内容可以被JDK提供的工具javadoc所解析，生成一套以网页文件形式体现的该程序的说明文档，一般写在类和方法前面。

#### 基本格式

```java
/**

	* [javadoc标签]

	* [javadoc标签]

*/
```

#### 如何生成对应的文档注释

**基本命令**

**javac -d 文件夹路径 -@author -@version \*\*.java**

#### javadoc 标签

**javadoc** **工具软件识别以下标签：**

| **标签**          | **描述**                                                   | **示例**                                                     |
| ----------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **@author**       | **标识一个类的作者**                                       | **@author  description**                                     |
| **@deprecated**   | **指名一个过期的类或成员**                                 | **@deprecated  description**                                 |
| **{@docRoot}**    | **指明当前文档根目录的路径**                               | **Directory  Path**                                          |
| **@exception**    | **标志一个类抛出的异常**                                   | **@exception  exception-name explanation**                   |
| **{@inheritDoc}** | **从直接父类继承的注释**                                   | **Inherits a  comment from the immediate surperclass.**      |
| **{@link}**       | **插入一个到另一个主题的链接**                             | **{@link  name text}**                                       |
| **{@linkplain}**  | **插入一个到另一个主题的链接，但是该链接显示纯文本字体**   | **Inserts an  in-line link to another topic.**               |
| **@param**        | **说明一个方法的参数**                                     | **@param  parameter-name explanation**                       |
| **@return**       | **说明返回值类型**                                         | **@return  explanation**                                     |
| **@see**          | **指定一个到另一个主题的链接**                             | **@see  anchor**                                             |
| **@serial**       | **说明一个序列化属性**                                     | **@serial  description**                                     |
| **@serialData**   | **说明通过writeObject( ) 和 writeExternal( )方法写的数据** | **@serialData  description**                                 |
| **@serialField**  | **说明一个ObjectStreamField组件**                          | **@serialField  name type description**                      |
| **@since**        | **标记当引入一个特定的变化时**                             | **@since  release**                                          |
| **@throws**       | **和  @exception标签一样.**                                | **The  @throws tag has the same meaning as the @exception tag.** |
| **{@value}**      | **显示常量的值，该常量必须是static属性。**                 | **Displays  the value of a constant, which must be a static field.** |
| **@version**      | **指定类的版本**                                           | **@version  info**                                           |

 

------

## ==1.14 Java_代码规范==

1. 类、方法的注释，一定要以javadoc的方式来写，也就是一定要用文档注释。

2. 非Java Doc的注释，往往是给代码的维护着看的，着重告诉读者为什么这样写，如何修改，注意什么问题等。

3. 使用tab操作，实现缩进，默认整体向右边移动，用shift+tab整体向左移动。

4. 运算符和 = 两边习惯性各加一个空格。比如：2 + 4 * 5 +345 -89。

5. 源文件使用utf-8编码。

6. 行宽度不要超过80字符。

7. ***代码编写==次行风格==和==行尾风格==。***

   ![image-20220726100512333](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207261034111.png)

![image-20220726100651701](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207261034610.png)

------

## 1.15 Dos命令（了解）

### 1.15.1 Dos介绍

Dos：Disk Operating System 磁盘操作系统。简单说一下Windows的目录结构。

![image-20220726101206653](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207261034854.png)

### 1.15.2 相对路径，绝对路径

- 相对路径：从当前目录开始定位，形成一个路径
- 绝对路径：从顶级目录d盘开始定位，形成的路径

![image-20220726101358463](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207261034078.png)

### 1.15.3 常用的dos命令

1. 查看当前目录是有什么内容dir

   dir dir d:\abc2\test200

2. 切换到其他盘下：盘符号 cd: change directory
   案例演示：切换到 c盘 cd/D c:

3. 切换到当前盘的其他目录下(使用相对路径和绝对路径演示),..\表示上一级目录
   案例演示： cd d:\abc2\test200  cd\..\abc2\test200

4. 切换到上一级：
   案例演示： cd..

5. 切换到根目录：cd\
   案例演示：cd\

6. 查看指定的目录下所有的子级目录 tree

7. 清屏 cls [苍老师]

8. 退出 DOS exit

9. 说明: 因为小伙伴后面使用DOS 非常少，所以对下面的几个指令，大家了解即可(md[创建目
   录],rd[删除目录],copy[拷贝文件],del[删除文件],echo[输入内容到文件],type,move[剪切]) => Linux,

