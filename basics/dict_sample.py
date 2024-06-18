def main():
    addresses = {"Sawitzki": "München", "Meier": "Hamburg", "Schneider": "Berlin"}
    print(addresses["Sawitzki"])
    addresses["Musterfrau"] = "München"
    addresses["Sawitzki"] = "Rosenheim"
    print(addresses.values())    
    for key in addresses.keys():
        print(key)
    for values in addresses.values():
        print(values)
    for key in addresses:
        print(f"key={key}, value={addresses[key]}")

main()