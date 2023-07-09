
with open("Off_Pulses.txt", "r") as pulseData:
    pulses = pulseData.readline().split(",")

pulsesClean = []

for i in pulses:
    pulsesClean.append(i.replace(" ", ""))

pulsesClean = pulsesClean[6:-1]
bits = []
for i in pulsesClean:
    if int(i) < 0:
        bits.append(int(i))

byteCount = ""
binary = ""
counter = 1

for i in bits:
    counter += 1
    if i < -1000:
        byteCount += " "
        binary += "1"
    else:
        byteCount += " "
        binary += "0"
    if counter % 8 == 1 and counter != 1:
        byteCount += str(int(counter / 8))
        binary += " "
print(byteCount)
print(binary)
