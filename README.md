# WarpScript magic

Ipython magic command to execute a WarpScript on a Warp10 backend.

## Installation

A jupyter notebook is necessary. In case you don't have Jupyter installed you can follow the instructions on the [Jupyter official page](http://jupyter.readthedocs.org/en/latest/index.html).

Download this repo and and inside the WarpScriptMagic folder type:
```
python setup.py install
```

If you have any problem with the installation, please, open an issue.

## Usage

example:

```
%%warpscript -u http://localhost:8080

[ 'READTOKEN' 'mydata' {} NOW -100 ] FETCH

// Some Warpscript code

```

-u correspond to the Warp10 backend to reach. It can be using http or https.



