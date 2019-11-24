import pandas as pd
cars = pd.read_csv('cars.csv')
a = cars.loc[[0,1,2,3,4], ::2]
b = cars[cars['Model']=='Mazda RX4']
c = cars.loc[cars['Model']=='Camaro Z28', 'cyl']
d1 = cars.loc[(cars['Model']=='Mazda RX4 Wag'), ('Model', 'cyl', 'gear')]
d2 = cars.loc[(cars['Model']=='Honda Civic'), ('Model', 'cyl', 'gear')]
d3 = cars.loc[(cars['Model']=='Ford Pantera L'), ('Model', 'cyl', 'gear')]
print(a, '\n')
print(b, '\n')
print('No. of cylinders of Camaro Z28:\n', c, '\n')
print('Cylinders and gears:')
print(pd.concat([d1,d2,d3]))

