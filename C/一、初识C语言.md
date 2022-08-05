[TOC]



# 一、初识C语言

## 1.1 什么是C语言

### 1.1.1 介绍

C语言是一门通用的**计算机编程语言**，广泛用于**底层开发**。C语言的设计目的是提供一种能以简易的方式编译、处理低级存储器、产生少量的机械码以及**不需要任何运行环境支持便能运行的编程语言**。

底层：即应用层以下。如操作系统，驱动。

![image-20220804132615187](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202208041326319.png)

尽管C语言提供了许多低级处理的功能，但仍然保持着良好跨平台的特性，以一个标准规格写出的
C语言程序可在许多电脑平台上进行编译，甚至包含一些嵌入式处理器（单片机或称MCU）以及
超级电脑等作业平台。

### 1.1.2 国际标准

二十世纪八十年代，为了避免各开发厂商用的C语言语法产生差异，由美国国家标准局为C语言制
定了一套完整的美国国家标准语法，称为**ANSI C**，作为C语言最初的标准

目前2011年12月8日，国际标准化组织（ISO）和国际电工委员会（IEC）发布的C11标准是C语言的第三个官方标
准，也是C语言的最新标准，该标准更好的支持了汉字函数名和汉字标识符，一定程度上实现了汉字编程。

C语言是一门面向过程的计算机编程语言，与C++，Java等面向对象的编程语言有所不同。
其编译器主要有Clang、GCC、WIN-TC、SUBLIME、MSVC、Turbo C等

C语言有国际标准：C89，C90，C99，C11 

演变历史：

![image-20220804133216872](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202208041332907.png)

## 1.2 第一个C语言程序

1. 新建项目
2. 在源文件目录下新建项或源文件
3. 写代码
4. 编译代码

```c
// 写代码
#include <stdio.h>  //引用头文件
int main()          //主函数，程序的入口，一个程序有且只有一个主函数
{
	printf("hello C\n");
	printf("he he\n");
	return 0;
}
```

## 1.3 数据类型

### 1.3.1 数据类型一览

| char   | 字符数据类型   |
| ------ | -------------- |
| short  | 短整数数据类型 |
| int    | 整数数据类型   |
| long   | 长整数数据类型 |
| float  | 单精度浮点数   |
| double | 双精度浮点数   |

### 1.3.2 为什么会有这么多数据类型？

计算机对数据的的认识和分类，例如纯字符即字母，数字，数字又分小数和整数，又分大和小，每一种不同的数据类型都有不同的大小。对不同数数据进行区分可以合理更高效率的利用存储空间。

### 1.3.3 每种数据类型的大小

可使用sizeof，sizeof是C语言的关键字或操作符，可以计算数据类型或者变量所占空间的大小(单位是byte)。

```c
#include <stdio.h>
int main(){						//编译后得
    printf("%d\n",sizeof(char)); // 1
    printf("%d\n",sizeof(short));// 2
    printf("%d\n",sizeof(int));	 // 4
    printf("%d\n",sizeof(long)); // 4 	C语言的标准：sizeof（long）>=sizeof（int）
    printf("%d\n",sizeof(float));// 4
    printf("%d\n",sizeof(double));//8
    return 0;
}
```

PS: ***byte***即字节。1 byte = 8 bit，bit是计算机中的单位，计算机只认识二进制，即0和1，一个bit存放一个二进制位。

## 1.4 变量和常量

### 1.4.1 介绍

变量：可变的数据（例如血压、体重、工资）

常量：定值，固定不变的数据（血型、性别）

### 1.4.2 定义变量的方法

一个变量 = 数据类型 + 变量标识符（变量名） （+ 数值）

1. 定义变量的同时进行赋值，例如：

   int year = 2022，

   char blood = A

2. 先定义数据类型后面再赋值也可，例如：

   char blood；

   blood = A；

### 1.4.3 变量的分类

- 局部变量

- 全局变量

  ```c
  #include <stdio.h>
  
  int global = 2022;//mian函数外部定义的是全局变量，
  int mian(){
      int local = 2023;//main函数内部定义的是局部变量
      int global = 2024;
      printf("global = %d\n",global);// 2024 其中%d就是映射整型变量global
      return 0;
  }
  ```

  **总结：当局部变量和全局变量重名的时候，局部变量优先使用。但是不建议全局变量和局部变量重名。**

  > %d-int  %f-float  %lf-double

