import pandas as pd
import matplotlib.pyplot as plt, matplotlib.image as mpimg
from sklearn.model_selection import train_test_split
from sklearn import svm

blackFriday = pd.read_csv('BlackFriday.csv')
#1
a1 = blackFriday.groupby(['Product_ID'],as_index=False).agg({'Purchase':sum})
a1.sort_values(['Purchase'], ascending=False, inplace=True)
print(len(a1))
#2
a2 = blackFriday[['Product_Category_1','Purchase']].groupby(['Product_Category_1'],as_index=False).agg({'Purchase':sum})
a2.sort_values(['Purchase'], ascending=False, inplace=True)
a2.head(10)
#3
a3 = blackFriday[['Gender','Purchase']].groupby(['Gender'],as_index=False).agg({'Purchase':sum})
a3.sort_values(['Purchase'],ascending=False,inplace=True)
a3.head(10)
woman = blackFriday[['Gender','Product_ID','Purchase']].groupby('Gender').get_group('F').groupby('Product_ID').agg({'Purchase':sum})
woman.sort_values(['Purchase'],ascending=False,inplace=True)

man = blackFriday[['Gender','Product_ID','Purchase']].groupby('Gender').get_group('M')
man2 = man.groupby('Product_ID').agg({'Purchase':sum})
man2.sort_values(['Purchase'],ascending=False,inplace=True)


#4
a4 = blackFriday[['Age','Purchase']].groupby(['Age'],as_index=False).agg({'Purchase':sum})
a4.sort_values(['Purchase'],ascending=False,inplace=True)
a0_17 = blackFriday.groupby('Age').get_group('0-17').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
a18_25 = blackFriday.groupby('Age').get_group('18-25').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
a26_35 = blackFriday.groupby('Age').get_group('26-35').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
a36_45 = blackFriday.groupby('Age').get_group('36-45').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
a46_50 = blackFriday.groupby('Age').get_group('46-50').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
a51_55 = blackFriday.groupby('Age').get_group('51-55').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
a55Up = blackFriday.groupby('Age').get_group('55+').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)


#5
a5 = blackFriday[['Occupation','Purchase']].groupby(['Occupation'],as_index=False).agg({'Purchase':sum})
a5.sort_values(['Purchase'],ascending=False,inplace=True)
o0 = blackFriday.groupby('Occupation').get_group(0).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o1 = blackFriday.groupby('Occupation').get_group(1).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o2 = blackFriday.groupby('Occupation').get_group(2).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o3 = blackFriday.groupby('Occupation').get_group(3).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o4 = blackFriday.groupby('Occupation').get_group(4).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o5 = blackFriday.groupby('Occupation').get_group(5).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o6 = blackFriday.groupby('Occupation').get_group(6).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o7 = blackFriday.groupby('Occupation').get_group(7).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o8 = blackFriday.groupby('Occupation').get_group(8).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o9 = blackFriday.groupby('Occupation').get_group(9).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o10 = blackFriday.groupby('Occupation').get_group(10).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o11 = blackFriday.groupby('Occupation').get_group(11).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o12 = blackFriday.groupby('Occupation').get_group(12).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o13 = blackFriday.groupby('Occupation').get_group(13).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o14 = blackFriday.groupby('Occupation').get_group(14).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o15 = blackFriday.groupby('Occupation').get_group(15).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o16 = blackFriday.groupby('Occupation').get_group(16).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o17 = blackFriday.groupby('Occupation').get_group(17).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o18 = blackFriday.groupby('Occupation').get_group(18).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o19 = blackFriday.groupby('Occupation').get_group(19).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
o20 = blackFriday.groupby('Occupation').get_group(20).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)


#6
a6 = blackFriday[['City_Category','Purchase']].groupby(['City_Category'],as_index=False).agg({'Purchase':sum})
a6.sort_values(['Purchase'],ascending=False,inplace=True)
A = blackFriday.groupby('City_Category').get_group('A').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
B = blackFriday.groupby('City_Category').get_group('B').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
C = blackFriday.groupby('City_Category').get_group('C').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)


#7
a7 = blackFriday[['Stay_In_Current_City_Years','Purchase']].groupby(['Stay_In_Current_City_Years'],as_index=False).agg({'Purchase':sum})
a7.sort_values(['Purchase'],ascending=False,inplace=True)
s0 = blackFriday.groupby('Stay_In_Current_City_Years').get_group('0').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
s1 = blackFriday.groupby('Stay_In_Current_City_Years').get_group('1').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
s2 = blackFriday.groupby('Stay_In_Current_City_Years').get_group('2').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
s3 = blackFriday.groupby('Stay_In_Current_City_Years').get_group('3').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
s4Up = blackFriday.groupby('Stay_In_Current_City_Years').get_group('4+').groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)


#8
a8 = blackFriday[['Marital_Status','Purchase']].groupby(['Marital_Status'],as_index=False).agg({'Purchase':sum})
a8.sort_values(['Purchase'],ascending=False,inplace=True)
m0 = blackFriday.groupby('Marital_Status').get_group(0).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)
m1 = blackFriday.groupby('Marital_Status').get_group(1).groupby('Product_ID').agg({'Purchase':sum}).sort_values("Purchase",inplace=False, ascending=False)

#已婚男女购买对比
a9 = blackFriday.groupby('Marital_Status').get_group(1).groupby('Gender').get_group('M').groupby('Product_ID').agg({'Purchase':sum})
a9.sort_values(['Purchase'],ascending=False,inplace=True)

a9 = blackFriday.groupby('Marital_Status').get_group(1).groupby('Gender').get_group('F').groupby('Product_ID').agg({'Purchase':sum})
a9.sort_values(['Purchase'],ascending=False,inplace=True)

#print(a9.head(10))
#a8.sort_values(['Purchase'],ascending=False,inplace=True)
a10 = blackFriday.groupby('City_Category').get_group('C').groupby('Stay_In_Current_City_Years').agg({'Purchase':sum})
print(a10)
