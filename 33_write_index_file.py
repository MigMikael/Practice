"""
1,60,60
2,61,56
3,57,61
4,65,72
"""
data_path = "C:\\Users\\Mig\\Documents\\Thesis\\iPadMini4\\data_set\\resize_img\\"

with open(data_path + "start_index.txt", 'a') as txtfile:
    for i in range(103):
        line = str(i+1) + ",\n"
        txtfile.write(line)
    print("Finish")
