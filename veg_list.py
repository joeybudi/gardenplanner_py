'''
Created on May 5, 2016
Make usable vegetable list for warm and cool climate crops
@author: jwb33
'''

#empty list
warmvegs_type2 = []
warmvegs_price2 = []

coolvegs_type2 = []
coolvegs_price2 = []

#split crop name from the price
#warm season vegs      
with open('warmveg_text','r') as d:
    warmvegs = d.readlines()
    data = warmvegs[0].split()
    warmvegs_type2.append(data[0])
    result = ''
    for item in data[1:]:
        result += item +' '
    warmvegs_price2.append(result)
    for line in warmvegs[1:]:
        strings = line.split()
        warmvegs_type2.append(strings[0])
        warmvegs_price2.append(strings[1])
        
#cool season vegs
with open('coolveg_text','r') as e:
    coolvegs = e.readlines()
    for line in coolvegs:
        strings_cool = line.split()
        coolvegs_type2.append(strings_cool[0])
        coolvegs_price2.append(strings_cool[1])


    
#modify list to add \n on each component    
def modify_list(list1):
    list2 = ''
    for i in list1:
        j = i + '\n'
        list2 += j
    return list2


#use modify_list function to store the modified list
warmvegs_type = modify_list(warmvegs_type2)
warmvegs_price = modify_list(warmvegs_price2)

coolvegs_type = modify_list(coolvegs_type2)
coolvegs_price = modify_list(coolvegs_price2)

#for calculator purposes
all_vegs = warmvegs_type2[1:] + coolvegs_type2[1:]
all_vegs_price = warmvegs_price2[1:] + coolvegs_price2[1:]
all_vegs_revenue = ['2250', '2800', '5700', '4200', '7000', '1200', '9000', '2800', '11300', '7100', '11300']






if __name__ == '__main__':
    print(all_vegs)
    print(all_vegs_price)
    print(all_vegs_revenue)
    #print(warmvegs_type)
    #print(warmvegs)
    #print(line)
    #print (warmvegs_type)
    #print(warmvegs_price)