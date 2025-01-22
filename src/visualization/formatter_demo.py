import matplotlib.pyplot as plt
import numpy as np

data = {
    "x_vals": np.linspace(0, 10, 100),
    "y_vals": np.sin(np.linspace(0, 10, 100)),
    "label": "Sine Wave",
    "title": "Sine Wave Example",
    "xlabel": "X-axis",
    "ylabel": "Y-axis",
    "legend_loc": "upper right",
}
x = data["x_vals"]
y = data["y_vals"]
plt.plot(x, y, label=data["label"])
plt.title(data["title"])
plt.xlabel(data["xlabel"])
plt.ylabel(data["ylabel"])
plt.legend(loc=data["legend_loc"])
plt.show()
