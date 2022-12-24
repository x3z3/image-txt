import os


def readFromFile(filename):
    with open(filename, "r") as f:
        return f.read()

def writeToFile(filename, string):
    with open(filename, "w") as f:
        f.write(string)

def main():
    if not os.path.exists("fragments"):
        print("No fragments found")
        return
    
    data = ""
    for file in os.listdir("fragments"):
        data += readFromFile(os.path.join("fragments", file))   

    writeToFile("aggregated.txt", data)

if __name__ == "__main__":
    main()