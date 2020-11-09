#для pow 
import math
#константа точности
EPS=1e-5
#инициализация входных данных
xPrev=1.0
xCur=0.2
#основной цикл
while(abs(xPrev-xCur)>=EPS):
    xPrev=xCur
    xCur=(2-pow(xPrev, 3))/5
    print("xPrev = %7.5f\t"%xPrev, end="")
    print("xCur = %7.5f"%xCur, end="\n")
#вывод ответа
ans=xCur
print("Answer is : %7.5f"%ans)
    

