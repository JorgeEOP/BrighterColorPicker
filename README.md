# BrighterColorPicker

To use the ColorPicker simply clone the code and run
```
python3 main.py
```

You need to have the libraries *pandas* and *request* in oprder for the code to work

## Test
To select any of the tests, only comment and uncomment the lines in the main.py
file (lines 14, 15, 16)

### Test1
For this tests we use the Proposed list:
["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]

The Code throws the correct answer:

```
The brightest color is: #FFFFFF (r=255, g=255, b=255) called White
```


### Test2
For the following tests I have used some random colors from the external API

```

{
  "name": "CornflowerBlue",
  "hex": "6495ED",
  "rgb": "100,149,237"
}
Brightness: 146.86859092399573

{
  "name": "Chartreuse",
  "hex": "7FFF00",
  "rgb": "127,255,0"
}
Brightness: 220.95104435145808

{
  "name": "DarkGoldenrod",
  "hex": "B8860B",
  "rgb": "184,134,11"
}
Brightness: 143.44030117090523
```

In this case, the brightest color should be Chartreuse. This should be thrown by the code.
The code shows the correct result:

```
The brightest color is: #7FFF00 (r=127, g=255, b=0) called Chartreuse
```

## No color in external API (Test3)
If none of the colors provided in the list exists in the external api (available colors are 148 CSS),
then the code throws the message:

```
The color with maximum brightness (RGB: [170, 187, 204]) can not be found in External API
```

## Automatic Tests
To run a series of Tests, go into the folder Tests/
Then type the following command:
```
pytest -v testColorPicker.py
```

This will run the defined tests and report if there is an error in the execution of
the script
