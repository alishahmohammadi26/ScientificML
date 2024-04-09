import crystals
from crystals import Crystal
import numpy as np
from pprint import pprint # pretty printing
import scipy 

cif_file = r"C:\Users\xpv9360\OneDrive - Takeda\Projects\AD\Molecular simulations\paracetamol.cif"
crystal = Crystal.from_cif(cif_file)

#Lattice vectors:A crystal lattice is an infinitely repeating 
# arrangement of unit cells in three dimensions.The vectors a, b, and c 
# are the primitive vectors of the lattice.The primitive vectors define
# the shape and orientation of the unit cell.
a1, a2, a3 = crystal.lattice_vectors

# The standard three lengths and angles description of a lattice is also accessible:
a, b, c, alpha, beta, gamma = crystal.lattice_parameters

#The unit cell volume (and by extensions, density) is also accessible:
vol = crystal.volume   # Angstroms cubed
density = vol/len(crystal)

crystal.lattice_system

pprint(crystal.symmetry())

# matrix symmetry operations
first_symop = crystal.symmetry_operations()[0]
print(first_symop)

########################################################################
from pyxtal import pyxtal
from pymatgen.io.cif import CifParser
from pymatgen.optimization import LBFGS

parser = CifParser(cif_file)
structure = parser.get_structures()[0]

# Perform geometry optimization (choose appropriate method)
# Example: Using the built-in optimization method
optimized_structure = pyxtal.optimize(crystal)

# Access optimized coordinates
optimized_coords = optimized_structure.frac_coords
print("Optimized fractional coordinates:")
print(optimized_coords)



###################################################################################
import pymatgen.core as pmg

from pymatgen.io.cif import CifParser
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer


# Parse the CIF file

cif_file_path = 'paracetamol.cif'

parser = CifParser(cif_file_path)

try:
    structure = parser.parse_structures()[0]
except Exception as e:
    print(f"Error: {e}")

# Print the single crystal structure
print("Single crystal structure:")
print(structure)



from pymatgen.core import Structure
struct = Structure.from_file(filename=cif_file_path)
print(struct)


from pymatgen.io.vasp.inputs import Poscar
poscar = Poscar(structure = struct, comment="paracetamol")
print(poscar)

poscar = Poscar(struct)
poscar_file = "POSCAR"
poscar.write_file(poscar_file)

from pymatgen.io.vasp.sets import MPRelaxSet
relax_set = MPRelaxSet(structure=struct)
relax_set.incar
relax_set.poscar
relax_set.kpoints



from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.io.vasp.sets import MPRelaxSet

from atomate.vasp.drones import VaspDrone
from atomate.vasp.workflows.presets.core import wf_structure_optimization
from atomate.vasp.workflows.presets.core import wf_bandstructure
from atomate.vasp.powerups import add_modify_incar

structure = Poscar.from_file(poscar_file).structure

input_set = MPRelaxSet(structure)


# Create the band structure workflow
wf = wf_bandstructure(structure)

so_wf = wf_structure_optimization(structure=struct)


print(so_wf)


# Optimize single crystal structure:

from pyxtal import pyxtal
from pyxtal.symmetry import Group

# Define the space group (you can find this in your CIF file)
space_group_number = 191  # Example: P6/mmm

# Create a PyXtal structure
crystal = pyxtal.from_random(structure, space_group_number)

# Access the generated structure
print(crystal)


# Visualize the crystal
import nglview as nv

# Assuming 'structure_to_show' is your pymatgen structure object
view = nv.show_pymatgen(structure)
view.add_unitcell() 
view 
# Optional: Display the unit cell
