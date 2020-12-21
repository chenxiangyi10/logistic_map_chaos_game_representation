import numpy as np
import matplotlib.pyplot as plt


pvalues = np.load(r'C:\Users\xxc90\Desktop\phm08-project\pvalues.npz')
poss0 = np.load(r'C:\Users\xxc90\Desktop\phm08-project\poss0.npz')
poss2 = np.load(r'C:\Users\xxc90\Desktop\phm08-project\poss2.npz')
poss2_normalized = np.load(r'C:\Users\xxc90\Desktop\phm08-project\poss2_normalized.npz')

bifurcation_mu = np.load(r"C:\Users\xxc90\Desktop\phm08-project\logistic_bifurcation_mu.npz")
bifurcation_x = np.load(r"C:\Users\xxc90\Desktop\phm08-project\logistic_bifurcation_x.npz")


L0, d = poss0.shape
L,n,d = poss2.shape

print(poss2.shape)

fig = plt.figure(figsize=(9.5, 5.6))
ax = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)
ax6 = fig.add_subplot(236)
axs = [ax, ax2, ax3, ax4, ax5, ax6]

mu = [2.6, 3.4, 3.5, 3.8, 3.9, 4.0]
cycle = ["1 cycle", "2 cycles", "4 cycles", "chaos", "chaos", "chaos"]
index = []
for value in mu:
    index.append(list(pvalues).index(value))
print(index)
for i in range(6):
    axs[i].scatter(poss0[:50000,0], poss0[:50000,1], s = 0.5, color = "blue", marker = "o", alpha = 0.002)
    axs[i].set_xlabel("$x$")
    axs[i].set_ylabel("$y$")
    axs[i].scatter(poss2_normalized[index[i],:,0], poss2_normalized[index[i],:,1], s=0.5, color = "black", marker = "o", alpha = 0.05, label="$μ=%.2f$"%mu[i])
    axs[i].set_title("$μ=%.2f$, regime = %s"%(mu[i],cycle[i]))
    #axs[i].legend(frameon=False, loc = 1)
plt.tight_layout()
print("done")
plt.savefig(r'C:\Users\xxc90\Desktop\phm08-project\CGR_logistic_map.png', dpi = 300 )                              
plt.show()