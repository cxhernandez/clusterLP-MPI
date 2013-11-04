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

This script uses hybrid MPI/OpenMP paralleism in addition to highly optimized
SIMD vectorization within the compute kernels. Using multiple MPI processes
requires running this command using your MPI implementation's process manager,
e.g. `mpirun`, `mpiexec`, or `aprun`. The number of OpenMP threads can be
controled by setting the OMP_NUM_THREADS environment variable. (e.g.
$ export OMP_NUM_THREADS=4; mpirun -np 16 clusterLP-MPI <options>)
