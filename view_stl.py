import vtkInterface
import vtk

mesh = vtkInterface.PolyData("3D_Models_good/f_fullbody.stl")

#mesh.Plot(color='orange', linethick=1e-7, showedges=False)
mesh.Plot(color='white', linethick=1e-7)