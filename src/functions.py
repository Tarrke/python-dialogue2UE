from tkinter import Tk

def copyToClipboard(message):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(message)
    r.update()
    r.destroy()

def findLinksFromNode(data, sourceId):
    ids = []
    for connection in data["connections"]:
        # print(data["connections"][connection])
        if data["connections"][connection]["sourceid"] == sourceId:
            print("We have to make a link from " + sourceId + " to " + data["connections"][connection]["targetid"])
            ids.append(data["connections"][connection]["targetid"])
    return ids