### 1.4.4 变量的使用

printf是输出函数，scanf是输入函数;

&是取址符，即读取地址，地址上的数据便会赋予指定变量。

```c
#include <stdio.h>
int main(){
    int num1,num2,sum;
    printf("请输入两个数字,例如:12 13");
    scanf("%d %d",&num1,&num2);
    sum = num1 + num2;
    printf("两个数的合为:%d",sum);
    return 0;
}
```

### 1.4.5 变量的作用域和生命周期

#### 作用域

> 作用域（scope）的程序设计概念，通常来说，一段程序中所用到的变量并不总是有效或者可用
>
> 而限定这个变量的可用性的代码范围就是这个名字的作用域

1. 局部变量的作用域是变量所在的局部范围。
2. 全局变量的作用域是整个工程。

#### 生命周期

> 变量的生命周期指的是从变量的创建到变量的销毁的一个时间段

1. 局部变量的生命周期是：进入作用域局部变量被创建，生命周期开始；出作用域，局部变量被销毁，生命周期结束。
2. 全局变量的生面周期是：整个程序的生命周期。 

#### 全局变量范例

extern用作声明变量，告诉计算机有这个变量

```c
//同一个项目中，同一个源文件目录下
//在main.c文件中中定义一个全局变量
int num1 = 0,num2 = 1;

//在test.c文件中
#include <stdio.h>
extern int num1,num2;
int main() {
	printf("请输入个输入数字（例如：12 13）：\n%d,%d",num1,num2);
	return 0;	
}

//编译运行得：
请输入个输入数字（例如：12 13）：
0,1
--------------------------------
```

## 1.5 常量

- C语言中的常量和变量的定义的形式有所差异。

- C语言中的常量分为以下几种：

  1. 字面常量

  2. ==const==修饰的常变量——具有常属性，即具有常量的不可变性

     ```c
     #include <stdio.h>
     int main() {
     	const int num = 2024;//整型num被const赋予常量的不可变性
     	num = 2022; //次行代码会报错，因为num变量已经被const修饰为常变量，不可再赋值或运算改变
     	printf("num = %d",num1);
     	return 0;	
     }
     ```

  3. ==#define== 定义的标识符常量

     ```c
     #define MAX 10000 //define将MAX定义成一个值为10000的常量
     #include <stdio.h>
     int main(){
         MAX = 200//此处会报错，去掉即正常
         int n = MAX;
     	printf("%d", MAX);//打印输出10000
         return 0;
     }
     ```

     

  4. 枚举常量，例如： 

     enum Sex

     {

     ​	MALE,

     ​	FEMALE,

     ​	SECRET

     }；

     其中enum Sex是自己创建的枚举类型，括号中的即为枚举常量，类似于变量的变量类型加变量标识符，也就是变量名

     ```c
     #include <stdio.h>
     enum Sex
     
     {
     	MALE,
     	FEMALE,
     	SECRET
     };
     int main(){
     	enum Sex s = MALE;
         //这里赋值只能写上方括号中写的值，其中enum Sex是自己创建的枚举类型，s是枚举类型名，类似于变量的变量类型加变量名字，括号中的即为枚举常量，
         printf("%d\n",MALE);//0
         printf("%d\n",FEMALE);//1
         printf("%d\n",SECRET);//2
         printf("%f\n",MALE);//输出全为0.000且有警告
     	printf("%f\n",FEMALE);
     	printf("%f\n",SECRET);
         return 0;
     }
     ```
     
     ![image-20220804181907295](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202208041819421.png)
     
     
     
     可以把代码再改一下
     
     ```c
     #include <stdio.h>
     enum Sex
     
     {
     	/*
     	MALE = 1.0// 会报错
         MALE =1，//不会报错
     	FEMALE
     	SECRET 
     	*/
     
         MALE =1，//不会报错
     	FEMALE
     	SECRET
     
     };
     int main(){
     	enum Sex s = MALE;//这里赋值只能写上方括号中写的值
         printf("%d\n",MALE);//1
         printf("%d\n",FEMALE);//2
         printf("%d\n",SECRET);//3
         return 0;
     }
     默认赋值就是从0开始顺序赋值，如果开头或中间有个数被赋了初值的，那么赋了初值的那个数往后的数就会以这个初值为开头依次按顺序赋值
     ```
     
     总结：enum会按顺序把字符串变成一个枚举常量并赋予整数，默认赋值就是从0开始顺序赋值，如果开头或中间有个数被赋了初值的，那么赋了初值的那个数往后的数就会以这个初值为开头依次按顺序赋值。

