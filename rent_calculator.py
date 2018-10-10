print("Welcome to the rent calculator! lol")
rent_amount = 1046.15 #constant
internet_bill = 53 #constant


hydro = input("What is the hydro bill amount? ")
hydro_internet_portion = (float(hydro) + internet_bill)

joy_owe = float("{0:.2f}".format(0.3*rent_amount + (hydro_internet_portion/3)))
jane_owe = float("{0:.2f}".format(0.4*rent_amount - (hydro_internet_portion/3)*2))
manisha_owe = float("{0:.2f}".format(0.3*rent_amount + hydro_internet_portion/3))


print("Note: Manisha pays the rent each month.")
print("Note: Jane pays the internet and hydro each month, these are deducted from the amount she owes Manisha.\n")

print("Confirmation:")
print("Jane total: " + str(float("{0:.2f}".format(hydro_internet_portion + rent_amount*0.4 - (hydro_internet_portion/3)*2))))
print("Joy total: " + str(float("{0:.2f}".format(rent_amount*0.3 + (hydro_internet_portion/3)))))
print("Manisha total: " + str(float("{0:.2f}".format(rent_amount - rent_amount*0.3 - rent_amount*0.4 + hydro_internet_portion/3)))+"\n")


print("Transfers:")
print("Jane needs to transfer $"+ str(jane_owe) + " to Manisha")
print("Joy needs to transfer $"+ str(joy_owe) + " to Manisha \n")


