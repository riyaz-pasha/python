nums =list(set(map(int, list(input()))))
size=len(nums)
for i in range(0,size//2):
        print(nums[size-i-1])
        print(nums[i])
if(size/2!=size//2):
    print(nums[size//2])

