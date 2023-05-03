import core

iterations=101
print("Summary of ",iterations," iterations")
#Board size
for j in range(8,9):
    W,B,D=0,0,0
    # file_name = "stats/max_max_"+str(j)+".txt"
    for i in range(1,iterations):
        file_name = "stats/max_morbius_"+str(j)+"_iteration_"+str(i)+".txt"
        # if i==99:
        #     win=core.play_game(j,True)
        # else:
        win=core.play_game(j,file_name,False,False)
        if win == "W":
            W+=1
        elif win == "B":
            B+=1
        else:
            D+=1
        # print(i," White: ",W," Black: ",B," Draw: ",D)
    print("Size: ",j, "White: ",W," Black: ",B," Draw: ",D)
