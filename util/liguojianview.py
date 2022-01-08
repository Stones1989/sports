#1、请写出一段Python代码实现删除一个list里面的重复元素
def no_reate(list1):
    list1 = list(set(list1))
    return list1

#2、编程先去重，再排序，list=[4,6,1,2,3,1,7,9,5,4,6,2,6,3,8]
list1=[4,6,1,2,3,1,7,9,5,4,6,2,6,3,8]
list1 = no_reate(list1)
print(list1)
list1 = sorted(list1)
print(list1)


#3、下面的代码可以将列表连接成单个字符串，且每一个元素间的分隔方式设置为了逗号。

hobbies = ["basketball", "football", "swimming"]


#4、写一个函数, 输入一个字符串, 返回倒序排列的结果: 如:string_reverse(‘abcdef’), 返回: ‘fedcba’ (请采用多种方法实现, 并对实现方法进行比较)

#5、10个常用的linux命令，并写出其作用

# ls  ll cd  mkdir remove
#
# kill -9 杀死进程


# 9、冒泡算法。

def buble(list1):
    for i in range(0,len(list1)-1):
        for j in range(i+1,len(list1)-1):
            if list[i] >= list[j]:
                list[i],list[j] = list[j],list[i]


# 10、从两个不等的字符串中找出他们相等且最长的一部分

def same_str(a,b):
    if len(a) >= len(b)
        a,b = b,a
    if a in b:
        return a
    for i in range(0,len(a)+1):
         for j in range(0,i-1):











# 11、已知数列 1 2 2 3 3 3 4 4 4 4.... ，求它的前n（n>0）项和

def sum_list():

# 12、求出大于或等于 N 的最小回文素数。

def
















