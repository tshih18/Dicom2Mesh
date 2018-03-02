import vtkInterface
import vtk

mesh = vtkInterface.PolyData("3D_Models_good/f_knee.stl")

mesh.Plot(color='orange', linethick=1e-7)
# mesh.Plot(color='orange', linethick=1e-7)