print("Welcome to the rent calculator! lol")
rent_amount = 1046.15 #constant
internet_bill = 53 #constant


hydro = input("What is the hydro bill amount? ")
hydro_internet_portion = (int(hydro) + internet_bill)

joy_owe = float("{0:.2f}".format(0.3*rent_amount + (hydro_internet_portion/3)))
jane_owe = float("{0:.2f}".format(0.4*rent_amount - (hydro_internet_portion/3)*2))
manisha_owe = float("{0:.2f}".format(0.3*rent_amount + hydro_internet_portion))


print("Note: Manisha pays the rent each month.")
print("Note: Jane pays the internet and hydro each month, these are deducted from the amount she owes Manisha.\n")

print("Confirmation:")
print("Jane amount: " + str(float("{0:.2f}".format(internet_bill + rent_amount*0.4 - (internet_bill/3)*2))))
print("Joy amount: " + str(float("{0:.2f}".format(rent_amount*0.3 + (internet_bill/3)))))
print("Manisha amount: " + str(float("{0:.2f}".format(rent_amount - rent_amount*0.3 - rent_amount*0.4 + internet_bill/3)))+"\n")


print("Transfers:")
print("Jane needs to transfer $"+ str(jane_owe) + " to Manisha")
print("Joy needs to transfer $"+ str(joy_owe) + " to Manisha \n")


