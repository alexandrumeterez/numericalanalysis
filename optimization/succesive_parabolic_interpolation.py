import numpy as np

def succesive_parabolic_interpolation(a, b, c, f, eps = 0.1, max_iterations = 3):
    """
        Takes in an interval [a, b] and a unimodal function f and returns the point of local minima.
    """
    
    gr = (np.sqrt(5) + 1)/2
    k = 1
    x_curr = 1
    while k <= max_iterations:
        x = b - 1/2 * ((b-a)**2 * (f(b) - f(c)) - (b-c)**2 * (f(b) - f(a))) / ((b-a)   * (f(b) - f(c)) - (b-c)   * (f(b) - f(a)))
        x_next = x
        if x < a or x > c:
            d = (gr - 1) / (c - a)
            x1 = a + d
            x2 = c - d
            if f(x1) < f(x2):
                c = x2
            else:
                a = x1
        if(x < b and f(x) < f(b)):
            b = x
            c = b
        elif(x < b and f(x) > f(b)):
            a = x
        elif(x > b and f(x) < f(b)):
            a = b
            b = x
        elif(x > b and f(x) > f(b)):
            c = x
        k = k + 1
        if(abs(x_next - x_curr)/abs(x_next) < eps):
            return x_curr
        x_curr = x;
    return False