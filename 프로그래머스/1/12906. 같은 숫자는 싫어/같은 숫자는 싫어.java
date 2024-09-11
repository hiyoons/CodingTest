import java.util.*;

public class Solution {
    
    public int[] solution(int []arr) {
        Vector<Integer> stk=new Vector<>();
        int num=-1;
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i]!=num)
                stk.add(arr[i]);
            num=arr[i];
        }
        Integer[] before=new Integer[stk.size()];
        before=stk.toArray(before);
        int[] answer=java.util.Arrays.stream(before).mapToInt(Integer::intValue).toArray();
        return answer;
    }
}