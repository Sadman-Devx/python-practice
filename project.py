"""# Ask user for their name,remove whitespace & capitalize user's name
name = input("what is your name? ").strip().title()

first,medlast,last = name.split(" ")
# Say hello to user
print(f"hello, {first}")


"""

def main():
    name = input("what's your name? ").strip().title()
    hello(name)
    

def hello(to="world"):
    print("hello,",to)

main()    