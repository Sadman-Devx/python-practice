name = input("what's your name? ")

match name:
    case "harry" | "stocks" | "roy":
        print("englang")
    case "hardik":
        print("india")
    case "sadid":
        print("bokacoda")
    case _:
        print("who?")