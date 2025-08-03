import pandas
import numpy

import sklearn

from rdkit import Chem
from rdkit.Chem import rdmolops # for graph generation and operations/manipulations on molecules

smiles = 'CCO'  # Example SMILES string for ethanol
molecule = Chem.MolFromSmiles(smiles)

atoms = []
for atom in molecule.GetAtoms():
    atoms.append({
        'Atom Index': atom.GetIdx(),
        'Atomic Number': atom.GetAtomicNum(),
        'Periodic Table Symbol': atom.GetSymbol(),
        'Bonding Degree': atom.GetDegree(), # number of bonds to neighbours 
        'Formal Charge': atom.GetFormalCharge(), # Lewis structure formal charge
        'Hybridization': atom.GetHybridization().name, # valence bond hybridization state (sp, sp2, tetrahedral sp3, planar sp3, etc.)
        'Aromatic?': atom.GetIsAromatic(), # whether the atom is part of an aromatic ring
        ''
        ''
        ': 
    }
    )

