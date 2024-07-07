#Dictionary as a parameter to a function of format dic={'item name':price} and display item if its value is more than 150

def checkdict(dic):
    for i in dic:
        if dic[i]>150:
            print(i)

dict={'TV':45000,'Book':145,'pen':50}
checkdict(dict)
