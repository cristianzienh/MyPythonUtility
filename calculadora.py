import sys

print("\nargs:", sys.argv[1], " ", sys.argv[2], " ", sys.argv[3])

operacao = sys.argv[1]

if (operacao == "+") :
    print("soma:", int(sys.argv[2]) + int(sys.argv[3])) 
elif (operacao == "-") :
    print("subtracao:", int(sys.argv[2]) - int(sys.argv[3]))     

