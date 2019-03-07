class Screen(object):
    
    @property
    def  width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.__width = value
        
    @property
    def height(self):
        return self.__heigtht
    
    @height.setter
    def height(self, value):
        self.__height = value
        
    @property
    def resolution(self):
        return self.__width * self.__height

    
if __name__ == "__main__":
    s = Screen()
    s.width = 1024
    s.height = 768
    print('resolution =', s.resolution)
    if s.resolution == 786432:
        print('pass')
    else:
        print('fail')
        
    
