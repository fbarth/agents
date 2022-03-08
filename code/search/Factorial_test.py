import math
from datetime import datetime

for i in range(1,900000000,1000):
    inicio = datetime.now()
    x = math.factorial(i)
    fim = datetime.now()
    print(str(i)+" ; "+str(fim-inicio))
