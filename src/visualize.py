import matplotlib.pyplot as plt

from matplotlib.patches import Circle
from coordinates import project_to_sky

def plot_star_map(df, chart_size=10, max_star_size=50, zoom_factor=2):
    ra = df['ra']
    dec = df['dec']
    magnitude = df['phot_g_mean_mag']

    # normalize marker size based on magnitude
    x, y = project_to_sky(ra, dec)
    marker_size = max_star_size * 10 ** (magnitude /-2.5)

    # create black plot
    fig, ax = plt.subplots(figsize=(chart_size, chart_size))
    ax.set_facecolor('black')

    # draw sky border
    border = Circle((0, 0), 1, color='navy', fill=True)
    ax.add_patch(border)

    # plot stars
    ax.scatter(x, y, s=marker_size, color='white', marker='.', linewidths=0, zorder=2)

    # clip to horizon
    horizon = Circle((0,0), radius=1, transform=ax.transData)
    for col in ax.collections:
        col.set_clip_path(horizon)

    # adjust zoom level
    limit = 1 / zoom_factor
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)

    # display plot
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')
    plt.show()
