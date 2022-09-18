# List of multiple matrices list elements
print("\n")
k = int(input("Enter the number of matrices: "))

matrixListApnd = []
matrixListSum =[]

n = int(input("Enter # of colums n: "))
m = int(input("Enter # of rows m: "))
print(" ")

for k in range(k):
    matrixList = [[ "----------" for j in range(n)] for i in range(m)]
    #print("Foramt: ", matrixList)

    for i in range(m):
        for j in range(n):
            matrixList[i][j] = int(input("Enter element"+ str(i+1)+ "x"+ str(j+1)+ ": "))
      
    print("\nMatrix (" + str(k+1) +"): \n"+ str(matrixList)+"\n")
    print("---------------------")
    for x in matrixList:
        matrixListApnd.append(x.copy())

        
print ("Matrix/List of multiple matrices list elements: \n", matrixListApnd)
print("\n")