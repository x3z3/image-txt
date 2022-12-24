import os

AGGREGATE_FILE = "aggregated.txt"

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

    if os.path.exists(AGGREGATE_FILE):
        os.remove(AGGREGATE_FILE)
    
    data = ""
    for file in sorted(os.listdir("fragments")):
        data += readFromFile(os.path.join("fragments", file))   

    writeToFile(AGGREGATE_FILE, data)

if __name__ == "__main__":
    main()