# BrighterColorPicker

## Test
For Testing I have used some random colors from the external API

### Test1
For this tests we use the Proposed list:
["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]

The Code throws the correct answer:

```
The brightest color is: #FFFFFF (r=255, g=255, b=255) called White
```


### Test2

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

In this case, the brightest color should be Chartreuse. This should be thrown by the code
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