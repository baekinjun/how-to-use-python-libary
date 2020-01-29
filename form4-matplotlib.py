import matplotlib.pyplot as plt # 파이썬의 라이브러리 matplotlib 함수 사용
from matplotlib.widgets import Button  #matplotlib 함수의 widget 에서 Button import

x=list(range(0,11))                       # 임의로 차트값을 주었습니다
y= list(range(0,110,10))

fig,ax=plt.subplots()
plt.subplots_adjust(left=0.1,bottom=0.3)
p,=plt.plot(x,y,lw=2)


class index (object):                    #class 로 선굵기 증가 감소 함수 이벤트 묶기
    a=0
    def plus(self,event):
        self.a+=1
        p.set_linewidth(1+self.a)           
        
    def minus(self,event):
        self.a-=1
        p.set_linewidth(1+self.a)

        
callback=index()                        #버튼 이벤트를 계속 쓰기 위해 index 함수 callback 과 버튼 디자인
axButton1 =plt.axes([0.1,0.1,0.1,0.1])
btn1=Button(axButton1,label='+')
btn1.on_clicked(callback.plus)
axButton2=plt.axes([0.3,0.1,0.1,0.1])
btn2=Button(axButton2,label='-')
btn2.on_clicked(callback.minus)
      
plt.show()
