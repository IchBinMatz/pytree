# filetreeMarkdown
this reads in the given directory and creates a file tree in readable text format


prints the current directory:

``` sh
pytree .
```

prints the current directory with hidden files and folders
``` sh
pytree --hidden .
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
