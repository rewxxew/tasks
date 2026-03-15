import sys
func = open(sys.argv[1], 'r')
x0, y0 = map(float, func.readline().split())
a, b = map(float, func.readline().split())
func.close()
func = open(sys.argv[2], 'r')
dots = func.readlines()
func.close()
if len(dots) < 1 or len(dots) > 100:
    print("Требуется количество точек от 1 до 100")
    sys.exit(1)
for dot in dots:
    if dot.strip():
        x, y = map(float, dot.split())
        for n in [x0, y0, a, b, x, y]:
            if abs(n) > 1e38 or (abs(n) < 1e-38 and n != 0):
                print("Координаты не соответствуют диапазону")
                sys.exit(1)
        res = ((x - x0)/a)**2 + ((y - y0)/b)**2
        if abs(res - 1) < 0.000001:
            print(0)
        elif res < 1:
            print(1)
        else:
            print(2)
