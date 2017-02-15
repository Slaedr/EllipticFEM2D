""" @brief Assembly routines of local and global FE matrices.
"""

import numpy as np
from numba import jit, generated_jit
from mesh import *
from quadrature import GLQuadrature1D, GLQuadrature2DTriangle

class Element:
    """ @brief Abstract class for a finite element.
    Members are
    nnodel: number of nodes in the element
    phynodes: locations of physical nodes
    refnodes: locations of reference nodes
    """
    def __init__(self):
        pass
    def setPhysicalElementNodes(self, physical_nodes, num_dofs):
        """ physical_nodes is a nnodel x ndim numpy array describing locations of the physical nodes."""
        self.phynodes = np.copy(pysical_nodes)
        self.ndofs = num_dofs
    def setReferenceElementNodes(self):
        pass
    def getJacobianDet(self, x, y):
        pass
    def getBasisFunction(self, idof, x, y):
        pass

class P1TriangleElement(Element):
    def setReferenceElementNodes(self):
        self.refnodes = np.zeros(phy_nodes)
        self.nnodel = phy_nodes.shape[0]
        if self.nnodel == 3:
            refnodes[0,:] = [0.0,0.0]
            refnodes[1,:] = [1.0,0.0]
            refnodes[2,:] = [0.0,1.0]
        else:
            print("! P1TriangleElement: Element with " + str(self.nnodel) + " nodes not available!")

    def getJacobianDet(self, x, y):
        pass

class P2TriangleElement(Element):
    def setReferenceElementNodes(self):
        self.refnodes = np.zeros(phy_nodes)
        self.nnodel = phy_nodes.shape[0]
        if self.nnodel == 6:
            refnodes[3,:] = (refnodes[0,:]+refnodes[1,:])*0.5
            refnodes[4,:] = (refnodes[1,:]+refnodes[2,:])*0.5
            refnodes[5,:] = (refnodes[2,:]+refnodes[0,:])*0.5
        else:
            print("! P2TriangleElement: Element with " + str(self.nnodel) + " nodes not available!")
    
    def getJacobianDet(self, x, y):
        pass

class LagrangeP1TriangleElement(P1TriangleElement):
    """ Triangular element with Lagrange P1 basis for the trial and test spaces.
    """
    def getBasisFunction(self, idof, x, y):
        pass

class LagrangeP1TriangleElement(P2TriangleElement):
    """ Triangular element with Lagrange P2 basis for the trial and test spaces.
    """
    def getBasisFunction(self, idof, x, y):
        pass


@jit(nopython=True, cache=True)
def coeff_mass(x, y):
    return x + 2.0*y

@jit(nopython=True, cache=True)
def coeff_stiffness(x, y):
    return x*x + y*y - x*y

@jit(nopython=True, cache=True)
def localMassMatrix(m, ielem, localmass):
    """ Computes the local mass matrix of element ielem in mesh m.
    The output array localmass needs to be pre-allocated."""
    pass

@jit(nopython=True, cache=True)
def localStiffnessMatrix(m, ielem, localstif):
    """ Computes the local stiffness matrix of element ielem in mesh m.
    The output array localmass needs to be pre-allocated."""
    pass

def localLoadVector_domain(m, ielem, localload):
    """ Computes the domain integral part of the local load vector.
    localload must be pre-allocated.
    """
    pass

def localLoadVector_boundary(m, iface, localload):
    """ Computes the local boundary integral part of load vector for Neumann BCs.
    localload must be allocated before passing to this.
    """
    pass
