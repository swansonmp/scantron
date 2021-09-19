# scantron

Lightweight quiz scoring application written in Python.

## Usage

```bash
$ python scantron.py -h
usage: scantron.py [-h] [-e EXPECTED] [-a ACTUAL]

Tabulates results of tests

optional arguments:
  -h, --help            show this help message and exit
  -e EXPECTED, --expected EXPECTED
                        Expected answers file name
  -a ACTUAL, --actual ACTUAL
                        Actual answers file name
```

## Example

### Expected

Provide the answer key in the file named `expected`.
You may use another file by using the `-e` argument.

```
c
c
a,b
a,b
c
c
c
c
c
a,b,c
```

### Actual

Provide the answers in the file named `actual`.
You may use another file by using the `-a` argument.

```
c
c
a,b
c,d
c
c
a
c
c
a,b,d
```

### Result

`scantron` uses `colorama` for terminal coloring.

```bash
$ python scantron.py 
Q	E	A
------------------------
1.	C	C
2.	C	C
3.	A,B	A,B
4.	A,B	C,D
5.	C	C
6.	C	C
7.	C	A
8.	C	C
9.	C	C
10.	A,B,C	A,B,D
------------------------
Results: 7.3 of 10 (0.73)
```
