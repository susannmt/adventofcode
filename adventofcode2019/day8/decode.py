width = 25
hight = 6
size = width*hight

pixels = open("input.txt").read()

layers = [list(pixels[i*size:(i+1)*size]) for i in range(len(pixels)//size)]
occ_of_0 = [layer.count("0") for layer in layers]
idx = occ_of_0.index(min(occ_of_0))
print(layers[idx][:].count("1")*layers[idx][:].count("2"))


decoded = []
layers.reverse()
for i in range(size):
    curr = ""
    for layer in layers:
        if layer[i] == "2":
            continue
        elif layer[i] == "0":
            curr = " "
        else:
            curr = "1"
    decoded.append(curr)

for j in range(hight):
    print("".join(decoded[j*width:(j+1)*width]))
