import os
MAXCHAR_LENGTH = 65000

def main():
    if not os.path.exists("encoded.txt"):
        print("The encoded file does not exist")
        return
    if not os.path.exists("fragments"):
        os.mkdir("fragments")
    else:
        for file in os.listdir("fragments"):
            os.remove(os.path.join("fragments", file))

    with open("encoded.txt", "r") as f:
        data = f.read()
    frags = 0
    for i in range(0, len(data), MAXCHAR_LENGTH):
        with open(f"fragments/encoded_{frags}.txt", "w") as f:
            f.write(data[i:i+MAXCHAR_LENGTH])
        frags += 1

if __name__ == "__main__":
    main()