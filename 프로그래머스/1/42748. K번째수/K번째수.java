import java.util.Arrays;
class Solution {
   

    public int[] solution(int[] array, int[][] commands) {
            int[] answer = new int[commands.length]; //배열 길이 정하기
    
            int k=0;
        
        
        for(int i=0;i<commands.length;i++)
        {
            int[] b= Arrays.copyOfRange(array,commands[i][0]-1,commands[i][1]);
            Arrays.sort(b);
            answer[k] = b[commands[i][2]-1];
            k++;
        }

        
        return answer;
    }
}