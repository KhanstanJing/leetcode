
class Solution:
    def isPalindrome3(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_num = 0
        # 判断后半段是否被扔完的过程
        while(x > reversed_num):
            # 后半段翻转的过程
            reversed_num = reversed_num*10 + x % 10            # 扔掉后半段的过程
            x //= 10
        return x == reversed_num or x == reversed_num//10
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


"""
isPalindrome()
101ms 7.11%
16.73MB 53.42%
1 python中使用单斜杠是输出浮点数的除法，使用//是输出整数的除法，向下取整
2 python中想要使用动态列表直接写一个 list mylist = []，而后需要用的时候向其中添加，使用mylist.append即可
3 if-elif-else
4 enumerate先返回索引，而后返回值
5 开始没有加入对于0的判断，因此在对x进行对10取余的时候0被判断成Falsel
6 并且i的设置有点短，开始设置的是10位，因此1000000001就返回None了，后来想了一下，这个应该多大都没什么关系

isPalindrome1()
85ms 10.53%
16.58MB 59.26%

isPalindrome2()
51ms 81.18%
16.62MB 54.89%
看了另一个答案，意识到完全没必要每次都用原数字减去一个342000的形式的数字
因为整数除法本身就能每一次都把个位数的数甩掉而且减少十倍，所以只要每次都这么做就可以了
1 需要返回True or False的问题直接在return部分放判断就可以
2 我设计了一个对于x判断是否能整除10的部分，但是这部分加上去之后比原代码有时候快有时候慢，效果不明显
3 多设计一个reversed_num来额外存放待比较的数，这一点开始不知道怎么想都没想出来

isPlindrome3()
这是写了isPlindrome2()的作者写的另外一个答案，这个答案可以通过判断一半来判断数字是否为回文，很精妙
要想只判断一半的代码，首先一个重大的问题就是数字是奇数位还是偶数位
如果要我来想的话，我会想这个问题在于如何获取数字到底是奇数位还是偶数位，进而可能就必须得知道数字的位数
但是通过作者的思维来看明显就不是那么回事儿，作者的思维重点在于**如果是奇数位应该怎么办，如果是偶数位又应该怎么办**
在这种思考方式下，我们的目标就变成了获得前半段和后半段翻转过的数字，并且想办法判断它们是否相等
而奇数位数字中间数字的问题也很好解决了，我们直接扔掉它就可以了
这样，我们只需要：整数除法和取余运算即可。整数除法可以抛掉最后一位数，取余运算可以取到最后一位数
另外，判断可以放在一行写
"""