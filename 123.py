import sys
outputf1 = open("output.txt","w")   # output file
inputf2 = open("input.txt","r")     # input file

# reading file
content = inputf2.readlines()
a = {}
b = {}
employees = int(content[0].split(": ")[1])
goodies = content[4:]

prices = []
for item in goodies:
    if item[-2:] == "\n":
        item = item.split(": ")
        name,price = item[0],int(item[1][:-1])
    else:
        item = item.split(": ")
        name,price = item[0],int(item[1])
    prices.append(price)
    a[name] = price
sprices = sorted(prices)      # sorting the prices
diff = []
# difference between the low price goodie and the high price goodie
for i in range(len(prices)-employees):
    diff.append(sprices[i+employees-1] - sprices[i])
for i in a:
    b[a[i]] = i
ind = diff.index(min(diff))

# Writing the Result in output.txtg
out = ["The goodies selected for distribution are:\n","\n"]
for i in sprices[ind:ind+employees]:
    out.append(b[i] + ": " + str(i) + "\n")
out.append("\n")
out.append("And the difference between the chosen goodie with highest price and the lowest price is " + str(min(diff)))
outputf1.writelines(out)
outputf1.close()
