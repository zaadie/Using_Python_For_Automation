# 1. Count the amount of numbers from the 'numbers.csv' file
vals = []
count = 0
with open('numbers.csv') as f:
    for line in f:
        try:
            vals.append(int(line.strip()))
            count+=1
        except ValueError:
            pass

def max_val():
    mx = max(vals)
    print("The max number in the file is: %d" % (mx))
    return mx

def min_val():
    mn = min(vals)
    print("The min number in the file is: %d" % (mn))
    return mn

def avg():
    n = sum(vals)
    d = len(vals)
    x = float(n)/d
    a = float("{:.2f}".format(x))
    print("The average number of the file is: " , a)
    return(a)

def most_common():
    c = max(set(vals), key=vals.count)
    print("The most repeated/occuring numbers is: %d" % (c))
    return c

def unique():
    u = list(set(vals))
    u_amt = len(u)
    print("The amount of unique numbers are: %d" % (u_amt))
    return(u)

def amt_nums():
    print("The amount of numbers in the file are: %d" % (count))
    return(count)

# 1. Count the amount of numbers
amt_nums()

# 2. Find the max/highest number
max_val()

# 3. Find then min/lowest number
min_val()

# 4. Calculate the average to two decimal places
avg()

# 5. Find the most repeated/occurring number
most_common()

# 6 Find the amount of unique numbers
unique()