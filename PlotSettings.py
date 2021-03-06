#List of implemented fields.
proj_fields = "SurfaceDensity", "SigmaV", "KineticEnergy", "Q", "SFDensity", "MagEnergySurfaceDensity"
slice_fields = "Density", "NumberDensity", "Temperature", "MagEnergyDensity", "JeansMass", "B_z", "B_x", "B_y", "B"

# Fields to actually plot
fields_toplot = {0: ["SurfaceDensity","Temperature"],
                 1: [],
                 2: ["SurfaceDensity"],
                 3: ["SurfaceDensity"],
                 4: ["SurfaceDensity"],
                 5: ["SurfaceDensity"]
                 }

# Colormap limits for each field
field_limits = {"SurfaceDensity": [1, 1e4],
                "B_z": [1e-5, 1e-2],
                "B_x": [1e-5, 1e-2],
                "B_y":[1e-5, 1e-2],
                "B": [1e-5, 10],
                "Temperature": [10, 1e7],
                "SigmaV": [1e-1, 1e4],
                "Density":[1e2,1e8],
                "NumberDensity":[1, 1e5],
                "KineticEnergy": [1e40, 1e60],
                "Q": [1e-1,1e3],
                "SFDensity" : [1e-8, 10],
                "MagEnergySurfaceDensity": [1e46, 1e60],
                "JeansMass": [1e-6, 1e3]}

#Plot labels for fields. Can contain TeX syntax
field_labels = {"SurfaceDensity": "$\\Sigma$ $(\mathrm{M_\odot}/\mathrm{pc}^2)$",
                "SigmaV": "$\\sigma_{zz}$ $(\mathrm{km/s})$",
                "KineticEnergy": "$\\frac{\mathrm{d}T}{\mathrm{d}A}$ $(\mathrm{erg} \, \mathrm{pc}^{-2})$",
                "NumberDensity": "$n$ $(\mathrm{cm}^{-3})$",
                "Density": "$\\rho$ $(\mathrm{g} \mathrm{cm}^{-3})$",
                "Temperature": "$T$ $(\mathrm{K})$",
                "Q": "$\\mathcal{Q}$",
                "SFDensity": "$\dot{\Sigma}_\star$ $(\\mathrm{M_\odot} \mathrm{yr}^{-1} \mathrm{pc}^{-2})$",
                "MagEnergySurfaceDensity": "$\\Sigma_{B}$ $(\mathrm{erg} \,\mathrm{pc}^{-2})$",
                "JeansMass": "$M_J$ $(M_\\odot)$",
                "B_z": "$B_z$ $(G)$",
                "B_x": "$B_x$ $(G)$",
                "B_y": "$B_y$ $(G)$",
                "B": "$B$ $(G)$"
                                  }
