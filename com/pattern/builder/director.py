class Director:
    
    def __init__(self,builder):
        print('Director build')
        self._builder = builder
        
    def construct(self):
        print('Director construct')
        self._builder.build_part1()
        self._builder.build_part2()