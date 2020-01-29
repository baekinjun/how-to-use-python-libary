import pandas as pd # 파이썬의 pandas 라이브러리 함수 사용
import time
df= pd.read_csv(r'C:\Users\VIP-HS\Desktop\백인준\test.csv',encoding='cp949') #csv 파일 읽어오기
df.fillna(0) # NA 값 바꾸기 
i=1
while i<10: #1번부터 9번까지 object String 값을 float 으로 변경해주었습니다.
    df[df.columns[i]]=pd.to_numeric(df[df.columns[i]],errors='coerce')
    i+=1
j=0

while j<=10:
    if j<10:
        print("")
        start=time.time() 
        print('p{0}:min:'.format(j),df[df.columns[j]].min(),'p{0} min:runtime'.format(j),time.time()-start) #min값 계산
        start=time.time()
        print('p{0}:max:'.format(j),df[df.columns[j]].max(),'p{0} max:runtime'.format(j),time.time()-start) #max 값 계산
        start=time.time()
        print('p{0}:average:'.format(j),df[df.columns[j]].mean(),'p{0} average:runtime'.format(j),time.time()-start) #평균 게산
        start=time.time()
        print('p{0}:standard deviation:'.format(j),df[df.columns[j]].std(),'p{0} standard deviation:runtime'.format(j),time.time()-start) #표준편차 계산
        start=time.time()
        print('p{0}:meadian:'.format(j),df[df.columns[j]].median(),'p{0} median:runtime'.format(j),time.time()-start)#중간값 계산
        print('p{0}:length:'.format(j),len(df[df.columns[j]])) #줄수 계산
        print("                                                                                                                           ")
    else:
        time.sleep(500)
    j+=1

    
