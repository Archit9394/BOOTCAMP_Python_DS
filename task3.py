# 3.Create a list of given structure and run 
# 	x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
# Access list [1, 2, 3, 4]
# Access list [600,  700]
# Access list [100, 300, 500, 600, 800]
# Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
# Access list [10]
# Access list [ ]

given_list=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

print (given_list[5][:4])
print (given_list[6:8])
print (given_list[::2])
print (given_list[::-1])
print (given_list[5][5][0])
print (given_list[5][5][0])
print (given_list[-1:-4])