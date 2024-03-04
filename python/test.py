import math

def closest_reciprocal(n):
    if n == 0:
        return None
    sqrt_n = math.sqrt(n)
    floor_val = math.floor(sqrt_n)
    ceil_val = math.ceil(sqrt_n)
    
    if abs(sqrt_n - floor_val) < abs(sqrt_n - ceil_val):
        return 1.0 / floor_val
    else:
        return 1.0 / ceil_val
ans = closest_reciprocal(10)
print(ans)