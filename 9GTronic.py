# msbnet.co.uk
import sys
import requests

if len(sys.argv) > 1:
    projectName = sys.argv[1]
    labPath = sys.argv[2]
else:
    print()
    print("USAGE: python " + sys.argv[0] + " <project name> <project path>")
    print()
    print("Example:  python " + sys.argv[0] + " iBGP /gns3labs/IBGP\ Internal\ BGP/")
    print()
    exit()

R1 = "Tulip"
R2 = "Rose"
R3 = "Lily"
R4 = "Blossom"

try:
    urlVer = f"http://localhost:3080/v2/version"
    srvCheckreq = requests.get(urlVer)
    srvCheckres = srvCheckreq.json()
    srvCheckresVer = srvCheckres["version"]
except:
    print("Unable to connect to GNS3 server at " + urlVer)
    print()
    exit() 

print()
print("GNS Server: " + srvCheckresVer)
print()
urlNodes = 'nodes'
urlProj = f"http://localhost:3080/v2/projects"
requestBodyProject = {"name": projectName}
requestProject = requests.post(urlProj, json = requestBodyProject)

if requestProject.status_code == 409:
    checkProject = requests.get(urlProj, json = {})
    checkProjectresponse = checkProject.json()
    ifexistProj = next(item for item in checkProjectresponse if item["name"] == projectName)
    projectId = ifexistProj["project_id"]
    urlq = f"http://127.0.0.1:3080/static/web-ui/server/1/project"f"/{projectId}"
    url0 = f"http://localhost:3080/v2/projects"f"/{projectId}"
    confirmDel = input("Project (" + urlq + ") already exists. DELETE? [Y/n] ")
    if confirmDel == '' or confirmDel.lower() == 'y' :
        print("Deleting... " + projectId)
        requests.delete(url0)
        requestProject = requests.post(urlProj, json = requestBodyProject)
        print()
    else:
        print("Exiting...")
        print()
        exit()

responseProject = requestProject.json()
projectId = responseProject["project_id"]

url1 = f"http://localhost:3080/v2/projects"f"/{projectId}"f"/{urlNodes}"
url2 = f"http://localhost:3080/v2/projects"f"/{projectId}"f"/links"
urlw = f"http://127.0.0.1:3080/static/web-ui/server/1/project"f"/{projectId}"
print("Created new project " + projectId)
print()
def newRouter(routername, x, y):
    rBody = {
    "symbol": ":/symbols/router.svg",
    "name": routername, "properties": {
        "platform": "c3600",
        "nvram": 256,
        "image": "C3640-JK.image",
        "ram": 192,
        "system_id": "FTX0945W0MY",
        "slot0": "NM-1FE-TX",
        "slot1": "NM-1FE-TX",
        "slot2": "NM-1FE-TX",
        "slot3": "NM-1FE-TX",
        "idlepc": "0x6050b114",
        "startup_config": labPath + routername + ".cfg"
    },
    "compute_id": "local",
    "node_type": "dynamips",
    "x": x,
    "y": y
    }
    request = requests.post(url1, json = rBody)
    response = request.json()
    nodeId = response["node_id"]
    startURL = f"http://localhost:3080/v2/projects"f"/{projectId}"f"/{urlNodes}"f"/{nodeId}"f"/start"
    requests.post(startURL)
    print("Started node " + nodeId)
    return(nodeId)

def link(nodeIdA, adapterA, nodeIdB, adapterB):
    linkRequest = {
        "nodes": [{
            "adapter_number": adapterA,
        "node_id": nodeIdA,
        "port_number": 0}, {
            "adapter_number": adapterB,
            "node_id": nodeIdB,
            "port_number": 0}]
            }
    requests.post(url2, json = linkRequest)
    print("Linked " + nodeIdA + " to " + nodeIdB)

nodeIdR1 = newRouter(R1, -150, -150)
nodeIdR2 = newRouter(R2, -150, 150)
nodeIdR3 = newRouter(R3, 150, -150)
nodeIdR4 = newRouter(R4, 150, 150)
print()
link(nodeIdR1, 0, nodeIdR3, 0)
link(nodeIdR1, 1, nodeIdR2, 0)
link(nodeIdR3, 1, nodeIdR4, 1)
link(nodeIdR2, 1, nodeIdR4, 0)
print()
print("Lab is now running in GNS3: " + urlw)
print()