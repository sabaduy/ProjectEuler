import math

# This is equal to the binomial coefficient
# (n + k)
# (  n  )
#
# Binomial coefficient formula is
# (n)       n!
# ( ) = ----------
# (k)   k!(n - k)!
#
# This translates to
# (n + k)       (n + k)!
# (     ) = ----------------
# (  n  )   n!((n + k) - n)!


num_rows = 20
num_cols = 20

answer = math.factorial(num_rows + num_cols)/(math.factorial(num_rows)*math.factorial(num_rows + num_cols - num_rows))
print(int(answer))

