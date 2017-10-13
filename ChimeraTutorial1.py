import chimera

opened = chimera.openModels.open('/4fun.pdb')

mol = opened[0]

f = open("4fun.mol2", 'w')

MOLECULE_HEADER = "@MOLECULE"
ATOM_HEADER = "@ATOM"
BOND_HEADER = "@BOND"
SUBSTR_HEADER = "@SUBSTRUCTURE"

chimera2sybyl = {

'C3' : 'C.3', 'C2' : 'C.2', 'Car' : 'C.ar', 'Cac' : 'C.2',
'C1' : 'C.1', 'N3+' : 'N.4', 'N3' : 'N.3', 'N2' : 'N.2',
'Npl' : 'N.pl3', 'Ng+' : 'N.pl3', 'Ntr' : 'N.2', 'Nox' : 'N.4',
'N1+' : 'N.1', 'N1' : 'N.1', 'O3' : 'O.3', 'O2' : 'O.2',
'Oar' : 'O.2', 'O3-' : 'O.co2', 'O2-' : 'O.co2', 'S3+' : 'S.3',
'S3' : 'S.3', 'S2' : 'S.2', 'Sac' : 'S.O2', 'Son' : 'S.O2',
'Sxd' : 'S.O', 'Pac' : 'P.3', 'Pox' : 'P.3', 'P3+' : 'P.3',
'HC' : 'H', 'H' : 'H', 'DC' : 'H', 'D' : 'H',
'P' : 'P.3', 'S' : 'S.3', 'Sar' : 'S.2', 'N2+' : 'N.2'
}

f.write("%s\n" % MOLECULE_HEADER)
f.write("%s\n" % mol.name)
ATOM_LIST = mol.atoms
BOND_LIST = mol.bonds
RES_LIST = mol.residues

f.write("%d %d %d\n" % ( len(ATOM_LIST), len(BOND_LIST), len(RES_LIST)) )
f.write("PROTEIN\n")
f.write("NO_CHARGES\n")
f.write("\n\n")
