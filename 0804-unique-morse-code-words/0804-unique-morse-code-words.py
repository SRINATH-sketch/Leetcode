class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        alphabet=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        arr=[]
        for i in words:
            word=[]
            for j in i:
                position=ord(j)-ord('a')
                word.append(alphabet[position])
            word="".join(word)
            arr.append(word)
        return len(set(arr))