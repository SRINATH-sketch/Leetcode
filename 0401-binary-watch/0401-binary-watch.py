class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        arr=[]
        leds=[1,2,4,8,1,2,4,8,16,32]

        def find(index,count,hours,minutes):
            if(index==10):
                if(count==turnedOn and hours<=11 and minutes<=59):
                    arr.append(f"{hours}:{minutes:02d}")
                return

            find(index+1,count,hours,minutes)

            if index<4:
                find(index+1,count+1,hours+leds[index],minutes)
            else:
                find(index+1,count+1,hours,minutes+leds[index])    
                
        find(0,0,0,0)
        return arr