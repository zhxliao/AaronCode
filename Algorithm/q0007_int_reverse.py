
# take01 30%
class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            flag = -1
            x_new = abs(x)
        else:
            x_new = x
        x_new = str(x_new)
        y = ''
        for i in range(len(x_new)):
            y += x_new[-(i+1)]
        y_new = flag * int(y)
        if (-1)*(2**31) > y_new or y_new > 2**31-1:
            return 0 
        else:
            return y_new 

if __name__ == '__main__':
    test = Solution()
    print(test.reverse(1534236469)) 
