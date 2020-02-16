flag1 = ""
flag2 = ""

with open("./cattos.jpg", "rb") as cat:
    cat_full = cat.read()

with open("./kitters.jpg", "rb") as kit:
    kit_full = kit.read()

for i in range(min(len(kit_full), len(cat_full))):
    if kit_full[i] != cat_full[i]:
        flag1 += str(chr(kit_full[i]))
        flag2 += str(chr(cat_full[i]))
print(flag1)
print(flag2)
