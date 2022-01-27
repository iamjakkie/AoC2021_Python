def main():
    horizontal = aim = depth = 0
    with open("/workspaces/AoC2021/2/input.txt") as input:
        for line in input:
            order,val = line.replace('\n','').split(' ')
            val = int(val)
            if(order == "forward"):
                horizontal+=val
                depth+=aim*val
            elif(order == "up"):
                aim-=val
            elif(order == "down"):
                aim+=val
    print(str(horizontal*depth))

if __name__ == "__main__":
    main()