'''
@author: Administrator
'''


def sort(nums):
    nums_length = len(nums)
    for i in range(nums_length - 1):
        for j in range(nums_length - 1 - i):
            if nums[j] > nums[j + 1]:
                tmp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = tmp
    print nums


if __name__ == '__main__':
    nums = [3, 2, 8, 4, 1]
    sort(nums)
