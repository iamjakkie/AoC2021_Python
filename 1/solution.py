def calculateSlidingWindow(size=1):
    curr = prev = cnt = 0
    if(size==1):
        with open("/workspaces/AoC2021/1/input.txt") as input:
            for line in input:
                curr = int(line)
                if(prev):
                    if(curr > prev):
                        cnt+=1
                prev = curr
        return cnt
    else:
        window = []
        with open("/workspaces/AoC2021/1/input.txt") as input:
            for _ in range(size):
                val = int(input.readline())
                window.append(val)
                curr += val
            prev = curr
            for line in input:
                curr-=window.pop(0)
                val = int(line)
                window.append(val)
                curr+=val
                if(curr > prev):
                    cnt+=1
                prev = curr
        return cnt



def main():
    print(calculateSlidingWindow(3))

if __name__ == "__main__":
    main()