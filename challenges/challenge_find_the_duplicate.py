def find_duplicate(nums):
    if len(nums) == 1:
        return False

    nums.sort()

    for index, num in enumerate(nums):
        if not isinstance(num, int) or num < 1:
            return False

        if num == nums[index - 1]:
            return num
    return False
