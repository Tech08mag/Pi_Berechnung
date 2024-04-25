import decimal

def pi_gauss_legendre(precision):
    decimal.getcontext().prec = precision + 2
    a = decimal.Decimal(1)
    b = 1 / decimal.Decimal(2).sqrt()
    t = decimal.Decimal(1) / decimal.Decimal(4)
    p = decimal.Decimal(1)

    for _ in range(precision):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2

    pi_approx = (a + b) ** 2 / (4 * t)
    return pi_approx

# Berechnen von π mit 100 Nachkommastellen Genauigkeit
precision = 100
pi_approx = pi_gauss_legendre(precision)
print(pi_approx)
