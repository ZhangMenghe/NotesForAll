/************************
Prefab
************************/
Instantiate(prefabTransform, Vector3 position, Quaternion rotation);
/************************
switch
************************/
switch (spawnSequence)
{
    case 0://lock
    dosomething();
    break;
}
/************************
outside variable
************************/
public gameController gameControllerScript;
void start(){
	GameObject Controller = GameObject.Find("Controller");
    gameControllerScript = Controller.GetComponent<gameController>();
    gameControllerScript.variableName = asdfasdfa;//must be public
}