'''
BUBBLE-SORT(A)
    for i = 1 to |A| -1 do                      --- 0((n - i) * (n - i)) = 0(n^2) times
        for j = |A| - 1 down to i + 1           --- repeated n - 1 times, 0(n - 1) times each
            if A[j] < A[j - 1] then             --- 0(1) times
                exchange A[j] with A[j - 1]     --- 0(1) times



                python:    A[j], A[j - 1] = A[j - 1], A[j]

                c++:    swap(A[j], A[j - 1])
                

'''
