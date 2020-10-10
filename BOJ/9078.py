for test_case in range(int(input())):
    n = int(input())
    lst = input().split()
    
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                count += 1

    if count % 2 == 0:
        print('YES')
    else:
        print('NO')
                

                
                    
