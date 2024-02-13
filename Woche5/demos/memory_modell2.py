def main():
    def print_vars(p):
        output = f"Param = {p}"
        print(output)
        p.append("C")
        print(f"nach hinzufügen von C: Param = {p}")

    l = ["A", "B"]
    
    print_vars(l) 
    
    
    print(l)         

    l2 = ["Z", "Y"]

    print_vars(l2.copy())

    print(l2)
              
main() 