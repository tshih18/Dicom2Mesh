# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.10.2/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.10.2/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/aether/Downloads/DicomToMesh-master

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/aether/Downloads/DicomToMesh-master/build

# Include any dependencies generated for this target.
include lib/CMakeFiles/dicom2meshlib.dir/depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/dicom2meshlib.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/dicom2meshlib.dir/flags.make

lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o: lib/CMakeFiles/dicom2meshlib.dir/flags.make
lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o: ../lib/src/vtkDicomRoutines.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/aether/Downloads/DicomToMesh-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o"
	cd /Users/aether/Downloads/DicomToMesh-master/build/lib && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o -c /Users/aether/Downloads/DicomToMesh-master/lib/src/vtkDicomRoutines.cpp

lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.i"
	cd /Users/aether/Downloads/DicomToMesh-master/build/lib && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/aether/Downloads/DicomToMesh-master/lib/src/vtkDicomRoutines.cpp > CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.i

lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.s"
	cd /Users/aether/Downloads/DicomToMesh-master/build/lib && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/aether/Downloads/DicomToMesh-master/lib/src/vtkDicomRoutines.cpp -o CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.s

lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o.requires:

.PHONY : lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o.requires

lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o.provides: lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o.requires
	$(MAKE) -f lib/CMakeFiles/dicom2meshlib.dir/build.make lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o.provides.build
.PHONY : lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o.provides

lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o.provides.build: lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o


lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o: lib/CMakeFiles/dicom2meshlib.dir/flags.make
lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o: ../lib/src/vtkMeshRoutines.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/aether/Downloads/DicomToMesh-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o"
	cd /Users/aether/Downloads/DicomToMesh-master/build/lib && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o -c /Users/aether/Downloads/DicomToMesh-master/lib/src/vtkMeshRoutines.cpp

lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.i"
	cd /Users/aether/Downloads/DicomToMesh-master/build/lib && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/aether/Downloads/DicomToMesh-master/lib/src/vtkMeshRoutines.cpp > CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.i

lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.s"
	cd /Users/aether/Downloads/DicomToMesh-master/build/lib && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/aether/Downloads/DicomToMesh-master/lib/src/vtkMeshRoutines.cpp -o CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.s

lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o.requires:

.PHONY : lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o.requires

lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o.provides: lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o.requires
	$(MAKE) -f lib/CMakeFiles/dicom2meshlib.dir/build.make lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o.provides.build
.PHONY : lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o.provides

lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o.provides.build: lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o


lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o: lib/CMakeFiles/dicom2meshlib.dir/flags.make
lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o: ../lib/src/vtkMeshVisualizer.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/aether/Downloads/DicomToMesh-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o"
	cd /Users/aether/Downloads/DicomToMesh-master/build/lib && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o -c /Users/aether/Downloads/DicomToMesh-master/lib/src/vtkMeshVisualizer.cpp

lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.i"
	cd /Users/aether/Downloads/DicomToMesh-master/build/lib && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/aether/Downloads/DicomToMesh-master/lib/src/vtkMeshVisualizer.cpp > CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.i

lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.s"
	cd /Users/aether/Downloads/DicomToMesh-master/build/lib && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/aether/Downloads/DicomToMesh-master/lib/src/vtkMeshVisualizer.cpp -o CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.s

lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o.requires:

.PHONY : lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o.requires

lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o.provides: lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o.requires
	$(MAKE) -f lib/CMakeFiles/dicom2meshlib.dir/build.make lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o.provides.build
.PHONY : lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o.provides

lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o.provides.build: lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o


# Object files for target dicom2meshlib
dicom2meshlib_OBJECTS = \
"CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o" \
"CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o" \
"CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o"

# External object files for target dicom2meshlib
dicom2meshlib_EXTERNAL_OBJECTS =

