import ColorPicker
from RestRequests.ColorsRequest import ColorsRequest as cr
from ColorPicker.ColorsPicker import ColorPicker as cp

from pandas import DataFrame as df

if __name__ == "__main__":

    '''
    Algorithm:
        get the brightest color from the list as 'RRR,GGG,BBB'
        get the colors List from External API (formatted as DF)
        compare the brightest Color found to data
    '''

    #testList = ["#AABBCC", "#154331", "#A0B1C2", "#000000", "#FFFFFF"]
    testList = ["#000000", "#7FFF00"]

    picker = cp(testList)
    colorsAsDecimal = picker.transformRGBToDecimal()
    brightestColor: list[int] = picker.getBrightestsColor(colorsAsDecimal)
    #print ("BrightestColor: ", brightestColor)


    colorsAPI = cr()
    colorsAPI.requestColors()
    colorsDF: df = colorsAPI.getColorsDF()

    #print (colorsDF)

    #condition = ((colorsDF['r'] == brightestColor[0]))

    try:
        condition = ((colorsDF['r'] == brightestColor[0]) &
                     (colorsDF['g'] == brightestColor[1]) &
                     (colorsDF['b'] == brightestColor[2])
                     )
    
    
        color = colorsDF[condition]
        colorInfo = color.values[0].tolist()

        result = 'The brightest color is: {} (r={}, g={}, b={}) called {}'.format(colorInfo[4], colorInfo[1], colorInfo[2], colorInfo[3], colorInfo[0] )
        print(result)
    except IndexError:
        print('The color with maximum brightness (RGB: {}) can not be found in External API'.format(brightestColor))