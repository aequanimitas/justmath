import matplotlib.pyplot as plt

fig = plt.figure(2)
fig.clf()
ax = fig.add_subplot(111, autoscale_on=True, xlim=(-2, 2), ylim=(-2, 2))
# args
arrow_kwargs = {
    "head_width": 0.05,
    "head_length": 0.1,
    "fc":'k',
    "ec": 'k'
}

# plot parallelogram rule
ax.arrow(0, 0, 1, 1, **arrow_kwargs)
ax.arrow(0, 0, 0.5, 0.7, **arrow_kwargs)
ax.arrow(0, 0, 0.5, 0.3, **arrow_kwargs)

# adjacent should be dashed
adj_kwargs = arrow_kwargs
adj_kwargs["linestyle"] = "dotted"

ax.arrow(0.5, 0.3, 0.5, 0.7, **adj_kwargs)
ax.arrow(0.5, 0.7, 0.5, 0.3, **adj_kwargs)
plt.show()
