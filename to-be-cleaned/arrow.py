import matplotlib.pyplot as plt


plt.axes().set_aspect("equal", adjustable="box")
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.arrow(0, 0, 3, 4, head_width=0.05, head_length=0.1, fc="k", ec="k")
plt.arrow(0, 0, -4, 3, head_width=0.05, head_length=0.1, fc="k", ec="k")

plt.show()
