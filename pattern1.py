row = 5
for i in range(1, row+1):
    for k in range(row-i):
        print(" " , end =" ")
    for j in range(i):
        print("*", end=" ")
    print("")


#         * 
#       * *
#     * * *
#   * * * *
# * * * * *