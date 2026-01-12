def add_zeros(n):
    n = f"{int(n):04}"
    return n        #returns n with 4 digits in string type

def validate_input(n):
    valid_input = True
    not_allowed = ["1111", "2222", "3333", "4444", "5555", "6666" , "7777", "8888", "9999", "0000"]
    num = add_zeros(n)
    if num in not_allowed or len(num) > 4:
        valid_input = False
    return valid_input #returns True if number is valid

def sort_digits(n,b):
    lst = []
    for ch in n:
        lst.append(int(ch))
    if b == True:
        order = []
        for i in range(4):
            maximum = 0
            for j in lst:
                if maximum < j:
                    maximum = j
            lst.remove(maximum)
            order.append(maximum)
    else:
        order = []
        for i in range(4):
            minimum = 9
            for j in lst:
                if minimum > j:
                    minimum = j
            lst.remove(minimum)
            order.append(minimum)
    sorted_str = ""
    for k in order:
        sorted_str += str(k)
    return sorted_str #Return a number sorted in string

def main():
    maximum_iterations = 0
    THE_number = []
    for i in range(9999):
        valid = validate_input(i)
        if valid == False:
            continue

        N = add_zeros(i)
        iter = 0
        finished = False
        while finished == False:
            a = int(sort_digits(N, False))
            b = int(sort_digits(N, True))
            dif = b - a
            if N == add_zeros(dif):
                finished = True
                break
            else:
                N = add_zeros(dif)
                iter += 1
        if iter >= maximum_iterations:
            maximum_iterations = iter
            THE_number.append(i)
    print (f"Number with biggest amount of itterations is {THE_number} with total amount of iterations: {maximum_iterations}")
    print (f"Total amount of numbers with iterations {maximum_iterations} are {len(THE_number)}")

main()