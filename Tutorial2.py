
import chimera

opened = chimera.openModels.open('3fx2', type="PDB")
mol = opened[0]

mol.display = True

from chimera.colorTable import getColorByName
red = getColorByName('red')

mol.color = red

blue = getColorByName('blue')
yellow = getColorByName('yellow')

ATOMS = mol.atoms
for at in ATOMS:
	at.drawMode = chimera.Atom.Ball
	if at.name == 'CA':
		at.color = yellow
	else:
		at.color = blue

BONDS = mol.bonds
for b in BONDS:
	b.display = chimera.Bond.Smart
	b.drawMode = chimera.Bond.Stick
	b.halfbond = True

RESIDUES = mol.residues
for r in RESIDUES:
	if r.isHelix:
		r.ribbonDisplay = True
		r.ribbonDrawMode = chimera.Residue.Ribbon_Round

