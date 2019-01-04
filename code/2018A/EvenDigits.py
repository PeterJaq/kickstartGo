def solution1(input):
    #number = str(input)
    distance = 0
    Flag = False
    while Flag is False:
        if is_even_digits(input + distance) is True or is_even_digits(input - distance) is True:
            Flag = True
        else:
            distance += 1
    return distance

def is_even_digits(number):
    while number > 0:
        if (number % 10) % 2 != 0:
            return False
        number = int((number - (number%10))/10)
    return True

def solution2(input):
    input_list = list(map(int, input))


    minus_flag = False
    for i in range(len(input_list)):
        if minus_flag is False and input_list[i] % 2 != 0:
            input_list[i] -= 1
            minus_flag = True
        elif minus_flag is True:
            input_list[i] = 8
    minus_ans = int(input) - int("".join([str(x) for x in input_list]))

    input_list = list(map(int, input))
    p1_flag = False
    for i in range(len(input_list)-1, -1, -1):
        if p1_flag is False and input_list[i] % 2 != 0:
            p1_flag = True
        elif p1_flag is True:
            if input_list[i] < 8:
                p1_flag = False

    if p1_flag is True:
        p1_answer = 2*10**len(input_list) - int(input)
        return min([minus_ans, p1_answer])

    input_list = list(map(int, input))
    p2_flag = False
    for i in range(len(input_list)):
        if p2_flag is False and input_list[i] % 2 != 0:
            p2_flag = True
            input_list[i - 1] += 2

    p2_ans = int(input) - int("".join([str(x) for x in input_list]))

    else:
        return min([minus_ans, p2_ans])



if __name__ == '__main__':

    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        ans = solution2(input()) # read a list of integers, 2 in this case
        print("Case #{}: {}".format(i, ans))