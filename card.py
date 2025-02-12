

card_no = "09443840258344"
double_list = []
odd_number =  0
Number = list(card_no)
for (idx, val) in enumerate(Number):
    if idx % 2 !=0:
        odd_number += int(val)
    else:
        double_list.append(int(val)*2)
print(double_list)

double_string = ""

for x in double_list:
    double_string += str(x)

double_list = list(double_string)
print(double_list)
        