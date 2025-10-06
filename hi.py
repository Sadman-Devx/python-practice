#name = input("what's your name? ").strip().title()
#age = input("what's your age? ")
#print(f"hello, {name} {age}")
#print("hello," ,name,age)
#print("hello, " + name.strip().title().translate() + " " + age)
em = ":D"
def main():
    global em 
    em ="😊"
    name = input("what's your name? ").title()
    age  = input("what's your age? ").title()
    hello(name,age)

def hello(n,a):
    
    print("hello," ,n,a,em)

main()    