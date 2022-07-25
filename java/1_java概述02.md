[TOC]



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

 ***PS：文件要以GBK编码保存,特别是有中文的时候，因为cmd.exe属性里显示当前代码页的编码为GBK***

![image-20220725111331899](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207251113968.png)

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

## 1.10 java开发规范

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

![image-20220725174351183](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207251743239.png)

原因：

- 源文件名不存
- 写错源文件名
- 当前路径错误

### 1.12.2 public主类名和文件名不一致

![image-20220725174405272](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207251744321.png)

解决方法：声明为public的主类应与文件名一致

### 1.12.3 缺少分号

![image-20220725174419645](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207251744697.png)

解决方法：注意错误提示的行数，再到源代码中指定的位置修改错误

### 1.12.4 拼写错误

![image-20220725175606271](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202207251756310.png)

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

   ​	内

   ​	容

   \*/

3. 文档注释/\*\*内容\*/

### 1.13.3 使用细节

1. 被注释的文字，不会被JVM解释执行
2. 多行注释里面不允许有多行注释嵌套

### 1.13.4 文档注释

注释内容可以被JDK提供的工具javadoc所解析，生成一套以网页文件形式体现的该程序的说明文档，一般写在类

