import vtkInterface
import vtk

mesh = vtkInterface.PolyData("f_hip_full_smooth.stl")

mesh.Plot(color='orange', linethick=1e-7)