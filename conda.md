## conda environment
__ONLY WORKS ON CMD NOT POWERSHELL__
- create an environment
`conda create --name leavesEnv python=3.6 scipy numpy`
- check envs
`conda info --env` or `conda list`
- activate env
`activate leavesEnv` and `deactivate leavesEnv`
- remove envs
`conda remove --name leavesEnv --all`
- jupyter should be installed in a specific env

## tensorflow
- Install
`pip install tensorflow` or `pip install tensorflow-gpu`
- Test if GPU available
`sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))`
