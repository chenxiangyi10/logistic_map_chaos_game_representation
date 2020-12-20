import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


pvalues = np.load(r'C:\Users\xxc90\Desktop\phm08-project\pvalues.npz')
poss0 = np.load(r'C:\Users\xxc90\Desktop\phm08-project\poss0.npz')
poss2 = np.load(r'C:\Users\xxc90\Desktop\phm08-project\poss2.npz')

bifurcation_mu = np.load(r"C:\Users\xxc90\Desktop\phm08-project\logistic_bifurcation_mu.npz")
bifurcation_x = np.load(r"C:\Users\xxc90\Desktop\phm08-project\logistic_bifurcation_x.npz")


# im_b = plt.scatter(bifurcation_mu, bifurcation_x, s = 0.5, color = "black", marker = "o", alpha = 0.01)

L0, d = poss0.shape
L,n,d = poss2.shape


fig = plt.figure(figsize=(9, 3.7))
ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax2.set_xlabel("$μ$")
ax2.set_ylabel("$x$")
#ax2.scatter(bifurcation_mu, bifurcation_x, s = 0.2, color = "blue", marker = "o", alpha = 0.01)
ax2.plot(bifurcation_mu, bifurcation_x, ls = "None", ms = 0.5, color = "blue", marker = "o", alpha = 0.01)

plt.tight_layout()
ims=[]
im1 = ax.scatter(poss0[:100000,0], poss0[:100000,1], s = 0.5, color = "blue", marker = "o", alpha = 0.005, label="Random number")
for i in range(L):
    print(i)
    ttl = plt.text(0.5, 1.01, "Logistic $μ=%f$"%pvalues[i], horizontalalignment='center', verticalalignment='bottom', transform=ax.transAxes)
    im_line = ax2.axvline(x = pvalues[i], color = 'black', label = 'axvline - full height')
    im = ax.scatter(poss2[i,:,0], poss2[i,:,1], s=0.5, color = "black", marker = "o", alpha = 0.05, label="Logistic \$μ=4\$")
    ims.append([im, ttl, im_line])
    #plt.cla()

print("done")

ani = animation.ArtistAnimation(fig, ims, interval=100, blit=False,
                              repeat_delay=500)
ani.save(r'C:\Users\xxc90\Desktop\phm08-project\dynamic_images.gif')                              
plt.show()
                              
print("done2")