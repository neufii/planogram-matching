This annotation refers to the test and train images of the Grocery Store dataset available here:
https://www.amazon.de/clouddrive/share/J3OaZMNnhBpKG28mAfs5CqTgreQxFCY8uENGaIk7H3s?_encoding=UTF8&mgh=1&ref_=cd_ph_share_link_copy

To use the annotation you will also need some additional product images to complete the dataset that you can find inside 'extra_products' folder.

If you use this dataset in your work please cite:

For the Grocery Store Dataset:
@inproceedings{george2014recognizing,
  title={Recognizing products: A per-exemplar multi-label image classification approach},
  author={George, Marian and Floerkemeier, Christian},
  booktitle={European Conference on Computer Vision},
  pages={440--455},
  year={2014},
  organization={Springer}
} 

For the Annotation:
@inproceedings{tonioni2017product,
  title={Product recognition in store shelves as a sub-graph isomorphism problem},
  author={Tonioni, Alessio and Di Stefano, Luigi},
  booktitle={International Conference on Image Analysis and Processing},
  year={2017}
}

##################################################################
This package contains two subfolders:
	- Annotations: with one csv file for each test image containing the bounding box of the single product instances
	- Planograms: with one json file for each test image containing the graph structure of the ideal planogram for that scene.
	- Extra_prodcts: additional product images to complete the Grocery Store Dataset.

The file are named according to the following scheme:
s{store_number}_{image_number}

Example: file "s1_14.csv" refers to test image "Testing/store1/images/14.jpg" of the Grocery Store Dataset

##################################################################
##                                                              ##
##                    Annotation Folder                         ##
##                                                              ##
##################################################################
Each csv file contains all the axis aligned bounding boxes of the products visible in that scene.
Each line refers to a bounding box and contains 5 value with the following meaning:
	${Relative path to the product image},${xmin},${ymin},${xmax},${ymax}

	|----------------------------------> x
	|
	|
	|       
	|     (xmin, ymin)______
	|                |      | 
	|                |______| 
	|                       (xmax, ymax)
	|
	|
	|
	|
	v  y


##################################################################
##                                                              ##
##                    Planogram Folder                          ##
##                                                              ##
##################################################################
Each file encodes in json a dictionary describing the graph representation of the planogram.
The dictionary has two main keys 
	-"objects": the list of objects described in the graph, each object is identified by its position in the list
		-Each entry has 3 field:
			+"img_path" --> relative path to the object image in the grocery store dataset
			+"height" --> scale factor for height between the image of the object in the scene and the template image, not used.
			+"width" --> scale factor for height between the image of the object in the scene and the template image, not used.

	-"graph": list of nodes of the graph with their connections, each node is identified by its position in the list
		-Each entry represent a node in the graph and is uniquely identified by its position in the list. Each node has 9 fields:
			+ogg: index of the object in that node (e.g. 0 refers to the first element of the "objects" list above and so on)
			+n,nw,w,sw,s,se,e,ne: index of the neighbor connected to this node with that kind of connection, '-1' if it is not connected to anything.

			Example:

			  0: {"ne": -1, "nw": -1, "se": 24, "e": 25, "w": -1, "sw": -1, "s": 1, "ogg": 0, "n": -1 }


                        nw      n      ne
                          \     |     /                           "Just one neighbour drawn, but node 0 will actually ave neighbours at se,e,sw and s"
			  			   \____|____/          __________
			  		w _____|   id:0  |_____e____|  id:25  |
			  			   |_________|          |_________|
			  			   /    |    \
			  			  /     |     \
			  			sw      s     se