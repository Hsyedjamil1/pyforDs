# step involove in data visulization
# Step - 1 Import libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Step - 2 you have to set a theme for seaborn
sns.set(style="ticks", color_codes=True)

# Step - 3 Importing the dataset
ship = sns.load_dataset("titanic")
# print(ship)

# Step - 4 Plot basic graph
p = sns.countplot(x="sex", data=ship)
plt.show()

# # Step - 5 Plot basic graph with 2 variable
p = sns.countplot(x="sex", hue="class", data=ship)
plt.show()

# Step - 6 Plot basic graph with 2 variable with title
p = sns.countplot(x="sex", hue="class", data=ship)
p.set_title("Titanic Passengers")
plt.show()