import requests as rq
from pandas import DataFrame as df

# TODO: Cache the color list from the requested API
class ColorsRequest:
    __formattedColorsDF: df
    def __init__(self):
        self.urlBase: str = 'https://www.csscolorsapi.com/'
        #self.__formattedColors = {}

    def requestColors(self): 
        try:

            request = rq.get(self.urlBase + 'api/colors')
            if (request.status_code != 200):
                return None
        
            #print("the Json: ", request.json())
            json = request.json()
            self.setFormattedColorsDF(json["colors"])

            return rq
        
        except ConnectionError:
            print("ConnectionError: Unable to connect to server")
    '''
    Expects a list in the format: [{
      "name": "AliceBlue",
      "theme": "light",
      "group": "Gray",
      "hex": "F0F8FF",
      "rgb": "240,248,255"
    }]
    '''
    def setFormattedColorsDF(self, _colorsListFromAPI):
        formattedColorList = []

        for i in _colorsListFromAPI:
            color = {}
            rgb = str(i['rgb']).split(',')

            color["name"] = str(i['name'])
            #color["rgb"] = str(i["rgb"])
            color["r"] = int(rgb[0])
            color["g"] = int(rgb[1])
            color["b"] = int(rgb[2])
            color['hex'] = '#' + str(i['hex']).upper()

            formattedColorList.append(color)

        colors = df(formattedColorList)
        #colors.set_index("rgb", inplace=True)

        self.__formattedColorsDF = colors

    '''
    returns: The colors as DF
    '''
    def getColorsDF(self) -> df:
        return self.__formattedColorsDF