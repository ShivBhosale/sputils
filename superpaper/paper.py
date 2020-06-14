import os
import json
from PIL import Image, ImageDraw
import numpy as np
from functools import reduce
from collections import defaultdict, namedtuple
class superpaper:
    """
        A Utility to parse stroke data from 
    """
    def __init__(self,file_path):
        assert(os.path.exists(file_path)), "No stroke file found @ {}!".format(file_path)
        assert(file_path.endswith('.json')), "The input file type must be a .json file"
        with open(file_path, "r") as f:
            self.stroke_data = json.loads(f.read())
        self.__parse_json()
        
        self.__plot_image()
        
    def __parse_json(self):
        self.height = int(self.stroke_data['canvas_h'])
        self.width = int(self.stroke_data['canvas_w'])
        self.shape = (self.width, self.height)
        self.description = self.stroke_data['description']
        self.drawing = {}
        self.stroke = {}
        
    
    def __plot_image(self):
        self.art = Image.new('L', (self.width, self.height), 255)
        self.draw = ImageDraw.Draw(self.art)
        self.drawing['all'] = self.art
        for data in self.stroke_data['stroke']:
            layer_object = self.drawing.get(data['layer'], False)
            stroke_object = self.stroke.get(data['layer'], False)
            if not layer_object:
                self.drawing[data['layer']] = Image.new('L', (self.width, self.height), 255)
                layer_object = self.drawing[data['layer']] 
            if not stroke_object:
                self.stroke[data['layer']] = []
                stroke_object = self.stroke[data['layer']] 
            layer_draw_obj = ImageDraw.Draw(layer_object)
            # last stroke memento is always an empty list
            stroke_list = data['memento'][:-1]
            if stroke_list:
                stroke_path = np.array(list(map(lambda x: [x[0]+x[2], x[1]+x[3]], stroke_list))).T.tolist()
                stroke_path_zipped = list(zip(stroke_path[0], stroke_path[1]))
                self.draw.line(stroke_path_zipped, fill=0, width=2)
                layer_draw_obj.line(stroke_path_zipped, fill=0, width=2)
                stroke_object.append(stroke_path)
                
    def show(self, layer='all'):
        if layer in self.drawing:
            self.drawing[layer].show()
        else:
            print('No layer found by that name!')
    
    def getLayers(self):
        return self.drawing
        
        