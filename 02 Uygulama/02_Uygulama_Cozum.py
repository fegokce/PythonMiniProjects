# Question 1
def find_num(d, n):
    for i in d.values():
        if i == n or i == str(n):
            return True
    return False
# print(find_num({2:"a","a":"4","t":9},4))

# Question 2
shopping_list = ["apples", "bananas", "kiwi", "pears", "tomatoes"]
shopping_done = {"apples": 3, "kiwi": 5, "tomatoes": 1}
def shopping(l, d):
    total_price = 0
    for i in l:
        if i in d.keys():
            l.remove(i)
    for price in d.values():
        total_price += price
    print(l)
    print(total_price)
# shopping(shopping_list,shopping_done)

# Question 3
class_1 = {"john": 3, "Steve": 6, "Emma": 4}
def average_grade(d):
    sum = 0
    for i in d.keys():
        sum += d[i]
    average = sum / float(len(d))
    return average
# print(average_grade(class_1))

# Question 4
users = {"user1": "password1", "user2": "password2", "user3": "password3"}
def check_pass(d, user_name, password):
    for i in d.keys():
        if i == user_name and d[i] == password:
            return "Logged in"
    return "Could not log in"
# print(check_pass(users,"user1","password2"))

# Question 5
def values(d, l):
    keys_list = []
    for i in d.keys():
        if d[i] == l:
            keys_list.append(i)
    return keys_list
# print(values({4:"is",5:"bb",3:"bb",9:"i"},"bb"))

# Question 6
def above_average(list1):
    sum = 0
    new_list = []
    for i in list1:
        sum += i
    average = sum / len(list1)
    for i in list1:
        if i > average:
            new_list.append(i)
    return new_list
# print(above_average([2, 3, 4, 5, 6]))

# Question 7
def myfn_reverse(lst):
    to_return = []
    for i in range(len(lst)):
        lst_max = max(lst)  # use a custom function here, this is for demo only
        to_return.append(lst_max)
        lst.remove(lst_max)
    return to_return
# print(myfn_reverse([1,2,3,5,6]))

# Question 8
def myfn_na(lst, na_lst):
    for i in range(len(na_lst)):
        na_index = lst.index("NA")
        lst[na_index] = na_lst[0]
        del na_lst[0]
    return lst
# print(myfn_na([1,2,"NA", 4, "NA"], [3, 5]))

#Question 9
def calc_polynomial(x_pows, coeffs, x):
    polynomial_value = 0
    for i in range(len(x_pows)):
        term = coeffs[i]*(x**x_pows[i])
        polynomial_value += term
    return polynomial_value
# print(calc_polynomial([3, 2, 1], [2, 0, 4], 3))

# Question 10
def myfn_samplespace(lst):
    out_dict= dict()
    for i in range(len(lst)):
        event = lst[i]
        if event not in out_dict:
            out_dict[event] = 1
        else:
            out_dict[event] += 1
    for key in out_dict:
        out_dict[key] = out_dict[key]/float(len(lst))
    return out_dict
# print(myfn_samplespace([1,1,1,1,0]))

# Question 11
def hom(s):
    dict = {}
    for i in s:
        if i in dict: dict[i]+=1
        else:dict[i] = 1
    return dict
#print(hom("kara murat kim"))

# Question 12
to_use_for_next_q = hom("kara murat kim")
def frq(dict):
    n_dict = {}
    for key in dict:
        val = dict[key]
        if val not in n_dict:
            n_dict[val] = [key]
        else: n_dict[val].append(key)
    return n_dict
#print(frq(to_use_for_next_q))

# Question 13
exam_dict= {"john":{"exam1":40, "exam2":70}, "murat":{"exam1":20, "exam2":30}, "faruk":{"exam1":35, "exam2":55}, "sow":{"exam1":80, "exam2":90}}
def calc_ex1(ex):
    sum = 0.0
    for std in ex:
        sum +=  ex[std]["exam1"]
    return sum/len(ex)
#print(calc_ex1(exam_dict))

# Question 14
s = "aaaabbaaabbbbbbcccd"
def comps(s):
    ad = ""
    dict = {}
    st = 0
    for i in range(len(s)):
        if i == 0:
            k = s[i]
        else:
            if s[i - 1] != s[i]:
                ad += (str(dict[k]) + k[0])
                st += 1
                k = s[i] + str(st)
        if k in dict:
            dict[k] += 1
        else:
            dict[k] = 1
    ad += str(dict[k]) + k[0]
    print(ad)
# comps(s)

# Question 15
d1 = {1: 2, 3: 4, 5: 6}
d2 = {1: 3, 6: 5, 3: 8}
def comb_la(d1, d2):
    d3 = {}
    for k1 in d1:
        for k2 in d2:
            if k1 == k2:
                if d1[k1] >= d2[k2]:
                    d3[k1] = d1[k1]
                else:
                    d3[k2] = d2[k2]
            else:
                d3[k2] = d2[k2]
                d3[k1] = d1[k1]
    print(d3)
# comb_la(d1,d2)

# Question 16
sample_dictionary = {("Ataturk", "Istanbul", "International"): 30000,
                     ("Ataturk", "Istanbul", "Domestic"): 65000,
                     ("SabihaGokcen", "Istanbul", "International"): 10000,
                     ("SabihaGokcen", "Istanbul", "Domestic"): 30000,
                     ("Menderes", "izmir", "International"): 5000,
                     ("Menderes", "izmir", "Domestic"): 15000}
def calc_fl(d):
    n_d = {}
    for tp in d:
        if tp[1] not in n_d:
            n_d[tp[1]] = d[tp]
        else:
            n_d[tp[1]] += d[tp]
    print(n_d)
# calc_fl(sample_dictionary)

# Question 17
s = "Hello World"
def char_d(s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = (s.index(i),)
        else:
            d[i] += (s.index(i),)
    print(d)
# char_d(s)

# Question 18
def getTopelements(s):
    d = {}
    li = []
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    v_s = sorted(d.values())[len(d.values()) - 3: len(d.values())]
    for i in d:
        if d[i] in v_s:
            li.append(i)
    for i in sorted(li):
        print(i)
# getTopelements("programming")

# Question 19
# dict = {}
# while True:
#    inp = input("Write something:")
#    if inp in dict:
#        dict[inp] += 1
#    else:
#        dict[inp] = 1
#    for i in dict:
#        if dict[i] >=3:
#            exit()

# Question 20
# d = {}
# while True:
#    name = input("Enter the name:")
#    grade = input("Enter the grade:")
#    if grade in d:
#        d[grade].append(name)
#    else:
#        d[grade] = [name]
#    print(d)

# Question 21
# arr={}
# arr[1]=1
# arr["1"]=2
# arr[1] += 1
# sum = 0
# for k in arr:
#     sum += arr[k]
# print (sum)

# Question 22
x = (1, (2, (3,), 4), 5)
# x = (1, (2,3,(4,(5,))), (11, 4))
# x = (1, 2, 3, 4, 5)
n_tuple = tuple()
def make_simple(t):
    global n_tuple
    for i in t:
        if type(i) != tuple:
            n_tuple += i,
        if type(i) == tuple:
            make_simple(i)
# make_simple(x)
# print(n_tuple)

# Question 23
def deep_reverse(t):
    return tuple(deep_reverse(x) if isinstance(x, tuple) else x for x in reversed(t))
# print(deep_reverse(x))
