# Python data types: int, float, bool, str

intiger_data = 564441654
float_data = 54456.54485
bool_data = True # or False
str_data = "KUJHFDJKSCGUHIDJ6+8558565+KJGIGHF" #or 'jsdhbfjdsfb34234sjnxckjsd@#$^+-/+9'

print(type(intiger_data))
print(type(float_data))
print(type(bool_data))
print(type(str_data))

# Calculations

print(2+2)
print(2-2)
print(2*2)
print(2/2)

# Basic
prefix="Py"
print(prefix)
print(prefix + "thon")

prefix="thon"
print(prefix)

print(prefix + "JJJJ")

# Touple

tup = ("fdslkgldfk", 2342345, 254435.345345, True, False)

dictionary = {"dfvdf": "dsffvdfg", 23423: "dfgdfg", "sddsf": {
    123324: 234234
}}

print(tup)

# Function
def func():
    print("Hey I'm func, Thank you!")

func()

# Func paramiter
def func_params(name):
    print("Hey, I'm: ", name)

func_params("Ahamad")

# Func paramiters
def func_paramiters(name, age, cls, institute):
    print(f"Hey, I'm {name}, my ages {age}, my class {cls}, and my instituet is {institute}")

func_paramiters("Ahamad", 18, "BEng", "YNU")

# Multiple Paramiter with *kwrg --> single stare (*) meanning is argumentrs ---> ("dfgdfk", "dlfkvjgodf", "rfgjdof")
def params(*kwrg): # {}
    print(kwrg)

    

params("dfgdfk", "dlfkvjgodf", "rfgjdof")

# MUiltiple Paramiter with **kworgs -- only two stars (**) meanning is Keywords and argumentrs --> dict
def params_stars(**kwargs):
    print(kwargs)

    return kwargs

ret = params_stars(ahamad="Ahamad", age=25, sex="Male", cls=2024) # {'ahamad': 'Ahamad', 'age': 25, 'sex': 'Male', 'cls': 2024}


print(ret["ahamad"])

# Work with python: Calculator
def calc(oparator, int_val):
    result = 0
    if(oparator=="+"):
        result = int_val + 10
    elif(oparator=="-"):
        result = int_val - 10
    elif(oparator=="/"):
        result=int_val / 10
    elif (oparator=="*"):
        result = int_val * 10
    else:
        result="Wrong input!"

    print(result)

calc("+", 20)
calc("-", 5)
calc("/", 20)
calc("*", 20)
calc("hhh", 50)

# calc("+", 2) + calc("-", 20) * calc("/", 20)