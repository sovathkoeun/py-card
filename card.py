

card_no = "09443840258344"
double_list = []
event_num = 0
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
    

for x in double_list:
    event_num += int(x)
    
net_sum = odd_number + event_num
if net_sum % 10 == 0:
    print("valid card")
else:
    print("invalid card")
        