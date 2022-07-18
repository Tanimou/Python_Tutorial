def multiply_basic(poly1, poly2):
    result = []

    lenght = len(poly1)+len(poly2)-1
    i, j, k, pr = 0, 0, 0, 0
    while k < lenght:
        for i in range(len(poly1)):
            for j in range(len(poly2)):
                if i+j == k:
                    pr += poly1[i]*poly2[j]
        result.append(pr)
        pr = 0
        k += 1
    return result


print(multiply_basic([], []))


def add(poly1, poly2):
    """Add two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result


#print(add([1, 2, 3, 4], [0, 4, 3]))


def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    return (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])


#print(split([1, 2, 3, 4], [0, 4, 3, 6, 7, 8, 2]))


def increase_exponent(poly, n):
    """Multiply poly1 by x^n"""
    return [0] * n + poly


#print(increase_exponent([1, 2, 3, 4], 3))


def multiply_optimized(poly1, poly2):
    n = max(len(poly1), len(poly2))
    if n % 2 != 0:
        n = n-1
    ##Dividestep
    if not poly1:
        return [0]*(len(poly2)-1)
    if not poly2:
        return [0]*(len(poly1)-1)
    if len(poly1) == 1:
     return [poly1[0] * poly2[i] for i in range(len(poly2))]
    elif len(poly2) == 1:
     return [poly2[0] * poly1[i] for i in range(len(poly1))]
    else:
        A, B = split(poly1, poly2)
        A0, A1 = A[0], A[1]
        B0, B1 = B[0], B[1]

        y = multiply_optimized(add(A0, A1), add(B0, B1))
        u = multiply_optimized(A0, B0)
        z = multiply_optimized(A1, B1)
        u_neg = multiply_basic(u, [-1])
        z_neg = multiply_basic(z, [-1])
        somme = add(y, add(u_neg, z_neg))
        z_carre = increase_exponent(z, n)
        somme_carre = increase_exponent(somme, n//2)

        return add(u, add(somme_carre, z_carre))


print(multiply_optimized([], []))
