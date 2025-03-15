#Exercise 3: Iteration and Conditions: Iteration and Looping: Gene Set Intersection

list_1 = ["Npepl1", "Rab13", "Reg4", "Asb17", "Clcnka", "Nup62", "Upf3a", "Kcnn1", "Ccdc151", "Arg1", "Tmem98", "Mtx3", "Isl1", "Fam53c"]
list_2 = ["Kcnj2", "Rab13", "Reg4","Nol6", "Masp2", "Clcnka", "Upf3a", "Kcnn1", "Arg1", "Krt75", "Smpd3", "Mtx3", "Trim8", "Fam53c"]

intersect_1_2 = []

for i in list_1:
    if i in list_2:
        intersect_1_2.append(i)

for i, v in enumerate(sorted(intersect_1_2), start = 1):
    print(f"{i}. {v}")

