#A = grams alcohol
#r = gender correction factor
#W = mass grams
#V = constant at 0.00015
#t = time hours

x = 0
while x == 0  :
    A = input('how many standard drinks did you have ')
    A = 10 * A
    try:
        A = float(A)
        if A >= 0:
            x = 1
        else:
            print('enter a positive integer')
    except:
        print('enter a positive integer')

    r = input('what is your gender? M or F? ')
    if 'm':
        r = 0.68
    else:
        r = 0.55

    W = input('what is your weight? (in KG) ')
    W = W * 1000

t = input('how long has it been since your first drink? (in hours) ')

A = float(A)
r = float(r)
W = float(W)
t = float(t)

float = B = (A / (r * W) * 100 - (0.00015 * t))
print(B)