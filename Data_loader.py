# Function: Load data from txt file
def txt_loader(filepath):
    x = []
    with open(str(filepath), 'r') as f:
        lines = f.readlines()
        for line in lines:
            value = [float(s) for s in line.split()]
            x.append(value)
    return x
