import math

class ColorPicker():
    '''
    __hexMap = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    '''

    # __listOfColors has the format ["#AABBCC", "#154331", ...]
    __listOfColors: list[str]
    def __init__(self, _listOfColors):
        self.__listOfColors = _listOfColors
    
    def brightestsOfTheColor(self, R: float, G: float, B: float) -> float:
        brightness: float = 0.0
        brightness = math.sqrt( 0.241* R**2 + 0.691 * G**2 + 0.068 * B**2 )

    # (F = 15, FF = 15 * 16 + 15 * 1 = 240 + 15 = 255)
    def transformRGBToDecimal(self) -> tuple[int, int, int] :
        assert self.__listOfColors is not None

        colorsAsDecimal = []
        #Order!
        colorsAsDecimal = [ ( int(i[1:3], 16), int(i[3:5], 16) , int(i[5:7], 16) ) for i in self.__listOfColors ]
        #print(colorsAsDecimal)

        return colorsAsDecimal
    
    #Complexity: O(n)?
    def getBrightestsColor(self, _colorsInDecimalFormat: list[tuple[int, int, int]]) -> list[int] :
        #According to brightness definition, brightness >= 0
        brightness: float = 0
        color = ''

        for i in _colorsInDecimalFormat:
            br = math.sqrt( 0.241* i[0]**2 + 0.691 * i[1]**2 + 0.068 * i[2]**2 )
            br = round(br, 4)
            if (br > brightness):
                brightness = br
                color = [i[0], i[1], i[2]]

        return color