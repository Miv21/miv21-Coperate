import math
def letter(a,b,c):
    p = (a + b + c )/2
    return math.sqrt(p) * (p - a)*(p - b)*(p - c)

def triagle(a,b,c):
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник не получится"
    else:
        if a == b or b == c or a == c:
            if a == b and a == c and b == c:
                return "Треугольник равносторонний", letter(a,b,c)
            else:
                return "Треугольник равнобедренный", letter(a,b,c)
        return "Утреугольника разные стороны",letter(a,b,c)

print (triagle(1,3,1))
print (triagle(7,7,7))
print (triagle(4,5,-3))
print (triagle(1,2,5))
print (triagle(3,4,5))
print (triagle(1,3,5))
print (triagle(6,4,2))