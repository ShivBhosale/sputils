# Superpaper Utils
Utils and Notebooks for building deep-learing models with data-generated from [superpaper web-app](https://superpaper.netlify.app/).

P.S: Most images in dataset are gonna be low in quality as thats how good my art-skills are

# Data

The stroke-data is exported as a json file. Use the ExploreStrokes.ipynb notebook to use utils for exploring data.

Currently, a single data-point comprises on 3 elements:

1) Stroke JSON
2) Base image
3) Sketch Layer

---

## 1. Stroke JSON 
```
{
	"description": "<str:title of the art work>",
	"stroke": [{
		"layer": "<str:Layer name>",
		"type": "<str:mouseup or penup>",
		"memento": [
			[<int:x-xcor>, <int:y-cor>, <int:offset-x>, <int:offset-y>],
			[809, 124, -310, -10],
            .
            .
			[]
		]
	}, {
		"layer": "Layer 1",
		"type": "mouseup",
		"memento": [
			[811, 126, -310, -10],
			[811, 126, -310, -10],
            .
            .
            .
			[]
		]
	}
    .
    .
    .],
	"device_type": "pc",
	"canvas_h": 649,
	"canvas_w": 999
}
```

Note that an empty entry in memento (i.e. []) signifies end of stroke

## 2. Base Image
This is the image used as reference for drawing the data

![alt text](<data/superpaper/Base_Layer (2).png>)


## 3. Sketch Layer
This is the image that was exported after drawing (p.s forgive me for this garbage trace)

![alt text](<data/superpaper/Layer_1 (2).png>)

---

# TODO
- [ ] Add Sketch-RNN wrapper
- [X] Create section for comic
