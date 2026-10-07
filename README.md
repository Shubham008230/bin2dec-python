# Bin2Dec (Python)

A command-line tool that converts up to 8 binary digits into a decimal number.

## Features
- Accepts 1 to 8 binary digits
- Shows an error if anything other than 0 or 1 is entered
- Converts without storing digits in an array
- Uses powers of 2 (`2 ** position`) to calculate each digit's value

## How to run
```
python bin2dec.py
```
Type `q` to quit.

## Example
```
Enter up to 8 bits of binary (or 'q' to quit): 101
Decimal value: 5
```

## Run the tests
```
python test_bin2dec.py
```

## enumerate, splitting code into functions,