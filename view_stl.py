import vtkInterface
import vtk

mesh = vtkInterface.PolyData("lung.stl")

# mesh.Plot(color='white', linethick=1e-7, showedges=False)
mesh.Plot(color='white', linethick=1e-7)
