import math

num = 100 #등분표 수
r1 = 1 #반지름
h = 100 #높이 등분
z = r1/h 
theta = 360/num*math.pi/180 #rad
xy = [] #꼭짓점

#1층추가, 반지름변경, 2층추가, 반지름 ... 끝까지 채우기
r2 = 1
for i in range(h): 
    r2 = math.pow((math.pow(r1,2)-math.pow(z*(i+1),2)),0.5) #반지름 재정의
    for j in range(num): #등분수만큼 돌아가면서 좌표 append
        xy.append([r2*math.cos(j*theta), r2*math.sin(j*theta),z*i]) 

tri = []
cnt = 0
temp = 0

for i in range(h-1): 
    for j in range(num-1): #yello tri
        tri.append([cnt,cnt+num,cnt+1])
        cnt += 1
    tri.append([cnt,cnt+num,0+num*i]) #예외항추가
    cnt += 1 
    for j in range(num-1): #blue tri
        tri.append([temp+1,temp+num,temp+(num+1)])
        temp += 1
    tri.append([0+num*i,temp+num,num*(i+1)]) #예외항추가
    temp += 1

a = open('hemisphere.vtu', 'w')
a.write('# vtk DataFile Version 3.0\n')
a.write('test123\n')
a.write('ASCII\n')
a.write('DATASET UNSTRUCTURED_GRID\n')

a.write('POINTS '+str(len(xy))+' float\n') #꼭짓점 좌표
for i in range(len(xy)): #16
    a.write(str(xy[i][0]) + ' '+ str(xy[i][1])+ ' ' + str(xy[i][2])+' \n') 

a.write('CELLS '+str(len(tri))+' '+str(4*len(tri))+'\n') #도형 정의
for i in range(len(tri)):
    a.write('3 '+str(tri[i][0])+' '+str(tri[i][1])+' '+str(tri[i][2])+'\n')

a.write('CELL_TYPES '+str(len(tri))+'\n') #도형 형태 정의
for i in range(len(tri)):
    a.write('5\n') #삼각형 개수만큼 생성

a.close()