seed = int(input("Enter seed: "))
steps = [seed]

while seed != 1:
    if seed % 2 == 0:
        seed /= 2
    else:
        seed = 3 * seed + 1

    steps.append(int(seed))

print("Number of steps: ", len(steps))
print("Highest number: ", max(steps))
print("Steps: ", steps)
