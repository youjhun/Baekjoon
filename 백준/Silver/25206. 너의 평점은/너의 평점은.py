grade = {}
num = 0
avg = 0
grade["A+"] = 4.5; grade["A0"] = 4.0; grade["B+"] = 3.5; grade["B0"] = 3.0; grade["C+"] = 2.5;
grade["C0"] = 2.0; grade["D+"] = 1.5; grade["D0"] = 1.0; grade["F"] = 0.0;
while True:
    try:
        s = input().split()
        if s[2] == "P":
            continue
        num += float(s[1]); avg += float(s[1]) * grade[s[2]]
    except:
        break
print(avg/num)