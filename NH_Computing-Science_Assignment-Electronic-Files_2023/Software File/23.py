def read_from_file():
    attraction = []
    category = []
    visitors = []
    daysOpen = []
    height = []
    with open ("NH_Computing-Science_Assignment-Electronic-Files_2023/Software File/attractions.csv", "r") as readfile:
        line = readfile.readline().rstrip('\n')
        while line:
            items = line.split(",")
            attraction.append(items[0])
            category.append(items[1])
            visitors.append(int(items[2]))
            daysOpen.append(int(items[3]))
            height.append(items[4])
            line = readfile.readline().rstrip('\n')
    return attraction, category, visitors, daysOpen, height

def find_display(attraction, visitors):
    mini = visitors[0]
    minpos = 0
    maxi = visitors[0]
    maxpos = 0
    for index in range(len(visitors)):
        if visitors[index] < mini:
            mini = visitors[index]
            minpos = index
        elif visitors[index] > maxi:
            maxi = visitors[index]
            maxpos = index
    print("The most visited was", attraction[maxpos], "and the least visited was", attraction[minpos])

def write_file(attraction, category, daysOpen):
    with open("service.csv", "w") as writefile:
        for index in range(len(attraction)):
            if category[index] == 'Roller Coaster':
                days = daysOpen[index] % 90
                if 90-days <= 7:
                    writefile.write(attraction[index] + "\n")

def height_restriction(height):
    counter = 0
    for index in range(len(height)):
        temp = height[index]
        if ord(temp[0]) == 49:
            counter+=1
    print("The number of attractions with height restriction 1m and above are", counter)
attraction, category, visitors, daysOpen, height = read_from_file()
find_display(attraction, visitors)
write_file(attraction, category, daysOpen)
height_restriction(height)