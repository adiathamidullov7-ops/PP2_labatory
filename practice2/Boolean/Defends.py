students = {
    "Zhusup" : 100,
    "Arslan" : 90,
    "Bekarys" : 80,
    "Nursultan" : 70
}
for name, x  in students.items():
    if 0 <= x <50:
        gpa = "FX"
    elif 50 <= x <=70:
        gpa = "2.33"
    elif 70 <= x <= 75:
        gpa = "2.60"
    elif 75 <= x <= 80:
        gpa = "3"
    elif 80 <= x <= 90:
        gpa = " 3.33"
    elif 90 <= x <= 95:
        gpa = "3.67"
    else:
        gpa = "4.00"
    print(f"{name}: {gpa}")