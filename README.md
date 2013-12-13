AirJam
===
*In air jammin*

Virtual music instruments based on gesture recognition. Works on computer vision using webcams.

###Dependencies
* [Python 2.7.*](http://www.python.org)
* [Numpy](http://www.numpy.org)
* [PyMedia](http://www.pymedia.org)
* [Sox](http://sox.sourceforge.net)
* **OpenCV** Python : See setup instructions [here](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_setup/py_table_of_contents_setup/py_table_of_contents_setup.html#table-of-content-setup).

###Working
===
#####The Guitar
* Wear three color strips in three fingers of the non-strumming hand ( RGB in index-middle-ring )
* Wear a Red strip in the strumming hand's finger (any finger)
* Strum !!

#####The Drums
* Use sticks with red heads.

*You need to set the color ranges in `./config/color_config.py` before anything.*
*You might also need to configure the drums (if you need) using `./config/drums_config.py` and appropriately supply the `.wav` files in `./sounds/drums/`*

###License
MIT Licensed
Copyright (C) 2013 Abhinav Tushar.