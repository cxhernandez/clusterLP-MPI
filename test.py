import os
import shutil
import tempfile
import numpy as np
import scripttest
import pandas as pd
import mdtraj as md
import mdtraj.testing


staging_dir = tempfile.mkdtemp()
output_dir = os.path.join(staging_dir, 'out')
def setup():
    np.savetxt(os.path.join(staging_dir, 'pi.dat'), [1,2,3], '%d')
    np.savetxt(os.path.join(staging_dir, 'li.dat'), [4,5,6], '%d')
    top = md.load(mdtraj.testing.get_fn('native.pdb')).top

    for i in range(10):
        l = np.random.randint(low=10, high=500)
        t = md.Trajectory(np.random.randn(l,22,3), topology=top)
        t.save(os.path.join(staging_dir, 'trj-%d.dcd' % i))
    t.save(os.path.join(staging_dir, 'top.pdb'))

def teardown_module(module):
    shutil.rmtree(staging_dir)

def test_1():
    env = scripttest.TestFileEnvironment(output_dir)
    s = os.path.abspath('clusterLP-MPI')

    results = []
    for i in range(1, 10):
        cmd = 'mpirun -np %d %s -pi ../pi.dat -li ../li.dat -td ../ -ext dcd -top ../top.pdb -k 30 -o out-%d.csv' % (i, s, i)
        env.run(cmd)
        print env.run('cat out-%d.csv' % i)
        results.append(pd.read_csv(os.path.join(output_dir, 'out-1.csv'), names=['trj', 'index'], skiprows=4))

    for i in range(len(results)):
        results[i].sort()
        assert np.all(results[0]['index'] == results[i]['index'])
        assert np.all(results[0]['trj'] == results[i]['trj'])


if __name__ == '__main__':
    setup()
