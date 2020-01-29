import tkinter as tk  #파이썬 라이브러리 중 tkinter을 사용하여 UI 제작
root=tk.Tk()

root.title=("form3")
root.geometry("300x100")
b=[]

def calculate(event):  #계산 이벤트 를 구현
    
    value=tk.Entry.get(String)
    
    value1=tk.Entry.get(x)
    
    if value!='' and value1!='':
        for i in value:
        
            if i=="=":
                continue
            elif i=="y":
                continue
            elif i=="Y":
                continue
            elif i=='"':
                continue

            elif i=="x":
                b.append(value1)
            elif i=="X":
                b.append(value1)
            else:
                b.append(i)
        
        cal=''.join(b)
        result=eval((cal))
        print(result)
        y.delete(0,tk.END)
        y.insert(0,result)
        b.clear()
        

label=tk.Label(root,text="String")              #기본적인 폼및레이아웃 제작 
label.pack(side ="top")
label.place(x=30,y=0)
String=tk.Entry(root,width=20)
String.pack(side="top" ,anchor="center")
label1=tk.Label(root,text="x")
label1.pack()
label1.place(x=40,y=30)
x=tk.Entry(root,width=5)
x.pack()
x.place(x=78,y=30)
label2=tk.Label(root,text="y")
label2.pack()
label2.place(x=40,y=60)
y=tk.Entry(root,width=5)
y.pack()
y.place(x=78,y=60)

button_e =tk.Button(root,text="계산",width=5)  #버튼 레이아웃 밑 이벤트를 걸었습니다.
button_e.bind('<Button-1>',calculate)
button_e.pack()
button_e.place(x=160,y=60)
root.bind('<Return>',calculate)
root.mainloop()

