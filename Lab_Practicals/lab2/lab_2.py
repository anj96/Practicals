import numpy as np
import matplotlib.pyplot as plt
import csv
with open('grades.csv', 'r') as f:
        reader = csv.reader(f,delimiter=',' )
        grades=[]
        for row in reader:
            grades.append(int(row[0]))

#Histogram
plt.hist(grades, bins=[65,70, 75, 80, 85, 90, 95, 100])
plt.title('Histogram')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.savefig('histogram.png')
plt.show()

#Pie-Chart
poor = 0
avg=0
good = 0

for grade in grades:
  if grade < 70:
    poor += 1
  elif grade>70 and grade<80:
      avg+=1
  else:
  	good += 1

plt.pie([good,avg ,poor], labels=["Good","Average","Poor"],explode = (0,0.10,0), shadow = True)
plt.title('Class Performance.')
plt.savefig('pie.png')
plt.show()

#Scatter Plot
marks=[int(i) for i in range(100)]
plt.scatter(grades,marks)
plt.ylabel('Range of Marks')
plt.xlabel('Marks Obtained')
plt.title('Scatter Plot- Marks')
plt.savefig('scatter.png')
plt.show()

#Bar Chart
vals=[np.amax(grades),np.amin(grades),np.mean(grades),np.std(grades)]
x=[1,2,3,4]
name=['   Max','    Min','    Mean','      Std-Dev']
plt.bar(x,vals)
plt.xticks(x,name)
plt.title('Bar Chart of Class Performance')
plt.savefig('bar.png')
plt.show()