## 1.6 字符串+转义字符+注释

### 1.6.1 字符串

#### 介绍

```c
"I want to take the postgraduate examination!!!"
```

这种由双引号（Double Quote）引起来的一串字符串成为字符串面值（String Literal），或简称字符串

注：字符串的结束标志是一个==\0==的转义字符。在计算字符串长度时==\0==是结束标志，不算做字符串内容。

字符数组-数组是一组形同类型（char arr[]）的元素。

```c
#include <stdio.h>

int main() {
	
	char arr[] = "I want to take the postgraduate examination!";
	
	return 0;
}
```

调试监视时可以看到arr最后一个值为“\0”

<img src="https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202208051100095.png" alt="image-20220805110026926" style="zoom: 50%;" />

#### 注意

用char arr[]="";方式写时，有\0时会隐藏不打印出来，没有时会自动添添加\0但是不打印出来。

用char arr[]={''，''，''，''\0'}；最后不会自动添加\0，需要在最后最后加上一个\0，否则会乱码

![image-20220805115028984](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202208051150060.png)

为什么会出现这样的情况呢？先引用大哥原话，毕竟我还没学到指针😵

<img src="https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202208051132012.png" alt="image-20220805113231907" style="zoom:50%;" />

#### 求字符串长度

使用strlen（string length）表达式

```c
#include <stdio.h>

int main() {

	char arr1[] = "I want to take the postgraduate examination!";
	char arr2[] = {'1','2','3'};
    char arr3[] = {'1','2','3','\0'};
	printf("%d\n",strlen(arr1));//44
	printf("%d", strlen(arr2));//随机值
	return 0;
}
```

![image-20220805114847176](https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202208051148255.png)



### 1.6.2 转义字符

| 转义字符 | 释义                                                         |
| -------- | ------------------------------------------------------------ |
| \?       | 在书写连续多个问号时使用，防止他们被解析成三字母词           |
| \\'      | 用于表示字符常量'                                            |
| \\"      | 用于表示一个字符串内部的双引号                               |
| \\\      | 用于表示一个反斜杠，防止它被解释为一个转义序列符。           |
| \a       | 警告字符，蜂鸣                                               |
| \b       | 退格符                                                       |
| \f       | 进纸符                                                       |
| \n       | 换行                                                         |
| \r       | 回车                                                         |
| \t       | 水平制表符                                                   |
| \v       | 垂直制表符                                                   |
| \ddd     | ddd表示1~3个八进制的数字。如：\130 输出八进制数130对应的ASCII码值 X |
| \xdd     | dd表示两个十六进制的数字。如：\x30  输出十六进制数30对应的ASCII码值 0 |

### 1.6.3 注释

1. 代码中有不需要的代码可以直接删除，也可以注释掉
2. 代码中有些代码比较难懂，可以加一下注释文字

注释有两种风格：

- C语言风格的注释 /\*

  ​			  xxxxxx

  ​			  \*/

  - 缺陷：不能嵌套注释

- C++风格的注释 //xxxxxxxx

  - 可以注释一行也可以注释多行

## 1.7 条件语句

### 1.7.1 选择语句

<img src="https://picgo-1305004037.cos.ap-guangzhou.myqcloud.com/images/202208051602365.png" alt="image-20220805160234113" style="zoom: 50%;" />

#### 基本语法：

```c
if（判断语句）{

	(代码语句);

}

else{

	(代码语句);

}
```



#### 范例

```c
#include <stdio.h>
int main(){
	int coding = 0;
	printf("你会要继续学习吗？（选择1 or 0）:>");
	scanf("%d", &coding);
	if(coding == 1){
		prinf("坚持，你能考研上岸的\n");
	}
	else{
		printf("放弃，回家卖红薯娶不到老婆\n");
	}
	return 0;
}
```

### 1.7.2循环语句

