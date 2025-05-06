class Solution {
    
    fun solution(k: Int, m: Int, score: IntArray): Int {
        var answer: Int = 0
        var score = score.sortedArray()
        var boxcnt = score.size / m
        var scoreList = score.toMutableList()
        for (i in 0 until boxcnt) {
            var apples : MutableList<Int> = ArrayList()
            for(j in 0 until m) {
                apples.add(scoreList.removeAt(scoreList.size -1))
            }
            val minimal = apples.minOrNull()
            if (minimal != null) {
                answer  += minimal * m
            }
           
        }
        
        return answer
    }
}