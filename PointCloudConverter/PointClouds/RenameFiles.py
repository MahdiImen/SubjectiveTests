import os
 
# Function to rename multiple files
def main():
    print("Start")
    for pc in ["longdress", "loot", "redandblack", "soldier"]:
        src = f"8iVFBv2/{pc}/Ply/"
        print(pc)
        for count, filename in enumerate(os.listdir(src)):
            print(filename)
            c = count + 1 #file number starting from 1            
            k = (4 - len(str(c))) * '0'
            f = f"{pc}_{k}{str(c)}.ply"
            path = src + f
            os.rename(src + filename , path)

 
# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()