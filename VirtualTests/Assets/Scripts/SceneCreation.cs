using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class SceneCreation : MonoBehaviour {
    public string sceneName = "scene_1";
    GameObject obj;

    private void Start() {
        //QualitySettings.vSyncCount = 0;
        //Application.targetFrameRate = 30;
        string fileName = "Assets\\Files\\SceneConfiguration\\" + sceneName + ".cfg";
        StreamReader inp = new StreamReader(@fileName);
        Screen.SetResolution(1832, 1920, true);
        while (!inp.EndOfStream) {
            var line = inp.ReadLine();
            var values = line.Split(' ');
            string name = values[0];
            int px = int.Parse(values[1]);
            int py = int.Parse(values[2]);
            int pz = int.Parse(values[3]);
            float rx = float.Parse(values[4]);
            float ry = float.Parse(values[5]);
            float rz = float.Parse(values[6]);
            obj = GameObject.FindWithTag(name);
            obj.transform.position= new Vector3(px, py, pz);
            Vector3 rotation = new Vector3(rx, ry, rz);
            obj.transform.rotation = Quaternion.Euler(rotation);
        }
    }

}
