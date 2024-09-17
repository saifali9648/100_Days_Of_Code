# def is_prime(num):
#     for i in range(1,num+1):
#         if num%2!=0:
#             return True
#         else:
#             return False

# print(is_prime(11))


def is_prime(num):
    # flage=False
    for i in range(2,num):
        if num%i ==0:
            return False
    else:
        return True
print(is_prime(75))