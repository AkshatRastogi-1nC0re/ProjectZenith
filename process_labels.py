def gen_labels():
    labels = {}
    with open("converted_keras\\labels.txt", "r") as label:
        text = label.read()
        lines = text.split("\n")
        print(lines)
        for line in lines[0:-1]:
            hold = line.split(" ", 1)
            labels[hold[0]] = hold[1]
    return labels