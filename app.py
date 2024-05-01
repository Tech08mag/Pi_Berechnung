import decimal

class Pi():
    def get_precision():
        precision = int(input("Gebe die Nachkommastellen von Pi ein, die du berechnen möchtest: "))
        return precision
    
    def pi_gauss_legendre():
        precision = Pi.get_precision()
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

pi_approx = Pi.pi_gauss_legendre()
print(pi_approx)