lib/libdicom2meshlib.dylib: lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o
lib/libdicom2meshlib.dylib: lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o
lib/libdicom2meshlib.dylib: lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o
lib/libdicom2meshlib.dylib: lib/CMakeFiles/dicom2meshlib.dir/build.make
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkDomainsChemistryOpenGL2-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersFlowPaths-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersGeneric-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersHyperTree-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersParallelImaging-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersPoints-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersProgrammable-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersSMP-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersSelection-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersTexture-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersTopology-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersVerdict-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkGeovisCore-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOAMR-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOEnSight-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOExodus-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOExportOpenGL2-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOImport-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOInfovis-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOLSDyna-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOMINC-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOMovie-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOPLY-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOParallel-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOParallelXML-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOSQL-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOTecplotTable-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOVideo-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkImagingMorphological-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkImagingStatistics-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkImagingStencil-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkInteractionImage-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkRenderingContextOpenGL2-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkRenderingImage-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkRenderingLOD-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkRenderingVolumeOpenGL2-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkViewsContext2D-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkViewsInfovis-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkDomainsChemistry-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkverdict-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkproj4-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersAMR-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOExport-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkRenderingGL2PSOpenGL2-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkgl2ps-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtklibharu-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtklibxml2-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkoggtheora-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersParallel-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkexoIIc-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOGeometry-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIONetCDF-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtknetcdfcpp-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkNetCDF-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkhdf5_hl-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkhdf5-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkjsoncpp-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkParallelCore-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOLegacy-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtksqlite-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkRenderingOpenGL2-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkglew-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkImagingMath-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkChartsCore-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkRenderingContext2D-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersImaging-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkInfovisLayout-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkInfovisCore-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkViewsCore-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkInteractionWidgets-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersHybrid-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkImagingGeneral-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkImagingSources-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersModeling-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkImagingHybrid-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOImage-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkDICOMParser-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkmetaio-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkpng-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtktiff-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkjpeg-8.1.1.dylib
lib/libdicom2meshlib.dylib: /usr/lib/libm.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkInteractionStyle-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersExtraction-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersStatistics-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkImagingFourier-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkalglib-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkRenderingAnnotation-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkImagingColor-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkRenderingVolume-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkImagingCore-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOXML-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOXMLParser-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkIOCore-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtklz4-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkexpat-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkRenderingLabel-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkRenderingFreeType-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkRenderingCore-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkCommonColor-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersGeometry-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersSources-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersGeneral-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkCommonComputationalGeometry-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkFiltersCore-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkCommonExecutionModel-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkCommonDataModel-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkCommonMisc-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkCommonSystem-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtksys-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkCommonTransforms-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkCommonMath-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkCommonCore-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkfreetype-8.1.1.dylib
lib/libdicom2meshlib.dylib: /Users/aether/Downloads/VTK-8.1.0/CMake/lib/libvtkzlib-8.1.1.dylib
lib/libdicom2meshlib.dylib: lib/CMakeFiles/dicom2meshlib.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/aether/Downloads/DicomToMesh-master/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX shared library libdicom2meshlib.dylib"
	cd /Users/aether/Downloads/DicomToMesh-master/build/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/dicom2meshlib.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/CMakeFiles/dicom2meshlib.dir/build: lib/libdicom2meshlib.dylib

.PHONY : lib/CMakeFiles/dicom2meshlib.dir/build

lib/CMakeFiles/dicom2meshlib.dir/requires: lib/CMakeFiles/dicom2meshlib.dir/src/vtkDicomRoutines.cpp.o.requires
lib/CMakeFiles/dicom2meshlib.dir/requires: lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshRoutines.cpp.o.requires
lib/CMakeFiles/dicom2meshlib.dir/requires: lib/CMakeFiles/dicom2meshlib.dir/src/vtkMeshVisualizer.cpp.o.requires

.PHONY : lib/CMakeFiles/dicom2meshlib.dir/requires

lib/CMakeFiles/dicom2meshlib.dir/clean:
	cd /Users/aether/Downloads/DicomToMesh-master/build/lib && $(CMAKE_COMMAND) -P CMakeFiles/dicom2meshlib.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/dicom2meshlib.dir/clean

lib/CMakeFiles/dicom2meshlib.dir/depend:
	cd /Users/aether/Downloads/DicomToMesh-master/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/aether/Downloads/DicomToMesh-master /Users/aether/Downloads/DicomToMesh-master/lib /Users/aether/Downloads/DicomToMesh-master/build /Users/aether/Downloads/DicomToMesh-master/build/lib /Users/aether/Downloads/DicomToMesh-master/build/lib/CMakeFiles/dicom2meshlib.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/CMakeFiles/dicom2meshlib.dir/depend

