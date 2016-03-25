import matplotlib.pyplot as plt

fig = plt.figure("Parallelogram Rule")
fig.clf()
# args
fig_kwargs = {
    "autoscale_on": True, 
    "xlim": (-2, 2), 
    "ylim": (-2, 2)
}

arrow_kwargs = {
    "head_width": 0.05,
    "head_length": 0.1,
    "fc": "#00BFFF",
    "ec": "#00BFFF"
}

# plot parallelogram rule
ax = fig.add_subplot(111, **fig_kwargs)

ax1 = arrow_kwargs.copy()
ax1["label"] = "v + w"
ax.arrow(0, 0, 1, 1, **ax1)
ax.arrow(0, 0, 0.5, 0.7, **arrow_kwargs)
ax.arrow(0, 0, 0.5, 0.3, **arrow_kwargs)

# adjacent should be dashed
adj_kwargs = arrow_kwargs.copy()
adj_kwargs["linestyle"] = "dotted"

ax.arrow(0.5, 0.3, 0.5, 0.7, **adj_kwargs)
ax.arrow(0.5, 0.7, 0.5, 0.3, **adj_kwargs)

fig2 = plt.figure("Triangle Rule")
ay = fig2.add_subplot(111, **fig_kwargs)
ay.arrow(0, 0, 0.5, 0.7, **arrow_kwargs)
ay.arrow(0.5, 0.7, 0.5, 0.3, **arrow_kwargs)
ay.arrow(0, 0, 1, 1, **arrow_kwargs)

fig3 = plt.figure("Vector Subtraction")
az = fig3.add_subplot(111, **fig_kwargs)
az.arrow(0, 0, 0.5, 0.7, **arrow_kwargs)
az.arrow(0, 0, -0.5, -0.7, **arrow_kwargs)

plt.show()
