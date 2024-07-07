import random
signal=['stop','wait','go']
for k in range(3):
    r=random.randint(0,k)
    print(signal[r],end='#')
