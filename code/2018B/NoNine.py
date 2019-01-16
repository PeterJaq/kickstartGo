def small_solution(snum, enum):
    ans = 0
    for num in range(snum, enum+1):
        if is_no_nine(num):
            ans += 1
            #print('True', num)
    return ans

def is_no_nine(num):
    sum = 0
    while num > 0:
        e = num % 10
        if e == 9:
            return False
        sum += e
        num = int(num / 10)
    if sum % 9 == 0:
        return False
    return True

def big_solution(snum, enum):
    pass


if __name__ == '__main__':
    n = int(input())
    print(n)
    for i in range(1, n+1):
        startNum, endNum = map(int, input().split(' '))
        print("Case #{}: {}".format(i, small_solution(startNum, endNum)))
