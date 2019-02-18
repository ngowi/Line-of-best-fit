# line of best fit for Data analysis

x = input("Enter x(blank to quit!): ")

product_xy = 0
sum_x = 0
sum_y = 0
sum_square_x = 0
n = 0

while x != "":
    y = input("Enter y: ")
    new_x = float(x)
    new_y = float(y)
    sum_x += new_x
    sum_y += new_y
    product_xy += new_x * new_y
    sum_square_x += new_x**2
    n = n+ 1
    x = input("Enter x(blank to quit!): ")

x_average = sum_x / n
y_average = sum_y / n


m = (product_xy - (sum_x * sum_y / n)) / (sum_square_x - (sum_x**2/n))

b = y_average - (m* x_average)

if b > 0:
    print("y = %.2fx + %.1f"%(m, b))
else:
    print("y = %.2fx - %.1f"%(m, -1*b))

    

    
    
    
    
    
