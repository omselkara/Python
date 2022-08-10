e = 2.7182818
def tanh(x):
    if x>30:
        x = 30
    elif x<-30:
        x = -30
    return (e**x - e**-x) / (e**x + e**-x)