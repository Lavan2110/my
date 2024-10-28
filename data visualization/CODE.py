import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(r"C:\Users\lavan\OneDrive\Desktop\MY PROJECTS\data visualization\data sheet.csv")
department=data['Department']
Loc=data['Loc']
Gender=data['Gender']
Ratings=data['Rating']
salary=data['Salary']
salary_numeric = [int(sal.replace("$", "").replace(",", "")) for sal in salary]


data = pd.DataFrame({
    'Department': department,
    'Salary': salary_numeric,
    'Gender':Gender,
    'Rating':Ratings,
    'Loc':Loc
})

gender_count = Gender.value_counts()
print("Gender Distribution:\n", gender_count)
gender_dept_count = data.groupby(['Department', 'Gender']).size().unstack()
print("\nGender Distribution by Department:\n", gender_dept_count)

gender_loc_count = data.groupby(['Loc', 'Gender']).size().unstack()
print("\nGender Distribution by Location:\n", gender_loc_count)
avg_pay_dept =data.groupby('Department')['Salary'].mean().sort_values(ascending = False)
print("\nAverage Pay by Department:\n", avg_pay_dept)
avg_pay_loc = data.groupby('Loc')['Salary'].mean().sort_values(ascending=False)
print("\nAverage Pay by Location:\n", avg_pay_loc)
rating_dist = data['Rating'].value_counts(normalize=True) * 100
print("\nRatings Distribution (%):\n", rating_dist)
gender_pay_gap_dept = data.groupby(['Department', 'Gender'])['Salary'].mean().unstack()
gender_pay_gap_dept['Pay Gap'] = gender_pay_gap_dept.apply(lambda x: x['Male'] - x['Female'], axis=1)
print("\nGender Pay Gap by Department:\n", gender_pay_gap_dept)
gender_pay_gap_loc = data.groupby(['Loc', 'Gender'])['Salary'].mean().unstack()
gender_pay_gap_loc['Pay Gap'] = gender_pay_gap_loc.apply(lambda x: x['Male'] - x['Female'], axis=1)
print("\nGender Pay Gap by Location:\n", gender_pay_gap_loc)
plt.figure(figsize=(10, 6))
sns.countplot(x='Gender', data=data)
plt.title('Gender Distribution')
plt.show()
plt.figure(figsize=(14, 8))
sns.countplot(x='Department', hue='Gender', data=data)
plt.title('Gender Distribution by Department')
plt.show()
plt.figure(figsize=(14, 8))
sns.countplot(x='Loc', hue='Gender', data=data)
plt.title('Gender Distribution by Location')
plt.show()
plt.figure(figsize=(14, 8))
avg_pay_dept.plot(kind='bar')
plt.title('Average Pay by Department')
plt.ylabel('Average Salary')
plt.show()
plt.figure(figsize=(14, 8))
avg_pay_loc.plot(kind='bar')
plt.title('Average Pay by Location')
plt.ylabel('Average Salary')
plt.show()
plt.figure(figsize=(10, 6))
sns.countplot(x='Rating', data=data, order=rating_dist.index)
plt.title('Ratings Distribution')
plt.show()
gender_location_crosstab = pd.crosstab(data['Gender'], data['Loc'])
print("\nGender & Location Crosstab:\n", gender_location_crosstab)
gender_department_crosstab = pd.crosstab(data['Gender'], data['Department'])
print("\nGender & Department Crosstab:\n", gender_department_crosstab)
gender_rating_crosstab = pd.crosstab(data['Gender'], data['Rating'])
print("\nGender & Rating Crosstab:\n", gender_rating_crosstab)

