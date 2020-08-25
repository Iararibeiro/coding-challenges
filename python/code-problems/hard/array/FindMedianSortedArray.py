def findMedianSortedArrays(nums1, nums2) -> float:
    merge = mergeArray(nums1, nums2)


def mergeArray(nums1, nums2):
    if len(nums1) == 0:
        return nums2
    if len(nums2) == 0:
        return nums1

    if len(nums1) == 1:
    half1 = len(nums1)/2
    half2 = len(nums2)/2

    print(nums1[0:int(half1)])
    print(nums2[0:int(half2)])


mergeArray([1,3],[2])
mergeArray([1,2],[3,4])
mergeArray([0,0],[0,0])
mergeArray([],[1])
mergeArray([2],[])
