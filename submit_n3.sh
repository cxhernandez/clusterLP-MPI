#!/bin/bash
#PBS -N clusterLP-MPI
#PBS -e ~/test20.err
#PBS -o ~/test20.out
#PBS -l nodes=6:ppn=12
#PBS -m e
#PBS -V
#PBS -l walltime=99:00:00 

source ~/.bash_profile
export PBS_O_WORKDIR
  
echo The master node of this job is `hostname`
echo The working directory is `echo $PBS_O_WORKDIR`
echo This job runs on the following nodes:
echo `cat $PBS_NODEFILE` 

SD=$PYTHONLIB/site-packages/msmbuilder-2.7.dev-py2.7-linux-x86_64.egg/msmbuilder/scripts/
OMP_NUM_THREADS=12

cd $MSMPATH
# have mpi ranks print out the node
mkdir d3/
time `mpirun -np 72 -wd $PBS_O_WORKDIR --hostfile $PBS_NODEFILE --bynode $PYTHONPATH/python -u $PATHTOCLUSTERLP-MPI/clusterLP-MPI -pi $PBS_O_WORKDIR/sirtuin_Calpha_indices.dat -li $PBS_O_WORKDIR/p53_Calpha_indices.dat -td $PBS_O_WORKDIR/dcd/ -ext dcd -top $PBS_O_WORKDIR/sir2_bound_reference.pdb -o d3/clusters.csv -d 0.3 >clust3.out`

