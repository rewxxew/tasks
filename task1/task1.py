import sys
n1 = int(sys.argv[1])
m1 = int(sys.argv[2])
n2 = int(sys.argv[3])
m2 = int(sys.argv[4])
def function_path(n, m):
    path = ""
    a = 1    
    while True:
        path = path + str(a)
        a = a + m - 1      
        if a > n:
            a = a - n     
        if a == 1:
            break      
    return path
print(function_path(n1, m1) + function_path(n2, m2))
