input_data = open('intput.txt','r')
data = input_data.readlines()
a=str(data[0])
b=str(data[1])
a=a.split()
b=b.split()
x1=float(a[0])
y1=float(a[1])
x2=float(a[2])
y2=float(a[3])
xa=float(b[0])
ya=float(b[0])
if x1 == x2:
    xb = 2 * x1 - xa
    yb = ya
if y1 == y2: 
    xb = xa
    ya = 2 * y1 - ya
output_data = open('output.txt','w')
output_data.write(str(int(xb)) + ' ' + str(int(yb)))
input_data.close()
output_data.close()