import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
##############  Title : Exploring Global Media Content: An Analysis of Movies and TV Shows    ##############

# Loading datasheet
data=pd.read_csv('D:\DAVIS\Project\dataset - netflix1.csv')
# Checking number of rows and columns
num_rows, num_columns=data.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")
#Checking first five rows with its data types and columns
print(data.head())
print(data.columns)
print(data.dtypes)
# Checking missing values
missing_data=data.isna()
missing_count=missing_data.sum()
print("Missing count : \n",missing_count)
# There are no missing values
# Checking for duplicate values
duplicates=data.duplicated()
num_duplicates=duplicates.sum()
print(f"Number of duplicate rows: {num_duplicates}")
# There are no duplicate values
# Checking outliers with IQR method
q1=data.select_dtypes(include=['int','float']).quantile(0.25)
q3=data.select_dtypes(include=['int','float']).quantile(0.75)
IQR=q3-q1
outliers = ((data.select_dtypes(include = ['int', 'float'])<(q1-1.5*IQR)) | (data.select_dtypes(include=['int', 'float'])>(q3+1.5*IQR))).any(axis=1)
print(data[outliers])
num_outliers=outliers.sum()
print(f"Number of outliers: {num_outliers}")
# Now removing outliers
data_cleaned=data[~outliers]
print("Number of rows after removing outliers:", data_cleaned.shape[0])
print(data_cleaned)
# Saving cleaned data
output_file='D:\DAVIS\Project\cleaneddata'
data_cleaned.to_csv(output_file, index=False)
print(f"Cleaned dataset saved to {output_file}.")


################################################################################


file_path = 'D:\DAVIS\Project\cleaneddata'
df = pd.read_csv(file_path)
# 1) Bar plot to visualize the 'type' column
sns.set(style = "darkgrid")
plt.figure(figsize = (10,6))
sns.countplot(data = data_cleaned , x = 'rating')
plt.title('Count of Shows/Movies by Rating')
plt.xticks(rotation = 90)
plt.savefig('Bar_plot.png')
plt.show()
# 2) Count plot to visualize the frequency of 'rating' category
sns.set(style = "darkgrid")
plt.figure(figsize = (10,6))
sns.countplot(data = data_cleaned , x = 'rating')
plt.title('Frequency of Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation = 90)
plt.savefig('count_plot.png')
plt.show()
# 3) Line plot for time-series data
data_cleaned_copy=data_cleaned.copy()
data_cleaned_copy['date_added']  = pd.to_datetime(data_cleaned_copy['date_added'])
data_cleaned_copy['release_year']=data_cleaned_copy['date_added'].dt.year
yearly_counts=data_cleaned_copy['release_year'].value_counts().sort_index()
yearly_counts_df=yearly_counts.reset_index()
yearly_counts_df.columns=['Year','Count']
sns.set(style="darkgrid")
plt.figure(figsize=(10,6))
sns.lineplot(data=yearly_counts_df, x='Year', y='Count')
plt.title('Number of titles added over the years')
plt.xlabel('year')
plt.ylabel('Number of titles added')
plt.xticks(rotation=90)
plt.savefig('line_plot.png')
plt.show()
# 4) Histogram for release year
sns.set(style="darkgrid")
plt.figure(figsize=(10,6))
sns.histplot(data=data_cleaned, x='release_year', bins=20, kde=True)
plt.title('Distribution of Release Years')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.savefig('Histogram.png')
plt.show()
# 5) Scatter plot for release year and duration
sns.set(style="darkgrid")
plt.figure(figsize=(10,6))
data_cleaned_copy=data_cleaned.copy()
data_cleaned_copy['duration']=data_cleaned_copy['duration'].str.extract('(\d+)').astype(int)
data_cleaned_copy['duration_hours']=data_cleaned_copy['duration']/60
sns.scatterplot(data=data_cleaned_copy, x='release_year', y='duration_hours')
plt.title('Scatter plot of Release Year vs. Duration')
plt.xlabel('Release Year')
plt.ylabel('Duration (Hours)')
plt.xticks(rotation=90)
plt.savefig('sactterplot.png')
plt.show()
# 6) heatmap for type vs. rating
pivot_table=pd.crosstab(data_cleaned['type'], data_cleaned['rating'])
sns.set(style="darkgrid")
plt.figure(figsize=(10,6))
sns.heatmap(pivot_table,annot=True, cmap="YlGnBu", fmt='d', cbar=False)
plt.title('Correlation Heatmap: Type vs. Rating')
plt.xlabel('Rating')
plt.ylabel('Type')
plt.xticks(rotation=90)
plt.savefig('heat_map.png')
plt.show()
# 7) Box plot for release year
sns.set(style="darkgrid")
plt.figure(figsize=(10,6))
sns.boxplot(data=data_cleaned, x='release_year')
plt.title('Box Plot of Release Year')
plt.xlabel('Release Year')
plt.xticks(rotation=90)
plt.savefig('Box_plot.png')
plt.show()
# 8) Violin plot for release year
sns.set(style="darkgrid")
plt.figure(figsize=(10,6))
sns.violinplot(data=data_cleaned,x='release_year')
plt.title('Violin Plot of Release year')
plt.xlabel('Release Year')
plt.xticks(rotation=90)
plt.savefig('Violin_plot.png')
plt.show()