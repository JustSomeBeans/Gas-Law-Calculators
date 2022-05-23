import time
def calculate():
    print("Note: Enter the missing value as zero") 
    v1 = float(input("Input first volume in liters \n")) #inputs of variables
    m1 = float(input("Input first molarity in mol/L \n"))
    v2 = float(input("Input second volune in liters \n"))
    m2 = float(input("Input second molarity in mol/L \n"))
    no = 0
    if v1 == 0: #tests if variable needs to be calculated for
        v1 = m2 * v2 / m1
        no = 1 #confirms 0 was stored as the calculated value
        if v1 != 1:
            print("The volume of your first solution was " + str(v1) + "l iters")
        else: #Corrects grammar if the answer is 1
            print("The volume of your first solution was " + str(v1) + " liter")
    if m1 == 0:
        m1 = m2 * v2 / v1
        no = 1 
        if m1 != 1:
            print("The molarity of your first solution was " + str(m1) + " mols per liter")
        else:
            print("The molarity of your first solution was " + str(m1) + " mol per liter")
    if v2 == 0:
        v2 = m1 * v1 / m2
        no = 1
        if v2 != 1:
            print("The volume of your second solution is " + str(v2) + " liters" )
        else:
            print("The volume of your second solution is " + str(v2) + " liter" )
    if m2 == 0:
       m2 = m1 * v1 / v2
       no = 1
       if m2 != 1:
           print("The molarity of your second solution is " + str(m2) + " mols per liter")
       else:
            print("The molarity of your second solution is " + str(m2) + " mol per liter")
    if no == 0: #tests to see if 0 was stores as the calculated value
        print("Please input 0 as the value you are trying to find")
        calculate()
    yn = str(input("Do you want to do another calculation (y/n)\n"))
    if yn == str("y"): #re-executes calculator if answer is yes
        calculate()
    if yn == str("n"): #exits program if answer is no
        print("Goodbye")
        time.sleep(1)
calculate()
