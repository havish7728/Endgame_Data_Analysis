from characters import *

# Plot the survival rate by gender
sns.barplot(x='Gender', y='Survived', data=avengers_data)
plt.title('Survival Rate by Gender')
plt.show()

# Plot the average screen time by team
sns.barplot(x='Team', y='ScreenTime', data=avengers_data)
plt.title('Average Screen Time by Team')
plt.xticks(rotation=45)
plt.show()

# Plot the survival rate by team
sns.barplot(x='Team', y='Survived', data=avengers_data)
plt.title('Survival Rate by Team')
plt.xticks(rotation=45)
plt.show()
