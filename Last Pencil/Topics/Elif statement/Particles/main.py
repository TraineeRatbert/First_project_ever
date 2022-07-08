spin = input()
charge = input()
if spin == "1/2" and charge == "-1/3":
    print("Strange Quark")
elif spin == "1/2" and charge == "2/3":
    print("Charm Quark")
elif spin == "1/2" and charge == "-1":
    print("Electron Lepton")
elif spin == "1/2" and charge == "0":
    print("Neutrino Lepton")
else:
    print("Photon Boson")
