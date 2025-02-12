

card_no = "09443840258344"
odd_number =  0
Number = list(card_no)
for (idx, val) in enumerate(Number):
    if idx % 2 !=0:
        odd_number += int(val)
    else:
        pass

print(odd_number)
        