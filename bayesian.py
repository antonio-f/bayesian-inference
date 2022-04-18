import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


# configure style
# mpl.rc('text', usetex=True)
# mpl.rc('font', size=26)
sns.set_style("darkgrid")
sns.set(rc={'text.color': 'gray', 
    'axes.edgecolor': '#202020', 
    'axes.facecolor':'#181818', 
    'figure.facecolor':'#181818', 
    "grid.color": "#252525", 
    "grid.linestyle": ":",
    'xtick.color': 'gray',
    'ytick.color': 'gray',
    # 'font.family': ['Nimbus Sans']
    })
sns.set_context("talk", rc={"figure.figsize": (12, 8)}, font_scale=0.6)
current_palette = sns.color_palette()

def plot_prior(alpha, beta, ax=None):
    x = np.linspace(0, 1, 1000)
    y = scipy.stats.beta.pdf(x, alpha, beta)

    if not ax:
        fig, ax = plt.subplots()
    ax.plot(x, y, '#fac038')
    ax.set_xlabel(r"$\theta$", fontsize=12, color='gray')
    ax.set_ylabel(r"$\mathrm{P}(\theta)$", fontsize=12, color='gray')
    ax.set_title("Prior: Beta({},{})".format(alpha,beta));
    
plot_prior(alpha=2, beta=2)

def plot_posterior(heads, tails, alpha, beta, ax=None):
    x = np.linspace(0, 1, 1000)
    y = scipy.stats.beta.pdf(x, heads+alpha, tails+beta)
        
    if not ax:
        fig, ax = plt.subplots()
    ax.plot(x, y, '#fac038')
    ax.set_xlabel(r"$\theta$", fontsize=12, color='gray')
    ax.set_ylabel(r"$\mathrm{P}(\theta \mid D)$", fontsize=12, color='gray')
    ax.set_title("Posterior after {} heads, {} tails, \
                 Prior: Beta({},{})".format(heads, tails, alpha, beta))

plot_posterior(heads=50, tails=25, alpha=2, beta=2)


fig, axes = plt.subplots(4)
flips = [(3, 7), (18, 22), (73, 77), (4005, 3995)]
for i, flip in enumerate(flips):
    plot_posterior(heads=flip[0], tails=flip[1], alpha=2, beta=2, ax=axes[i])
    axes[i].set_yticks([])
fig.subplots_adjust(hspace=.6)
for j, ax in enumerate(axes):
    # ax.set_yticks([])
    # ax.set_xticks([])
    ax.set_xlabel("")
    axes[j].set_xticks([0.5]);

plt.show()







