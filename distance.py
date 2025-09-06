distances = {
"chandpur": 0.6,
"cumilla": 0.4,
"borishal": 0.9    
}
def main():
    for distance in distances.values():
        print(f"{distance} Km is {convert(distance)} m")

def convert(km):
    return km * 1000
main()