using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class MeshRender : MonoBehaviour
{
    private int frameIndex = 0;
    public int loadedFrames = 0;
    
    
    private float time = 0.03333f;

    [SerializeField] List<Mesh> meshList = new List<Mesh>();
    [SerializeField] List<Texture> materialList = new List<Texture>();

    Renderer rend;
    MeshFilter filter;

    public int objectReferenceScene = 0;




    void Start()
    {
        StartCoroutine(LoadFrames());

        gameObject.transform.localScale = new Vector3(0.0018f, 0.0018f, 0.0018f);

        StartCoroutine(MeshRendering());

    }

    
    void LoadByQuality(int depth, int frames, int i)
    {
        for (int f = i+1 ; f <= frames+i; f++)
        {
            string fileName = "Meshes/" + name + "/depth_" + depth + "/Stl/" + name + "_" + (f).ToString("D4");
            string fileTex = "Meshes/" + name + "/depth_" + depth + "/Stl/" + name + "_" + (f).ToString("D4") + "_tex";

            Texture loadedtexture = (Texture)Resources.Load(fileTex, typeof(Texture));
            Mesh loadedmesh = (Mesh)Resources.Load(fileName, typeof(Mesh));

            meshList.Add(loadedmesh);
            materialList.Add(loadedtexture);
        }
    }



    private IEnumerator LoadFrames()
    {
        string fileName = "Assets\\Files\\LoadConfiguration\\LoadConfig_" + tag +".cfg";
        StreamReader inp = new StreamReader(@fileName);



        while (!inp.EndOfStream)
        {
            var line = inp.ReadLine();
            var values = line.Split(' ');
            int frames = int.Parse(values[0]);
            int depth = int.Parse(values[1]);
            LoadByQuality(depth, frames, loadedFrames);
            loadedFrames += frames;

            yield return null;
        }
    }


    public IEnumerator MeshRendering(){

        rend = GetComponent<Renderer>();
        filter = GetComponent<MeshFilter>(); 

        while (true){
            if(ButtonObject.Instance.sceneIndex == objectReferenceScene){

                if(rend.isVisible){


                    //Forward play of the sequence 
                    if(frameIndex < loadedFrames){
                        rend.material.mainTexture = materialList[frameIndex];    
                        filter.sharedMesh = meshList[frameIndex];
                    }
                    //Backward play of the sequence 
                    else
                    {
                        rend.material.mainTexture = materialList[2 * loadedFrames - frameIndex -1];    
                        filter.sharedMesh = meshList[2 * loadedFrames - frameIndex - 1];                           
                    }
                                   
                }
                frameIndex ++;
                frameIndex = frameIndex % (2 * loadedFrames);
                yield return new WaitForSeconds(time); //0.03333f   
            }else{
                yield return null;
            }

        }
    }
}
