def mainchain():
    import re
    from chimera import openModels, Molecule

    mainChain = re.compile("^(N|CA|C)$", re.I)
    for m in openModels.list(modelTypes=[Molecule]):
        for a in m.atoms:
            a.display = mainChain.match(a.name) != None