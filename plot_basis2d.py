import numpy as np
from matplotlib import pyplot as plt
import skfem as fem
from plot_vec3d import set_equal_aspect, hide_ticks

eps = np.finfo(float).eps

def plot_cross_sec(u, ps, basis):
    '''Plot cross section of u over the line segment with end points given by ps
        This works only on the mesh given by init_refdom()
    '''
    mesh = basis.mesh 
    ts = np.linspace(0, 1)
    xs = (1 - ts)*ps[0, 0] + ts*ps[0, 1]
    ys = (1 - ts)*ps[1, 0] + ts*ps[1, 1]
    # Due to rounding errors, the points given by xs and ys might not quite be in the element domain
    # To remedy this, move them slightly closer to the midpoint
    midpoint = np.sum(mesh.p, axis=1) / 3
    s = 10*eps
    xs = (1-s)*xs + s*midpoint[0]
    ys = (1-s)*ys + s*midpoint[0]
    probe = basis.probes(np.stack((xs, ys)))
    zs = probe @ u
    ax3d = plt.gca()
    ax3d.plot(xs, ys, np.zeros_like(xs), 'k--')
    ax3d.plot(xs, ys, zs, 'k')

def plot_facet_vals(u, basis):
    '''Plot cross sections of u over each facet
        This works only on the mesh given by init_refdom()
    '''
    for facet in basis.mesh.facets.T:
        plot_cross_sec(u, basis.mesh.p[:, facet], basis)

def plot_nodal_vals(u, basis):
    '''Plot point values of u at each node
        This works only on the mesh given by init_refdom()
    '''
    mesh = basis.mesh
    probe = basis.probes(mesh.p)
    zs = probe @ u
    xs, ys = mesh.p
    ax3d = plt.gca()
    ax3d.plot(xs, ys, zs, 'ko')
    for i in range(len(xs)):
        x, y, z = xs[i], ys[i], zs[i]
        ax3d.plot([x, x], [y, y], [0, z], 'k:')

