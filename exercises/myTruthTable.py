#!/usr/bin/env python3
#note: type in "chmod +x myTruthTable.py" to make self-executable

def myAND(in1_bool, in2_bool): #function to return the AND of two inputs
    #print("Input to AND: ",in1_bool, "::",in2_bool)

    return in1_bool and in2_bool
    #print("AND Result is: ", result)
#end of myAND()
def myOR(in1_bool, in2_bool): #function to return the OR of two inputs
    #print("Input to OR: ",in1_bool, "::",in2_bool)

    return in1_bool and in2_bool
    #print("OR Result is: ", result)
#end of myOR()
def main(): #driver function

    #establish some lists a data
    A_list = [True, True, False, False]
    B_list = [True, False, True, False]
    truth_dic = {}
    print("__AND Column__")

    for a in A_list:
        #print("My A_list term is: ",a)
        for b in B_list:
        #    print("My B_list term is: ",b)
            myANDOutput_bool = myAND(a, b)
            truth_dic[str(a)+" AND "+str(b)] = myANDOutput_bool


    for a in A_list:
    #print("My A_list term is: ",a)
        for b in B_list:
    #    print("My B_list term is: ",b)
            myOROutput_bool = myOR(a, b)
            truth_dic[str(a)+" OR "+str(b)] = myOROutput_bool
    for i in truth_dic:
        print("  ",i, ":", truth_dic[i])
    print("__OR Column__")
    print(" All finished!")
# end of main
main()
