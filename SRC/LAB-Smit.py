

import numpy as np
import  matplotlib.pyplot as plt
dormir =[7,8,6,11,7]
comer = [2,3,4,3,2]
trabajar=[7,8,7,2,2]
recreacion =[8,5,7,8,13]
divisiones=[7,2,2,13]
activadaes=['Dormir','Comer','Trabajar','Recreacion']
color = ['red','blue','green','yellow']
plt.pie(divisiones, labels=divisiones, colors=color, startangle=90, shadow=False,explode=(0.1,0,0,0), autopct='%1.1f%%')
plt.title('Graficos Circular')
plt.show()