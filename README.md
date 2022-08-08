# SubjectiveTests

## Introduction


## Requirements

## Steps to follow
### Convert PointClouds to Meshes

We will be using the [JPEG Pleno Database: 8i Voxelized Full Bodies (8iVFB v2)](http://plenodb.jpeg.org/pc/8ilabs/) with 4 different human subjects. We will first convert these objects to meshes.

1. Download the [8iVFB dataset](http://plenodb.jpeg.org/pc/8ilabs/) (5.5GB)
2. Navigate to the "PointCloudConverter" directory and extract the files in the "PointClouds" folder. You should have the following file structure.


**IMPORTANT NOTE**: keep the same folder names and structure. If you change them, make sure you change the input variables in the scripts.

```
	>PointCloudConverter
		>PointClouds
			>8iVFBv2
				>longdress
					>Ply
						>longdress_vox10_1051.ply
				>loot
				>redandblack
				>soldier
			>RenameFiles.py
		>Meshes
		>Scripts
		>meshlab.py
```

3. Navigate to the PointClouds folder in terminal and run the RenameFiles.py script.
```
>>>python RenameFiles.py
```

Once this is done, your Ply folders should look like this:

4.	In terminal, navigate back to the PointCloudConverter directory and run the meshlab.py script.

```
>>>python meshlab.py
```

You can also specify which object you want to convert, at which depth, starting from which frame and ending at which one.

* -o --object = Which type of pointcloud is to be converted. ['longdress', 'loot', 'redandblack', 'soldier']. If not given, all 4 are taken. If not precised, all objects will be considered.
* -d --depth = If depth is given, the meshes for that depth are constructed. If not they are made for 6,7 and 8. If not precised, all depths will be considered.
* -s --start = Starting frame number. If not precised, frames created will start from 1.
* -e --end = Ending frame number. If not precised, frames created will end at 300.

**Example**: 
```
>>>python meshlab.py -o longdress -d 8 -s 150 -e 300
```
 This will only create 150 frames of the longdress object at depth 8.

**IMPORTANT NOTE**: Depending on the machine running, this process will take hours to finish running. We recommend converting only 150 frames per object as only these will be used in the subjective tests. 

5. Once that's established, you can copy the Meshes folder into the MeshRenderer/Assets/Resources directory





