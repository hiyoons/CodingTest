import kotlin.math.sqrt

class Solution {
    
    fun countDiv(number: Int): Int {
        var result = 0
        val sqrt = sqrt(number.toDouble())
        
        for(i in 1 .. sqrt.toInt()) {
            if(number % i == 0) {
                result+=1
                if(number/i != i) {
                    result+=1
                }
            } 
        }
        
        return result
    }
    
    fun makeResult(number: Int, power: Int ,limit: Int): Int{
        if(number>limit){
            return power
        }
        else{
            return number
        }
    }
    
    fun solution(number: Int, limit: Int, power: Int): Int {
        var answer: Int = 0
        var numList = Array(number){i->countDiv(i+1)}
       
        for(i in 0 until numList.size) {
            answer+=makeResult(numList[i],power,limit)
        }
        
        
        return answer
    }
}