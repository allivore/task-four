def is_monotonic(nums=list):
    index = 0

    if nums[0] >= nums[-1]:
        for x in nums:
            if index == 0:
                index += 1
                continue
            elif x <= nums[index-1]:
                index += 1
                continue
            else:
                return False

    else:
        for x in nums:
            if index == 0:
                index += 1
                continue
            elif x >= nums[index-1]:
                index += 1
                continue
            else:
                return False

    return True
