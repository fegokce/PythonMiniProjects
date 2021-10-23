import matplotlib.pyplot as plt

students = ["Koray Can", "Sena", "Zeynep", "Ebrar", "Ayşenur", "Müslüm", "Melih"]
gano = [2.71, 3.02, 2.67, 2.54, 2.78, 2.56, 2.70]
marketing_course = [3.05, 2.75, 3.00, 2.86, 2.89, 2.69, 3.10]

# plt.plot(students, gano, color="red", linewidth=2, linestyle="--", marker="o", markersize=13, markerfacecolor="yellow", markeredgewidth=2, markeredgecolor="blue")
# plt.xlabel("Öğrenci İsimleri")
# plt.ylabel("Ortalama Puanları")
# plt.title("Öğrencilerin Genel Ağırlık Not Ortalaması")

# f = plt.figure(figsize=(15,7))
# axes1 = f.add_axes([0.1,0.1,0.8,0.8])
# axes2 = f.add_axes([0.5,0.5,0.3,0.3])
# axes1.plot(students, gano, color="red", linewidth=2, linestyle="--", marker="o", markersize=13, markerfacecolor="red", markeredgewidth=2, markeredgecolor="black", label="genel ağırlık not ortalaması")
# axes1.set_xlabel("Öğrenci İsimleri")
# axes1.set_ylabel("Ortalama Puanları")
# axes1.set_title("Öğrencilerin Genel Ağırlık Not Ortalaması")
# axes1.set_ylim([2,4])
# axes1.set_xlim([-1,7])
# axes2.plot(students, marketing_course, color="blue", linewidth=2, linestyle="--", marker="o", markersize=13, markerfacecolor="blue", markeredgewidth=2, markeredgecolor="black", label="pazarlama dersi not ortalaması")
# axes2.set_xlabel("Öğrenci İsimleri")
# axes2.set_ylabel("Ortalama Puanları")
# axes2.set_title("Öğrencilerin Pazarlama Dersi Not Ortalaması")
# axes2.set_ylim([2,4])
# axes2.set_xlim([-1,7])

f = plt.figure(figsize=(15,7))
axes = f.add_axes([0.1,0.1,0.8,0.8])
axes.plot(students, gano, color="red", linewidth=2, linestyle="--", marker="o", markersize=13, markerfacecolor="red", markeredgewidth=2, markeredgecolor="black", label="genel ağırlık not ortalaması")
axes.plot(students, marketing_course, color="blue", linewidth=2, linestyle="--", marker="o", markersize=13, markerfacecolor="blue", markeredgewidth=2, markeredgecolor="black", label="pazarlama dersi not ortalaması")
axes.set_xlabel("Öğrenci İsimleri")
axes.set_ylabel("Ortalama Puanları")
axes.set_ylim([2,4])
axes.set_xlim([-1,7])
axes.legend(loc=0)

plt.tight_layout()
plt.show()