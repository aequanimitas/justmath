import matplotlib.pyplot as plt

fig = plt.figure(2)
fig.clf()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-5, 5), ylim=(-5, 5))

# plot parallelogram rule
ax.arrow(0, 0, 1, 1, head_width=0.05, head_length=0.1, fc='k', ec='k')
ax.arrow(0, 0, 0.5, 0.7, head_width=0.05, head_length=0.1, fc='k', ec='k')
ax.arrow(0, 0, 0.5, 0.3, head_width=0.05, head_length=0.1, fc='k', ec='k')
ax.arrow(0, 0, 0.5, 0.3, head_width=0.05, head_length=0.1, fc='k', ec='k')

ax.arrow(0.5, 0.3, 0.5, 0.7, head_width=0.05, head_length=0.1, fc='k', ec='k', linestyle="dashed")
ax.arrow(0.5, 0.7, 0.5, 0.3, head_width=0.05, head_length=0.1, fc='k', ec='k', linestyle="dashed")
plt.show()
