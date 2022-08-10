e = 2.7182818
def tanh(x):
    if x<-15:
        x = -15
    elif x>15:
        x = 15
    return (e**x - e**-x) / (e**x + e**-x)