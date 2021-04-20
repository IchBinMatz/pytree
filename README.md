# Pytree
this reads in the given directory and creates a file tree in readable text format


prints the current directory:

``` sh
pytree .
```

prints the current directory with hidden files and folders
``` sh
pytree --hidden .
```

if your modules are not in path, you can use `pytree` via

``` sh
python3 -m pytree .
```
or on windows:

``` cmd
py -m pytree .
```

## example output

``` 
.
+-- thisFolder.md
+-- test
|   +-- test2
|   |   +-- bla
|   |   +-- blaa
|   |   
|   +-- foo
|   +-- bar
|   
+-- setup.py
+-- README.md
+-- LICENSE

```

## Installation

clone this repository
and then install with pip

``` sh
git clone https://github.com/IchBinMatz/pytree
cd pytree
pip install .
```
