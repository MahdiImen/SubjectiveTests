import pymeshlab
import argparse
import os
from datetime import datetime

#input = path to directory where the pointclouds are located. IMPORTANT: directory organization must be of the form bv.: \Maps\object\Ply\SOORT_0001.ply
#output =path to directory where the .obj files should come. IMPORTANT: all meshes must be in folders constructed as bv.: \Maps\object\Stl\SOORT_0001.obj
#object =  which type of pointcloud is desired bv. ['longdress', 'loot', 'redandblack', 'soldier']. If not given, all 4 are taken.
#depth = If depth is given, the meshes for that depth are constructed. If not they are made for 6,7,8,9 and 10. IMPORTANT the folder where the scripts reside must be modified in the meshing function
def main(input, output, object, depth):
    now = datetime.now()
    print("Starting Time:", now)
    objects = ['longdress', 'loot', 'redandblack', 'soldier']
    scripts = 'Scripts'   #place to directory with the scripts from starting place "C:\\Users\\woutm\\unief\\VOP\\scripts --> scripts" for current working directory "C:\\Users\\woutm\\unief\\VOP"

    generationDuration1 = now
    if object is None:
        for pointcloud in objects:
            k = '0001'
            for i in range(1, 301):     #amount of meshes to be generated
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
        for i in range(1, 301):     #amount of meshes to be generated
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
    parser.add_argument('-i', '--input', type=str, required=True, help="input image (PNG)")
    parser.add_argument('-o', '--output', type=str, required=True, help="output file (GIF)")
    parser.add_argument('-s', '--object', type = str, required = False, help = "Which mesh object to create",choices=['longdress', 'loot', 'redandblack', 'soldier'])
    parser.add_argument('-d', '--depth', type = str, required = False, help = "Depth of screened Poisson for mesh generation", choices=['6', '7', '8', '9', '10'])
    args = parser.parse_args()

    main(**vars(args))

