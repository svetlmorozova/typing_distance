# Typing distance
This is the Python CLI application for calculating the typing distance of the input string. 
The keyboard is presented as a two-dimensional array where every key is assigned its coordinates.

![Image](https://user-images.githubusercontent.com/19284162/79064722-19fa1a00-7cb4-11ea-8f03-4122622a758e.png)

Here, the distance is calculated as following:
>![Image](https://user-images.githubusercontent.com/19284162/79068941-293c9000-7cd3-11ea-814d-9b885a555f03.png)
> _where n is the length of input string._

You can also get an averaged distance, which represents the average typing distance between keys in the input string:
>![Image](https://user-images.githubusercontent.com/19284162/79068914-03af8680-7cd3-11ea-8c8d-6ab7fda5464c.png)
> _where n is the length of input string._

The idea is to give a perception of string complexity: for example, ```qwerty``` is easier to type rather than ```string```. 
For ```qwerty``` this distance is 5 (averaged is 1.0), while for ```string``` it is 12 (averaged is 2.4).

# Installation
After cloning this repo just run ```python setup.py install```

# Usage
**Help**:
```console
foo@bar:~$ python3 -m typing_distance --help
Usage: __main__.py [OPTIONS]

  Calculate and return typing distance for a given string

Options:
  -s, --string TEXT         Input string
  -kb, --keyboard [MAC]     What keyboard to use
  -avg, --averaged BOOLEAN  Return average value
  --help                    Show this message and exit.
```
**Get absolute distance**:
```console
foo@bar:~$ python3 -m typing_distance -s <your_string>
```
**Get averaged distance**:
```console
foo@bar:~$ python3 -m typing_distance -avg True -s <your_string>
```
**Unknown char**: 

As for now, ```typing_distance``` can handle only chars presented in **English MAC keyboard**, so if you'll try to type other characters, you will get the error:
```console
foo@bar:~$ python3 -m typing_distance -avg True -s строка
Your line contains chars which are not presented in chosen keyboard: MAC
```

## Example
**Absolute distance**
```console
foo@bar:~$ python3 -m typing_distance -s qwerty
Typing distance is 5
```
```console
foo@bar:~$ python3 -m typing_distance
string: some_distance
Typing distance is 59
```
**Averaged distance**
```console
foo@bar:~$ python3 -m typing_distance -avg True -s qwerty
Averaged typing distance is 1.0
```
```console
foo@bar:~$ python3 -m typing_distance -avg True
string: some_distance
Averaged typing distance is 4.9
```