import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample dataset
data = {
    'Character': ['Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow', 'Hawkeye', 'Ant-Man', 'Rocket', 'Nebula', 'War Machine', 'Captain Marvel'],
    'ScreenTime': [34, 30, 28, 15, 22, 20, 18, 12, 10, 8, 12],
    'Survived': [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
    'Team': ['Original Avengers', 'Original Avengers', 'Original Avengers', 'Original Avengers', 'Original Avengers', 'Original Avengers', 'New Avengers', 'Guardians of the Galaxy', 'Guardians of the Galaxy', 'New Avengers', 'New Avengers'],
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female']
}

avengers_data = pd.DataFrame(data)