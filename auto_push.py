from time import ctime,time 
from os import system


def get_time():
    
    return ctime()

def create_git_order(time):
    
    order_arr = ["git add -A","git commit -m " + '"' + time + '"',"git push origin master","git push github master"] # 创建指令集合
    for order in order_arr:
        system(order) 

def put_file(time):
    
    file = open(r"I:\Axiu\Desktop\study\git_push_time.txt","w") 
    file.write(time + "完成最后一次提交")

if __name__ == "__main__":
    date = get_time() 
    create_git_order(date) 
    put_file(date) 
