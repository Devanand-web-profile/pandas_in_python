# pandas
import pandas as pd
import matplotlib.pyplot as plt


x=[["ranjan",56],["mohan",20],["monkey",89],["hourse",20]]
data=pd.DataFrame(x,columns=["name","age"])
print(data)

print("---------------")

print(data[0:3])
print("---------------")
print(data[2:])
print("---------------")
print(data.head())
print("---------------")
print(data.head(2))
print("---------------")
print(data.tail())
print("---------------")
print(data.tail(3))


name=data["name"]
print(name)
age=data["age"]
print(age)
plt.plot(name,age,color="green")
plt.grid(True,color="red")
plt.title("student data")
plt.xlable("name")
plt.ylabel("age")
plt.scatter(name,age,color="magenta")
plt.show()











