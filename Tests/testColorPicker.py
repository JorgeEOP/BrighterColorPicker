import pytest
from pandas import DataFrame as df
import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from RestRequests.ColorsRequest import ColorsRequest as cr
from ColorPicker.ColorsPicker import ColorPicker as cp


def testRestRequestColors():
    request = cr()
    assert request.requestColors()

def testSizeOfDF():
    request = cr()
    request.requestColors()
    colorsDF: df = request.getFormattedColorsDF()
    assert len(colorsDF.index) == 148

def testGetBrightestColor_Black():
    test = ["#000000"]
    picker = cp(test)
    colorsAsDecimal = picker.transformRGBToDecimal()
    brightestColor: list[int] = picker.getBrightestsColor(colorsAsDecimal)
    assert brightestColor[0] == 0 
    assert brightestColor[1] == 0 
    assert brightestColor[2] == 0 

def testGetBrightestColor_NotInAPI():
    with pytest.raises(IndexError):
        test = ["#AABBCC", "#154331", "#A0B1C2", "#000000"]
        picker = cp(test)
        colorsAsDecimal = picker.transformRGBToDecimal()
        brightestColor: list[int] = picker.getBrightestsColor(colorsAsDecimal)
        
        colorsAPI = cr()
        colorsAPI.requestColors()
        colorsDF: df = colorsAPI.getFormattedColorsDF()
        
        condition = ((colorsDF['r'] == brightestColor[0]) &
                        (colorsDF['g'] == brightestColor[1]) &
                        (colorsDF['b'] == brightestColor[2])
                        )
        
        color = colorsDF[condition]
        colorInfo = color.values[0].tolist()

        result = 'The brightest color is: {} (r={}, g={}, b={}) called {}'.format(colorInfo[4],
                                                                                    colorInfo[1],
                                                                                    colorInfo[2],
                                                                                    colorInfo[3],
                                                                                    colorInfo[0])
def testBrightestColorIsWhite():
    test = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]

    picker = cp(test)
    colorsAsDecimal = picker.transformRGBToDecimal()
    brightestColor: list[int] = picker.getBrightestsColor(colorsAsDecimal)
        
    colorsAPI = cr()
    colorsAPI.requestColors()
    colorsDF: df = colorsAPI.getFormattedColorsDF()
        
    condition = ((colorsDF['r'] == brightestColor[0]) &
                    (colorsDF['g'] == brightestColor[1]) &
                    (colorsDF['b'] == brightestColor[2])
                )
        
    color = colorsDF[condition]
    colorInfo = color.values[0].tolist()

    result = 'The brightest color is: {} (r={}, g={}, b={}) called {}'.format(colorInfo[4],
                                                                                    colorInfo[1],
                                                                                    colorInfo[2],
                                                                                    colorInfo[3],
                                                                                    colorInfo[0])
    assert result == "The brightest color is: #FFFFFF (r=255, g=255, b=255) called White"