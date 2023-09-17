def minJumps(arr, N):
    pos, jumps, largest = 0, 0, 0
    test_arr = arr
    while pos <= N - 2:
        if arr[pos] == 0:
            return -1
        largest = max(arr[pos: pos + arr[pos] + 1])
        pos += test_arr.index(largest)
        test_arr.remove(largest)
        jumps += 1
    return jumps



arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = 11

arr2 = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
n2 = 10

arr3 = [1, 4, 3, 2, 6, 7]
n3 = 6

ans = minJumps(arr=arr2, N=n2)
print(ans)
