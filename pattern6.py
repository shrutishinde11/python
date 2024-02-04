row=8
for i in range(row,0,-1):
    for k in range(row-i):
        print(" " , end ="")
    for j in range(i):
        print("*", end=" ")
    print("")
for i in range(2, row+1):
    for k in range(row-i):
        print(" " , end ="")
    for j in range(i):
        print("*", end=" ")
    print("")


# * * * * * * * * 
#  * * * * * * *
#   * * * * * *
#    * * * * *
#     * * * *
#      * * *
#       * *
#        *
#       * *
#      * * *
#     * * * *
#    * * * * *
#   * * * * * *
#  * * * * * * *
# * * * * * * * * 