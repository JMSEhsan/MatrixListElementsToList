# List of multiple matrices list elements
print("\n")
k = int(input("Enter the number of matrices: "))

matrixListApnd = []
matrixListSum =[]

n = int(input("Enter # of rows n: "))
m = int(input("Enter # of colums m: "))

print(" ")

for l in range(k):
    matrixList = [[ "----------" for j in range(m)] for i in range(n)]
    #print("Foramt: ", matrixList)

    for i in range(n):
        for j in range(m):
            matrixList[i][j] = int(input("Enter element ("+ str(i+1)+ ", "+ str(j+1)+ ") : "))
      
    print("\nMatrix (" + str(k+1) +"): \n"+ str(matrixList)+"\n")
    print("-------------------------------")
    for x in matrixList:
        matrixListApnd.append(x.copy())

        
print("Matrix/list of list elements of the {} matrices/lists:" .format(k))
print(matrixListApnd)
print("\n")