# importing pandas library

# importing matplotlib library

    
# creating dataframe
df = pd.DataFrame({
    'Name': ['John', 'Sammy', 'Joe'],
    'Age': [45, 38, 90]
})

# plotting a bar graph
# df.plot(x="Name", y="Age", kind="bar")
sns.barplot(data=df, x='Name', y='Age')