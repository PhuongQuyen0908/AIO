import math

#Random and Math modules:
if False:
    import math
    
    x = input("Nhap x: ")
    x_float = float(x)
    print("Tri tuyet doi cua", x ,":", math.fabs(x_float))

    x1= input("Nhap so duong x: ")
    x1_float=float(x1)
    print("Can bac hai cua", x1 ,":", math.sqrt(x1_float))

    x2= input("Nhap mot so bat ky: ")
    x2_float=float(x2)
    print("Gia tri sin cua", x2 ,":", math.sin(x2_float))
    print("Gia tri e^x cua", x2 ,":", math.exp(x2_float))
    print("Gia tri logarit cua", x2 ,":", math.log(x2_float))       #Ham logarit se duoc ung dung rat nhieu!!!
    print("So pi:",math.pi )
    print("So e:",math.e)

if False: 
    import random
    #generating a random floating-point number in [0,1]
    print(random.random())
    print(random.random())
    #generating a random int number in [1,9]
    print(random.randint(1,9))
    print(random.randint(1,5))



#Basic operators:
if False:
    x = 7.5
    y = 5
    print(x + y)        #Cộng
    print(x - y)        #Trừ
    print(x * y)        #Nhân
    print(x / y)        #Chia
    print(x//y)         #Chia lấy nguyên
    print(x%y)          #Chia lấy dư
    print(x**y)         #x^y

#Example
if False:
    #Chuyển độ C thành độ F
    tempC = float(input("Nhập độ C: "))
    tempF_res = 9*tempC/5 + 32
    print("F = ", tempF_res )

    #Chuyển độ F thành độ C
    tempF = float(input("Nhập độ F: "))
    tempC_res = (tempF-32)*5/9
    print("F = ", tempC_res )

#Functions:
#1. Define function name: lowercase with underscore, begin with a verb
#2. Determine function paramenter
#3. Docstring: to describe and explain the function
#4. Output: the result of the function
#5. Viết code để sau này đọc lại =))

#Example 1:
if False:
    def compute_rectangle_area(height =0 ,width =0):
        '''
        This function aims to compute the area of the area
        height: is the height of the rectangle
        width: is the width of the rectangle
        This function returns the area of the rectangle
        '''
        rec_area = height*width
        return rec_area
    print(compute_rectangle_area())
#Example 2:
if False:
    def compute_circumference_of_unit_circle(degree=0):
        '''
        Given a degree
        This function aims to compute the circumference of a unit circle
        A unit circle is a circle with radius = 1
        C = 2*pi*r
        ''' 
        sin = math.sin(math.radians(degree))
        length = sin*(360/degree)
        return length
    print(compute_circumference_of_unit_circle(1))

    #Sử dụng lượng giác
    def compute_area_of_unit_circle(degree=0):
        '''
        Given a degree
        This function aims to compute the area of a unit circle
        A unit circle is a circle with radius = 1
        S = pi*r*r = pi (because r = 1)
        ''' 
        sin = math.sin(math.radians(degree))
        cos = math.cos(math.radians(degree))
        m = (sin*cos)/2
        area = m* (360/degree)
        return area
    print(compute_area_of_unit_circle(1))

    #Sử dụng tích phân
    # Aest ~ sum( f(xi)*delta(xi) ) (i=1,2,...n)

#Example 3: Đạo hàm cho hàm liên tục
#Đạo hàm = (delta(y))/(delta(x))
#Đạo hàm là mức độ thay đổi của y khi x thay đổi 


#Condition: if, if else , if elif else
if False:
    #if
    def ReLu(x):
        res=0
        if(x>0):
            res=x
        return res
    
    def ReLu1(a,b):
        res=0
        if(a>0):
            res=math.sqrt(b)
        else:
            res= b*b
        return res
    
    def ReLu2(x):
        res =""
        if(x>0):
            res="So duong"
        elif (x<0):
            res="So am"
        else: 
            res="So khong"
        return res
    
    print(ReLu(3))
    print(ReLu1(1,2))
    print(ReLu2(-4))


#Activation function
#Sigmoid function
def sigmoid_function(u):
    '''
    Hàm này thường được dùng để ép nó về trong khoảng [0,1]
    Ta không qtam bản thân giá trị của dữ liệu
    Ta chỉ qtam đến THỨ TỰ của dữ liệu
    Mỗi ngôn ngữ dùng một số bit nhất định để lưu trữ dữ liệu
    Ta có thể dùng hàm này để tránh trường hợp tràn số
    '''
    result = 1/(1+math.exp(-u))
    return result


#Overflow and Underflow
#Underflow: nhỏ quá không mô tả được ==> gán bằng 0
#Overflow: lớn quá không mô tả được ==> trả về số lớn nhất hoặc inf
#Để tránh trường hợp này ta có thể dùng hàm sigmoid


#Softmax function: chuyển các giá trị của một vector thành giá trị xác suất
#Give 3 values
v1,v2,v3 = 1.0, 2.0 ,3.0

#Cách 1:
total = math.exp(v1)+ math.exp(v2)+ math.exp(v3)

s1  = math.exp(v1)/total
s2  = math.exp(v2)/total
s3  = math.exp(v3)/total

#Nhược: hàm exp có thể dẫn đến overflow khi v1,v2,v3 quá lớn
print(s1, s2, s3)

#Cách 2:
max_value = max(v1,v2,v3)

e_v1 = math.exp(v1 - max_value)
e_v2 = math.exp(v2 - max_value)
e_v3 = math.exp(v3 - max_value)

total_e = e_v1+e_v2+e_v3

s1  = math.exp(e_v1)/total_e
s2  = math.exp(e_v2)/total_e
s3  = math.exp(e_v3)/total_e

print(s1,s2,s3)
#Nhược: chấp nhận underflow để khắc phục overflow
