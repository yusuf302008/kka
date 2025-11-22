import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

data = pd.read_csv('nilai_siswa.csv')
print(data.info())
print(data.head())
print(data.describe)

print("Rata Rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median)
print("Modus:", data['Nilai'].mode()[0])

# Matematika = data[data['matpel'] =='Matematika']
# print [Matematika]

# Inggris = data[data['matpel'] =='Bahasa inggris']
# print [Inggris]

# Indonesia = data[data['matpel'] =='Bahasa indonesia']
# print [Bahasa indonesia]