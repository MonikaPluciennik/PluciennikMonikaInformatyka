x = [5,3,8,4,1]
n = 5

i = 0
j = i+1; 


for i in range(0,n):
    if x[i] > x[j]:

        pom = x[i]
        x[i]=x[j]
        x[j]=pom 
        j=i+1
        
      
print("Uporządkowany ciag elementow: ", x)





