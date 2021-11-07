def health_calculator(age,apple_ate,cig_smoked):
    health = age+(apple_ate*0.1)-(cig_smoked*0.5)
    print(health)

myData=[21,1,5]
health_calculator(myData[0],myData[1],myData[2])
health_calculator(*myData)