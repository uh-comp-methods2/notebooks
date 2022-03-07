import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg as la

def plot_vec(v, *args, o=np.zeros(3)):
    '''Plot vector v with the base point at o'''
    w = v + o
    plt.gca().plot([w[0], o[0]], [w[1], o[1]], [w[2], o[2]], *args)

def plot_plane(v, w):
    ''''Plot a piece of the plane spanned by v and w'''
    v1 = v / la.norm(v)
    v2 = w - np.dot(w,v1) * v1
    v2 = v2 / la.norm(v2)
    ts = la.norm(v) * np.linspace(-0.2, 1.2)
    rs = la.norm(w) * np.linspace(-1.2, 1.2)
    [Ts, Rs] = np.meshgrid(ts, rs)
    Xs = v1[0] * Ts + v2[0] * Rs
    Ys = v1[1] * Ts + v2[1] * Rs
    Zs = v1[2] * Ts + v2[2] * Rs
    plt.gca().plot_surface(Xs, Ys, Zs, alpha=0.1)

def plot_coeffs(x, a0, a1, *args):
    '''Visualize coefficients x in the basis a0, a1'''
    plot_vec(x[0]*a0, *args)
    plot_vec(x[1]*a1, *args)
    plot_vec(x[0]*a0, *args, o=x[1]*a1)
    plot_vec(x[1]*a1, *args, o=x[0]*a0)

def set_equal_aspect():
    '''Set equal aspect ratio in all dimensions'''
    ax3d = plt.gca()
    wl = ax3d.get_w_lims()
    ax3d.set_box_aspect((wl[1]-wl[0],wl[3]-wl[2],wl[5]-wl[4]))  
    
def hide_ticks():
    '''Prettify plot by hiding the ticks in all axes'''
    ax3d = plt.gca()
    ax3d.set_xticks([])
    ax3d.set_yticks([])
    ax3d.set_zticks([])
