annual_tax_for_basketball_training = int(input())

sneakers = annual_tax_for_basketball_training - (annual_tax_for_basketball_training * 0.40)
outfit = sneakers - (sneakers * 0.20)
ball = outfit * 0.25
accessories = ball * 0.20
total_sum = annual_tax_for_basketball_training + sneakers + outfit +ball + accessories

print(total_sum)