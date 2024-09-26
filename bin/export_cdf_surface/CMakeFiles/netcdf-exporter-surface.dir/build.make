# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mikhail/foward_diser

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mikhail/build-diser-Desktop-Release

# Include any dependencies generated for this target.
include export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/compiler_depend.make

# Include the progress variables for this target.
include export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/progress.make

# Include the compile flags for this target's objects.
include export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/flags.make

export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.o: export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/flags.make
export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.o: /home/mikhail/foward_diser/export_cdf_surface/NetCDFExporterSurface.cpp
export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.o: export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/mikhail/build-diser-Desktop-Release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.o"
	cd /home/mikhail/build-diser-Desktop-Release/export_cdf_surface && /usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.o -MF CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.o.d -o CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.o -c /home/mikhail/foward_diser/export_cdf_surface/NetCDFExporterSurface.cpp

export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.i"
	cd /home/mikhail/build-diser-Desktop-Release/export_cdf_surface && /usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/mikhail/foward_diser/export_cdf_surface/NetCDFExporterSurface.cpp > CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.i

export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.s"
	cd /home/mikhail/build-diser-Desktop-Release/export_cdf_surface && /usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/mikhail/foward_diser/export_cdf_surface/NetCDFExporterSurface.cpp -o CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.s

# Object files for target netcdf-exporter-surface
netcdf__exporter__surface_OBJECTS = \
"CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.o"

# External object files for target netcdf-exporter-surface
netcdf__exporter__surface_EXTERNAL_OBJECTS =

export_cdf_surface/netcdf-exporter-surface: export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/NetCDFExporterSurface.cpp.o
export_cdf_surface/netcdf-exporter-surface: export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/build.make
export_cdf_surface/netcdf-exporter-surface: export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/mikhail/build-diser-Desktop-Release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable netcdf-exporter-surface"
	cd /home/mikhail/build-diser-Desktop-Release/export_cdf_surface && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/netcdf-exporter-surface.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/build: export_cdf_surface/netcdf-exporter-surface
.PHONY : export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/build

export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/clean:
	cd /home/mikhail/build-diser-Desktop-Release/export_cdf_surface && $(CMAKE_COMMAND) -P CMakeFiles/netcdf-exporter-surface.dir/cmake_clean.cmake
.PHONY : export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/clean

export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/depend:
	cd /home/mikhail/build-diser-Desktop-Release && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mikhail/foward_diser /home/mikhail/foward_diser/export_cdf_surface /home/mikhail/build-diser-Desktop-Release /home/mikhail/build-diser-Desktop-Release/export_cdf_surface /home/mikhail/build-diser-Desktop-Release/export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : export_cdf_surface/CMakeFiles/netcdf-exporter-surface.dir/depend

