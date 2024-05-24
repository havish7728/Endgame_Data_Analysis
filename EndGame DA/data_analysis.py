from characters import *

# Survival rate by gender
print(avengers_data.groupby('Gender')['Survived'].mean())

# Average screen time by team
print(avengers_data.groupby('Team')['ScreenTime'].mean())

# Survival rate by team
print(avengers_data.groupby('Team')['Survived'].mean())

# Total screen time
print(avengers_data['ScreenTime'].sum())