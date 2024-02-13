def main():
    def print_reference(p):
        output = f"Param = {p}"
        print(output)
        p.append("C")
        print(f"nach hinzufügen von C: Param = {p}")

    l = ["A", "B"]
    
    print_reference(l) 
   
    
    print(l)         


main() 