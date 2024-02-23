with open(r'C:\Users\alfa18\Desktop\hw\recipes\1.txt','r', encoding='utf-8') as file_1:
    sum_1 = {}
    counting_1 = 0
    for i in file_1.readlines():
        counting_1 += 1
        sum_1['1.txt'] = counting_1
#print(sum_1)
with open(r'C:\Users\alfa18\Desktop\hw\recipes\2.txt', 'r') as file_2:
    sum_2 = {}
    counting_2 = 0
    for n in file_2.readlines():
        counting_2 += 1
        sum_2['2.txt'] = counting_2
# print(sum_2)
with open (r'C:\Users\alfa18\Desktop\hw\recipes\3.txt', 'r') as file_3:
    sum_3 = {}
    counting_3 = 0
    for z in file_3.readlines():
        counting_3 += 1
        sum_3['3.txt'] = counting_3
# print(sum_3)
uniq = dict(list(sum_1.items()) + list(sum_2.items()) + list(sum_3.items()))

uniq_sorted = sorted(uniq.items(), key=lambda x: x[1])

new_dict_unic_sorted = dict(uniq_sorted)
print(new_dict_unic_sorted)