#from typing import List

class Solution:
    def twoSum(self, nums: list[int], target:int) -> list[int]:
        for i in range(len(nums)):
            temp = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == temp:
                    # wrong: print("[%d,%d]" %(i,j))
                    return [i,j]

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    solution = Solution()
    # Solution.twoSum([2, 7, 11, 15],9)
    print(solution.twoSum(nums, 9))

# runtime: 978ms 35.45%
# memory: 17.33MB 83.18%
# 1 题目中给定部分是class和def，注意这里的def中给定了需要返回的东西是一个列表，因此如果在函数结尾写print把结果打印出来是没有用的
# 2 List和list是不一样的，list是python内置的数据类型，List需要从typing中导入
# 3 twoSum是一个实例方法，因此在调用时需要传入类的实例作为第一个参数 self。在main中，直接使用 Solution.twoSum(nums, 9) 来调用 twoSum 方法，但是没有传入类的实例
#   这样就会出现以下错误：TypeError: Solution.twoSum() missing 1 required positional argument: 'target'
#   区分实例和类！类是抽象出来的东西，要使用必须创建一个实例才能使用
# 4 Solution.twoSum([2, 7, 11, 15],9)这句代码不会有任何输出结果，需要用print打印出来才有输出
# 5 ？一个问题，这里计算temp的位置会不会影响计算的时间？直觉上来说感觉会影响