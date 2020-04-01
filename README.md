# Phonia Toolkit

![phonia](https://user-images.githubusercontent.com/54115104/74159383-c2e0b600-4c2c-11ea-9aeb-62146b1af5bf.jpeg)

<p align="center">
  <a href="http://entynetproject.simplesite.com/">
    <img src="https://img.shields.io/badge/entynetproject-Ivan%20Nikolsky-blue.svg">
  </a>
  <a href="https://github.com/entynetproject/phonia/releases">
    <img src="https://img.shields.io/github/release/entynetproject/phonia.svg">
  </a>
  <a href="https://wikipedia.org/wiki/Python_(programming_language)">
    <img src="https://img.shields.io/badge/language-python-blue.svg">
 </a>
  <a href="https://github.com/entynetproject/phonia/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues/entynetproject/phonia.svg">
  </a>
  <a href="https://github.com/entynetproject/phonia/wiki">
      <img src="https://img.shields.io/badge/wiki%20-phonia-lightgrey.svg">
 </a>
  <a href="https://twitter.com/entynetproject">
    <img src="https://img.shields.io/badge/twitter-entynetproject-blue.svg">
 </a>
</p>

***

# About Phonia Toolkit

```
Phonia Toolkit is one of the most advanced toolkits to scan 
phone numbers using only free resources. The goal is to first gather 
standard information such as country, area, carrier and line type on 
any international phone numbers with a very good accuracy.
```

***

# Getting started

## Phonia installation

> cd phonia

> chmod +x install.sh

> ./install.sh

## Phonia uninstallation

> cd phonia

> chmod +x uninstall.sh

> ./uninstall.sh

***

# Phonia Toolkit execution

> phonia -h

```
usage: phonia [-h] [-p <phone>] [-i <inputfile>] [-o <outputfile>]
              [-s <scanner>] [--recon] [--no-ansi] [-u] [--version]

optional arguments:
  -h, --help            show this help message and exit
  -p <phone>, --phone <phone>
                        The phone number to scan.
  -i <inputfile>, --input <inputfile>
                        List of phone numbers to scan.
  -o <outputfile>, --output <outputfile>
                        Output to save scan results.
  -s <scanner>, --scanner <scanner>
                        The scanner to use.
  --recon               Launch custom format reconnaissance.
  --no-ansi             Disable colored output.
  -u, --update          Update Phonia Toolkit.
  --version             Show Phonia Toolkit version.
```

***
  
# Phonia Toolkit examples

## Example of scanning a phone number
    
> phonia -p 15554443333
    
## Example of scanning from a file

> phonia -i input.txt -o output.txt
    
## Example of selecting a scanner

> phonia -p 15554443333 -s footprints

***

# Phonia Toolkit disclaimer

```
Usage of the Phonia Toolkit for attacking targets without prior mutual consent is illegal.
It is the end user's responsibility to obey all applicable local, state, federal, and international laws.
Developers assume no liability and are not responsible for any misuse or damage caused by this program.
```

***

# Phonia Toolkit license

```
MIT License

Copyright (C) 2019-2020, Entynetproject. All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
