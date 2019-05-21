##导包
import pandas as pd
# from pandasql import sqldf
# import plotly.plotly as py
# import plotly.graph_objs as go
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# init_notebook_mode(connected=True)
import matplotlib.pyplot as plt
# import seaborn as sns
import numpy as np


def data_type(bf):
    for i in bf.columns:
        print(i,"------>>",bf[i].unique())


bf = pd.read_csv("/Users/maomao/Downloads/BlackFriday.csv", header='infer')
# data info
bf.info()
plt.figure()
plt.hist(bf['Purchase'],bins=100)
plt.xlabel('purchase')
plt.ylabel('count')
# plt.show()
# data type
data_type(bf)

# Gender and marriage impact on purchases
bf_gen_mar = bf.groupby(['Gender', 'Marital_Status']).count().reset_index('Marital_Status')
bf_gen = bf.groupby(['Gender']).count()
# Female_0,Female_1 "1"marriage, "0"for another
plt.figure(figsize=(9,6))
plt.pie(bf_gen_mar.iloc[:,2],radius=1,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','y'],labels=['Female_0','Female_1','Male_0','Male_1'],autopct='%1.1f%%',pctdistance = 0.9)
plt.pie(bf_gen.iloc[:,1],radius=0.7,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','yellow'],labels=['Female','Male'],labeldistance = 0.6,autopct='%1.1f%%',pctdistance = 0.4)
plt.tight_layout()
plt.legend()
plt.axis('equal')
plt.title('Gender & Marital_Status')
# plt.show()


# Gender count
user = bf.groupby(['User_ID','Gender'])
c_user = user.count().count(level='Gender')
g_user = c_user.count(level='Gender')
plt.figure()
plt.pie(g_user['Age'],labels=['F','M'])
# consume count
gender_sum_user = user.sum()
gender_sum_user = gender_sum_user.sum(level='Gender')
plt.figure()
plt.pie(gender_sum_user['Purches'],labels=['F','M'])


# Age
bf_age = bf.groupby(['Age']).count()
plt.bar(x=bf_age.index,y=bf_age.Purchase, height=100)

# Occupation
bf_Occ = bf.groupby(['Occupation']).count()
plt.barplot(x=bf_Occ.index,y=bf_Occ.Purchase)

# Stay Years
bf_Occ = bf.groupby(['Stay_In_Current_City_Years']).count()
plt.barplot(x=bf_Occ.index,y=bf_Occ.Purchase)

# City
bf_City = bf.groupby(['City_Category']).count()
plt.figure(figsize=(9,6))
plt.pie(bf_City.iloc[:,1],radius=0.7,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','yellow'],labels=['A','B','C'],labeldistance = 0.8,autopct='%1.1f%%',pctdistance = 0.7)
plt.tight_layout()
plt.legend()
plt.axis('equal')
plt.title('City')

# Population composition of each city
bf_C = bf.groupby(['City_Category','Age']).count().reset_index('Age')

fig=plt.figure(figsize=(14,8));
ax1=fig.add_subplot(1,3,1)
ax2=fig.add_subplot(1,3,2)
ax3=fig.add_subplot(1,3,3)
ax1.set_title('A')
ax2.set_title('B')
ax3.set_title('C')

ax1.pie(bf_C.iloc[0:7,2],radius=0.5,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','y','grey','olive','orange'],autopct='%1.1f%%',pctdistance = 0.7)
ax2.pie(bf_C.iloc[7:14,2],radius=0.5,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','y','grey','olive','orange'],autopct='%1.1f%%',pctdistance = 0.7)
ax3.pie(bf_C.iloc[14:23,2],radius=0.5,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','y','grey','olive','orange'],autopct='%1.1f%%',pctdistance = 0.7)

ax1.axis('equal')
ax2.axis('equal')
ax3.axis('equal')
ax3.legend(['0-17','18-25','26-35','36-45','46-50','51-55' ,'55+'],loc="best")

# Ring diagram
bf_C = bf.groupby(['City_Category','Age']).count().reset_index('Age')
fig=plt.figure(figsize=(14,8));
ax1=fig.add_subplot(1,3,1)
ax2=fig.add_subplot(1,3,2)
ax3=fig.add_subplot(1,3,3)
ax1.set_title('A')
ax2.set_title('B')
ax3.set_title('C')
ax1.pie(bf_C.iloc[0:7,2],radius=0.5,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','y','grey','olive','orange'],autopct='%1.1f%%',pctdistance = 0.7)
ax2.pie(bf_C.iloc[7:14,2],radius=0.5,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','y','grey','olive','orange'],autopct='%1.1f%%',pctdistance = 0.7)
ax3.pie(bf_C.iloc[14:23,2],radius=0.5,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','y','grey','olive','orange'],autopct='%1.1f%%',pctdistance = 0.7)
ax1.axis('equal')
ax2.axis('equal')
ax3.axis('equal')
ax3.legend(['0-17','18-25','26-35','36-45','46-50','51-55' ,'55+'],loc="best")


# user = pd.DataFrame(bf.groupby(['Gender']).get_group('M').groupby('User_ID'))
# print(user.shape[0])