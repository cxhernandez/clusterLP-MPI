[![DOI](https://zenodo.org/badge/9890/cxhernandez/msmbuilderMPITools.svg)](http://dx.doi.org/10.5281/zenodo.14963)
MSMbuilder MPITools
=============
## Overview
Cluster a protein-ligand system with RMSD using separate sets of atoms for the
alignment and distance computation. Both the "alignment" and "distance" atoms
for each frame will be loaded, and in each frame, the cartesian center of the
alignment atoms is computed and subtracted out of the coordinates of both the
alignment and distance atoms.

Distances are calculated between two frames by computing the rotation matrix
which optimally overlays the alignment atoms with one and other, and then
applying that rotation matrix to the distance atoms in the first frame and
computing their root-mean-squared deviation w.r.t the other frame.

Clustering is performed with the k-centers algorithm. You may specify the
termination criterion either by the number of states, or a cutoff distance
(which ensures that all data points are within that distance of their assigned
cluster center).

These scripts uses hybrid MPI/OpenMP paralleism in addition to highly optimized
SIMD vectorization within the compute kernels. Using multiple MPI processes
requires running this command using your MPI implementation's process manager,
e.g. `mpirun`, `mpiexec`, or `aprun`. The number of OpenMP threads can be
controled by setting the `OMP_NUM_THREADS` environment variable. For example,

```
$ export OMP_NUM_THREADS=4
$ mpirun -np 16 clusterLP-MPI <options>
$ mpirun -np 16 assignLP-MPI <options>
```

## Dependencies
This script requires python, the latest development version of MDTraj available
[on github](https://github.com/rmcgibbo/mdtraj), numpy, and mpi4py.

## Installation
No installation is required. Just call the script or move it into your `PATH`
if you like.
