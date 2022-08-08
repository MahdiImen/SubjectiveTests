import pymeshlab
import argparse
import os
from datetime import datetime

#input = path to directory where the pointclouds are located. IMPORTANT: directory organization must be of the form bv.: \PointClouds\8iVFBv2\object\Ply\object_0001.ply
#output =path to directory where the .obj files should come. IMPORTANT: all meshes must be in folders constructed as bv.: \Meshes\object\Stl\object_0001.obj
#object = Which type of pointcloud is to be converted. ['longdress', 'loot', 'redandblack', 'soldier']. If not given, all 4 are taken.
#depth = If depth is given, the meshes for that depth are constructed. If not they are made for 6,7 and 8.
#start = Starting frame number.
#end = Ending frame number.

def main(object, depth, start, end):
    now = datetime.now()
    print("Starting Time:", now)
    objects = ['longdress', 'loot', 'redandblack', 'soldier']
    scripts = 'Scripts'   #place to directory with the scripts

    if start is None:
        start = 1
    if end is None:
        end = 300 


    input = "PointClouds\\8iVFBv2"
    output = "Meshes"


    generationDuration1 = now
    if object is None:
        for pointcloud in objects:
            k = '0001'
            for i in range(start, end+1):    
                if depth is None:
                    for depts in range(6, 9):
                        k = k[:-len(str(i))]+str(i)
                        print(input+'\\'+pointcloud+'\\Ply\\'+pointcloud+'_'+k+'.ply')
                        meshing(input+'\\'+pointcloud+'\\Ply\\'+pointcloud+'_'+k+'.ply', output+'\\'+pointcloud+ '\\depth_' + str(depts) +'\\Stl\\'+pointcloud+'_'+k+'.obj', pointcloud+'_'+k+'_tex.png', scripts+'\\mesh_script_'+str(depts) +'.mlx')
                        generationDuration2 = datetime.now()
                        generationDuration = generationDuration2-generationDuration1
                        print("----> Generation duration: ", generationDuration)
                        generationDuration1 = generationDuration2
                else:
                    k = k[:-len(str(i))]+str(i)
                    print(input+'\\'+pointcloud+'\\Ply\\'+pointcloud+'_'+k+'.ply')
                    meshing(input+'\\'+pointcloud+'\\Ply\\'+pointcloud+'_'+k+'.ply', output+'\\'+pointcloud+ '\\depth_' + str(depth) +'\\Stl\\'+pointcloud+'_'+k+'.obj', pointcloud+'_'+k+'_tex.png', scripts+'\\mesh_script_'+depth +'.mlx')
                    generationDuration2 = datetime.now()
                    generationDuration = generationDuration2-generationDuration1
                    print("----> Generation duration: ", generationDuration)
                    generationDuration1 = generationDuration2
    else:
        k = '0001'
        for i in range(start, end+1):  
            if depth is None:
                for depts in range(6, 9):
                    k = k[:-len(str(i))]+str(i)
                    print(input+'\\'+object+'\\Ply\\'+object+'_'+k+'.ply')
                    meshing(input+'\\'+object+'\\Ply\\'+object+'_'+k+'.ply', output+'\\'+object+ '\\depth_' + str(depts) +'\\Stl\\'+object+'_'+k+'.obj', object+'_'+k+'_tex.png', scripts+'\\mesh_script_'+str(depts) +'.mlx')
                    generationDuration2 = datetime.now()
                    generationDuration = generationDuration2-generationDuration1
                    print("----> Generation duration: ", generationDuration)
                    generationDuration1 = generationDuration2
            else:
                k = k[:-len(str(i))]+str(i)
                print(input+'\\'+object+'\\Ply\\'+object+'_'+k+'.ply')
                meshing(input+'\\'+object+'\\Ply\\'+object+'_'+k+'.ply', output+'\\'+object+ '\\depth_' + str(depth) +'\\Stl\\'+object+'_'+k+'.obj', object+'_'+k+'_tex.png', scripts+'\\mesh_script_'+ depth  +'.mlx')
                generationDuration2 = datetime.now()
                generationDuration = generationDuration2-generationDuration1
                print("----> Generation duration: ", generationDuration)
                generationDuration1 = generationDuration2
    end = datetime.now()
    endDuration = end - now
    
    print("End Time:", end)
    print("---> Duration: ", endDuration)

            


def meshing(input, output, texturename, script):
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(input)
    ms.load_filter_script(script)
    ms.apply_filter_script()
    #makes texture for mesh
    ms.transfer_attributes_to_texture_per_vertex(sourcemesh=0,targetmesh= 1, textname=texturename,textw = 4096,texth= 4096)
    ms.save_current_mesh(output)
    return

if __name__ == '__main__':
    class CustomHelpFormatter(argparse.HelpFormatter):
        def _format_action_invocation(self, action):
            if not action.option_strings or action.nargs == 0:
                return super()._format_action_invocation(action)
            default = self._get_default_metavar_for_optional(action)
            args_string = self._format_args(action, default)
            return ', '.join(action.option_strings) + '   ' + args_string

    parser = argparse.ArgumentParser(formatter_class=CustomHelpFormatter)
    parser.add_argument('-o', '--object', type = str, required = False, help = "Which mesh object to create",choices=['longdress', 'loot', 'redandblack', 'soldier'])
    parser.add_argument('-d', '--depth', type = str, required = False, help = "Depth of screened Poisson for mesh generation", choices=['6', '7', '8'])
    parser.add_argument('-s', '--start', type = int, required = False, help = "Starting frame number",choices=range(1,300))
    parser.add_argument('-e', '--end', type = int, required = False, help = "Ending frame number", choices=range(1,300))
    args = parser.parse_args()

    main(**vars(args))

