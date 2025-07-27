def skyline (*args):
    longest_building=0
    for tool in args:
        if tool > longest_building:
            longest_building=tool
    return  longest_building        
all_building=(3,7,15,2,9)      
print(skyline(*all_building))



