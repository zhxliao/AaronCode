'''
# take01 too long
class Solution:
    def calTri(self, arr, i, j, k):
        a = arr[i]
        while True:
            i += 1
            if j>i:
                a = a^arr[i]
            else:
                break 
        b = arr[j]
        while True:
            j += 1 
            if k>=j:
                b = b^arr[j]
            else:
                break
        return (a, b)

    def countTriplets(self, arr) -> int:
        counting = 0
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                j_real = i+1+j 
                for k in range(len(arr)-j_real):
                    k_real = j_real + k 
                    a, b = self.calTri(arr, i, j_real, k_real)
                    if a==b:
                        print(counting+1, i, j_real, k_real)
                        counting += 1
        return counting

# take02 7%
# 根据异或运算的特殊性，增加 ^arr[item] 的抵消方式就是再来一个 ^arr[item]
# 意味着 a ^ b = 0, arr[i]^...^arr[k]
# 妈蛋，居然有数学推理
class Solution:
    def calTri(self, arr, i, k):
        a = arr[i]
        while True:
            i += 1
            if k>=i:
                a = a^arr[i]
            else:
                break 
        return True if a==0 else False 

    def countTriplets(self, arr) -> int:
        counting = 0
        for i in range(len(arr)-1):
            for k in range(len(arr)-i-1):
                k_real = i + 1 + k 
                if self.calTri(arr, i, k_real):
                    counting+=k_real-i 
        return counting

# take03 22%
# 在上一步的数学原理上更进一步
class Solution:
    def countTriplets(self, arr) -> int:
        counting = 0
        for i in range(len(arr)-1):
            tmp_tri_layer0 = arr[i]
            tmp_tri_layer1 = tmp_tri_layer0
            for k in range(len(arr)-i-1):
                k_real = i + 1 + k 
                tmp_tri_layer1 = tmp_tri_layer1^arr[k_real]
                if tmp_tri_layer1==0:
                    print(i, k_real, tmp_tri_layer0, tmp_tri_layer1)
                    counting+=k_real-i 
        return counting

# take04 52%
class Solution:
    def countTriplets(self, arr) -> int:
        counting = 0
        for i in range(len(arr)-1):
            tmp_tri_layer1 = arr[i]
            for k in range(len(arr)-i-1):
                k_real = i + 1 + k 
                tmp_tri_layer1 = tmp_tri_layer1^arr[k_real]
                if tmp_tri_layer1==0:
                    counting+=k_real-i 
        return counting
'''

# take05 24%
class Solution:
    def countTriplets(self, arr) -> int:
        counting = 0
        temp_dict = {}
        for i in range(len(arr)-1):
            tmp_tri_layer1 = arr[i]
            for m in range(i+1):
                if m not in temp_dict:
                    temp_dict[m] = arr[i]^arr[i+1]
                else :
                    temp_dict[m] = temp_dict[m]^arr[i+1]
                if temp_dict[m]==0:
                    counting+=i+1-m  
        return counting

if __name__ == '__main__':
    test = Solution()
    print(test.countTriplets([2,3,1,6,7]))
    # test.countTriplets([723,875,440,136,304,271,63,294,281,169,432,185,265,758,1023,760,263,13,266,458,192,774,966,855,145,115,226,233,11,710,717,281,980,386,598,564,98,604,574,717,243,309,454,676,866,944,210,301,511,700,835,696,507,794,737,999,262,36,290,981,759,52,707,734,29,273,268,853,601,293,892,66,830,145,943,959,16,989,973,609,428,289,141,985,852,974,154,522,656,894,494,520,998,934,64,967,903,708,323,927,732,878,434,972,638,550,88,805,893,514,383,686,977,165,884,691,455,39,480,698,858,400,714,230,556,566,26,851,841,240,953,938,19,385,402,931,561,502,967,104,943,948,27,248,227,677,582,541,91,703,740,871,387,788,663,210,581,335,778,514,264,538,786,369,611,349,830,246,968,152,848,471,647,488,879,900,235,726,573,200,757,236,537,420,957,793,164,120,220,276,456,772,716,112,700,40,660,498,870,559,329,411,210,783,989,732,257,988,733,743,58,8,50,266,312,461,245,849,932,758,338,62,364,474,182,680,542,201,727,782,473,567,1006,39,969,575,502,788,738,297,971,499,568]) 
