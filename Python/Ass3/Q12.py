#1
# def print_pattern(rows):
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()
# num_rows = 5
# print_pattern(num_rows)

#2
#3
#def print_pattern(rows):
#    for i in range(rows,0,-1):
#        for j in range(i,0,-1):
#            print(j,end=" ")
#        print()
#num_rows=5
#print_pattern(num_rows)

#4
#def print_pattern(rows):
#    for i in range(1,rows+1):
#        for j in range(0,i):
#            print(i,end=" ")
#        print()
#num_rows=5
#print_pattern(num_rows)

#5
#def print_pattern(rows):
#    for i in range(rows):
#       for j in range(i):
#            print( " ",end=" ")
#        for k in range(rows-i):
#            print(k+i+1,end=" ")
#        print()    
    
#num_rows=5
#print_pattern(num_rows)

#7
#def print_pattern(rows):
#    for i in range(rows):
#        for j in range(rows):
#           print("*",end=" ")
#        print()    
    
#num_rows=5
#print_pattern(num_rows)

#Q13
def print_pattern(rows):
   for i in range(rows):
       for j in range(i):
           print( " ",end=" ")
       for k in range(rows-i):
           print("$",end=" ")
       print()    
    
num_rows=5
print_pattern(num_rows)





