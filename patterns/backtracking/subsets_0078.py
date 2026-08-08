#78. Subsets
def subsets(nums):
    current = []     # the subset being built
    result = []

    def backtrack(index):
        if index == len(nums):
            # current[:] COPIES the list. Appending `current` itself would store a
            # reference that later pops mutate — every entry would end up empty.
            result.append(current[:])
            return

        # branch 1: choose nums[index]
        current.append(nums[index])
        backtrack(index + 1)
        current.pop()          # undo before exploring the other branch

        # branch 2: don't choose nums[index]
        backtrack(index + 1)

    backtrack(0)
    return result
