
'''
# take01 94% 
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_new = s.strip()
        last_len = 0 
        for i in range(len(s_new)):
            if s_new[(-1)*(i+1)] != ' ':
                last_len += 1 
            else:
                break
        return last_len
'''

# take02 33% 
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
        
if __name__ == '__main__':
    test = Solution()
    print(test.lengthOfLastWord('jafddfjjfd falfjlfjd afljdfljf jf')) 
