principal = 1000
rate = 0.05
num_years = 5
year = 1
while year <= num_years:
    principal = principal * (1 + rate)
    # print(year, principal)
    print('{0:3d}, {1:10.2f}'.format(year, principal))
    year += 1
