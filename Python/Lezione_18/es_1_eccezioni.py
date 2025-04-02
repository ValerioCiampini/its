import math

def safe_sqrt(number:int):
    n = math.sqrt(number)

    return print(n)

n = -9
if n < 0:
    raise Exception(f"n deve essere positivo ({n=})")
else:
    safe_sqrt(n)