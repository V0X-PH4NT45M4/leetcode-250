class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return Solution.heap_sort(nums)

    @staticmethod
    def merge_sort(nums: list[int]) -> list[int]:
        def merge(a: list[int], b: list[int]) -> list[int]:
            len_a, len_b = len(a), len(b)
            ptr_a, ptr_b = 0, 0

            c: list[int] = []
            while ptr_a < len_a and ptr_b < len_b:
                if a[ptr_a] < b[ptr_b]:
                    c.append(a[ptr_a])
                    ptr_a += 1
                else:
                    c.append(b[ptr_b])
                    ptr_b += 1
            
            for idx in range(ptr_a, len_a):
                c.append(a[idx])

            for idx in range(ptr_b, len_b):
                c.append(b[idx])
            
            return c

        if len(nums) <= 1:
            return nums

        # we want to call merge_sort recursively
        mid = len(nums) // 2
        a, b = Solution.merge_sort(nums[:mid]), Solution.merge_sort(nums[mid:])
        return merge(a, b)

    @staticmethod
    def heap_sort(nums: list[int]) -> list[int]:
        # we need to do an in-place heap sort
        # IIRC, heap can be built from a list in O(n) using heapify operation
        # 0 1 2 3 4 5 6 7 8 9 10 11
        # 0 -> (2*0 + 1, 2*0 + 2)
        # 1 -> (2*1 + 1, 2*1 + 2)
        # 2 -> (2*2 + 1, 2*2 + 2)
        # 3 -> (2*3 + 1, 2*3 + 2)
        # 4 -> (2*4 + 1, 2*4 + 2)
        # 5 -> (2*5 + 1, _)
        # 6 -> (_, _)
        # if i is parent 2*i + 1, 2*i + 2 are children
        # (2*i + 1 - 1) // 2 = (2*i + 2 - 1) // 2 = i so if j is child, (j - 1) // 2 is parent

        # heapify by pushing weak parents down, older sibling tries to replace, and then younger sibling
        # the fittest sibling defeats the parent (leaf nodes don't need to pushed down, since there's nothing for them)
        # the first non-leaf node is n // 2 - 1 since it's leaf nodes if (n is odd) -> n - 2, n - 1
        #                                                                    (n is even) -> n - 1, n
        def find_largest(idx: int, end_idx=len(nums)) -> int:
            left = idx * 2 + 1
            right = idx * 2 + 2
            largest = idx

            if left < end_idx and nums[left] > nums[largest]:
                largest = left
            if right < end_idx and nums[right] > nums[largest]:
                largest = right

            return largest

        for idx in reversed(range(len(nums) // 2)):
            while True:
                largest = find_largest(idx)
                if largest == idx:
                    break
                nums[largest], nums[idx] = nums[idx], nums[largest]
                idx = largest
                
        # now we need to pop n times
        for end_idx in reversed(range(1, len(nums))):
            # swap end_idx, now heap size is end_idx
            nums[0], nums[end_idx] = nums[end_idx], nums[0]

            # restore heap property
            bad_idx = 0
            while bad_idx < end_idx:
                largest = find_largest(bad_idx, end_idx=end_idx)
                if largest == bad_idx:
                    break
                else: 
                    nums[largest], nums[bad_idx] = nums[bad_idx], nums[largest]
                    bad_idx = largest

        return nums




if __name__ == "__main__":
    print(Solution().sortArray([-96,-91,-90,-87,77,-20,-85,-84,85,10,26,-84,86,-5,-78,-74,65,11,72,-24,56,-74,35,2,23,-71,64,25,91,63,-72,-69,47,28,73,-30,51,-58,30,-11,92,-44,65,-68,55,-22,54,-39,-13,-63,14,-10,-3,-55,-56,-28,-46,-46,29,-13,10,-25,-45,-44,-28,-24,95,34,45,26,29,25,-20,8,-12,-9,13,-8,-6,-2,-2,35,2,12,57,50,52,16,21,37,48,50,57,80,86,93,92,98]))
