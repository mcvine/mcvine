# Setup development environment

## Use conda to create an env with mcvine dependencies

```
$ conda create -n dev-mcvine python=2
$ conda install <deps>
```

The full list of dependencies can be found in 
https://github.com/mcvine/conda-recipes/blob/master/mcvine-core/meta.yaml

## Activate the new env

```
$ source activate dev-mcvine
```

## Checkout src

```
$ mkdir -p ~/dv/mcvine/build
$ cd ~/dv/mcvine
$ git clone git@github.com:mcvine/mcvine
$ git clone git@github.com:mcvine/resources
```

May need to clone other mcvine subpackages.

## env var shell script

See "envs.sh" in this directory.
Create one similar to that and use it:

```
$ . envs.sh
```
Add it to .bashrc if needed.

## Build and install for the first time
```
$ build0
```

## Build
```
$ mm
```

## Install
```
$ mi
```

## Test
```
$ mt
```
