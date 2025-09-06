def main():
    store ={"name":"sadid"}
    store["distance"] = 0.01
    store.update({"from":"mirpur"})

    print(creat_report(store))

def creat_report(store):
    return f"""
    Name: {store["name"]}
    Distance: {store.get("distance","unknown")} km
    From: {store["from"]}
    """
    



main()    