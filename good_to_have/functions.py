def getInputBetween(startval: int,endval: int)->int: 
    while True: 
        try: 
            val=int(input("Mata in:")) 
            if val >= startval and val <= endval: 
                return val 
            print(f"Ogiltigt val, mellan {startval} och {endval}, tack") 
        except: 
            print("Ange ett tal tack!")
    

# main nedan gör att koden endast köras
# om den ligger i samma fil,
# inte om den importeras.
if __name__ == "__main__":
    print("Testing")
    x = getInputBetween(100, 200)
    print(x)


def getBestPlayer()->str:
    return "Mats Sundin"