#This program takes a list of numbers and determines if they are all mutually exclusive from each other

print("This program takes a list of numbers and determines if they are all mutually exclusive from each other.")

list = input("Enter a list of numbers in this syntax: [a,b,c,d,e]- ")

def main(data):
    count = 0
    for k in data:
        for j in range (1, len(data) - 1):
            if k == j:
                count += 1
                if count == 2:
                    return False
                    return True
            
print(list)
