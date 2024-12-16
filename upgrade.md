# Change Command Line Interface Input/Output to GUI

## In General
`input(msg)` == `self.getInput(msg)`

`print(msg)` == `self.print(msg)`
### If there is an menu before and input afterward, e.g.
```
print("Mode :\n1. Auto\n2.Manual")
input("Pilih mode yang tersedia : ")
```
Then, change it into :
```
self.getInput(""Mode :\n1. Auto\n2.Manual\nPilih mode yang tersedia : ")
```
> Make it one line, any output above will be overwritten by the current output.


