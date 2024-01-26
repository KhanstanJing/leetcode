
class Solution:
    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        elif x % 10 == 0 and x != 0:
            return False
        else:
            temp = x
            reversed_num = 0
            while temp != 0:
                r = temp % 10
                reversed_num = reversed_num*10 + r
                temp //= 10
        return reversed_num == x
    def isPalindrome1(self, x: int) -> bool:
        mylist = []
        cal = 0
        if x < 0:
            return False
        elif x % 10 == 0 and x != 0:
            return False
        else:
            for i in range(1, 20):
                if x >= 10**i:
                    r = x % (10**i)
                    r = r // (10**(i - 1))
                    mylist.append(r)
                else:
                    r = x % (10 ** i)
                    r = r // (10 ** (i - 1))
                    mylist.append(r)
                    l = len(mylist)
                    for index, value in enumerate(mylist):
                        cal = cal + value*(10**(l - index - 1))
                    if cal == x:
                        return True
                    else:
                        return False
    def isPalindrome(self, x: int) -> bool:
        mylist = []
        cal = 0
        if x < 0:
            return False
        elif x % 10 == 0 and x != 0:
            return False
        else:
            for i in range(1, 20):
                s = (x // (10**i))*(10**i)
                if s != 0:
                    r = x - s
                    r = r // (10**(i - 1))
                    mylist.append(r)
                else:
                    s = x // (10**(i - 1))
                    mylist.append(s)
                    l = len(mylist)
                    for index, value in enumerate(mylist):
                        cal = cal + value*(10**(l - index - 1))
                    if cal == x:
                        return True
                    else:
                        return False

if __name__ == '__main__':
    # num1 = 5 / 2, num2 = 5 // 2
    # print(num1, num2)
    solution = Solution()
    print(solution.isPalindrome1(10301))

# isPalindrome()
# 101ms 7.11%
# 16.73MB 53.42%
# 1 python中使用单斜杠是输出浮点数的除法，使用//是输出整数的除法，向下取整
# 2 python中想要使用动态列表直接写一个 list mylist = []，而后需要用的时候向其中添加，使用mylist.append即可
# 3 if-elif-else
# 4 enumerate先返回索引，而后返回值
# 5 开始没有加入对于0的判断，因此在对x进行对10取余的时候0被判断成Falsel
# 6 并且i的设置有点短，开始设置的是10位，因此1000000001就返回None了，后来想了一下，这个应该多大都没什么关系

# isPalindrome1()
# 85ms 10.53%
# 16.58MB 59.26%

# isPalindrome2()
# 51ms 81.18%
# 16.62MB 54.89%
# 看了另一个答案，意识到完全没必要每次都用原数字减去一个342000的形式的数字
# 因为整数除法本身就能每一次都把个位数的数甩掉而且减少十倍，所以只要每次都这么做就可以了
# 1 需要返回True or False的问题直接在return部分放判断就可以
# 2 我设计了一个对于x判断是否能整除10的部分，但是这部分加上去之后比原代码有时候快有时候慢，效果不明显
# 3 多设计一个reversed_num来额外存放待比较的数，这一点开始不知道怎么想都没想出来