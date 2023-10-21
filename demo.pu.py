A= []
n = int(input("Order of square matrix:"))   
print("Row wise elements:")  
  
for i in range(n):  
    r = []  
    for j in range(n): 
        r.append(int(input()))  
    A.append(r)  
  
print("Matrix A:")
for i in range(n):  
    for j in range(n):  
        print(A[i][j], end=" ")  
    print() 