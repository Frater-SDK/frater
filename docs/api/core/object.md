# object

## Classes
The `object` subpackage has the following classes available for use. Th
### Object
`Object` is a container class to represent an object throughout a video. It can be considered a sequence of 
[Object Detections](#objectdetection) for the same object in a video.   
### ObjectDetection

#### `__init__()`
`ObjectDetection` is a container class to represent a single instance of an object. It can be from a frame of a video,   
or from some other image source. It includes 
##
### ObjectType

## Factory Methods

## Functions

### temporally_segment_objects(object\[, window_size=90\])
Return a list of copies of the object segmented into windows of size `window_size` over the object's trajectory.
The input 
If an object is shorter than the defined window size, the original object is returned in a list.
