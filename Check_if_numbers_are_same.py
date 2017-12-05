
#This program takes a list of numbers and determines if they are all mutually exclusive from each other

print("This program takes a list of numbers and determines if they are all mutually exclusive from each other.")

def main(data):
    copy = []
    # iterate all data
    for k in data:
        # if k is ',' do nothing, because ',' is not the data that we want to check
        if k == ',':
            pass
        else:
            # iterate the copy list
            for j in copy:
                # if k is in copy, then it has duplicate return true to exit function
                if k == j:
                    return True
            # if after the iteration of data, it means k is not in copy,
            # then store it in copy for later check
            copy.append(k)
    # duplicate not found, return false
    return False

# loop the prompt
while True:
    list = input("Enter a list of numbers in this syntax: [a,b,c,d,e]-, Enter q to quit: ")
    # if q then quit
    if list == 'q': 
        break
    print(list)
    if main(list) == True:
        print('Elements in the list are not mutually exclusive from each other')
    else:
        print('Elements in the list are mutaully exclusive from each other')
