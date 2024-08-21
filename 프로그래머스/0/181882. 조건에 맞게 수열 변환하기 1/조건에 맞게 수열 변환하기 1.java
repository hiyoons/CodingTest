import java.util.*;
class Solution {
    public List solution(int[] arr) {
        List<Integer> answer=new ArrayList<>();
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i]%2==0&&arr[i]>=50)
                answer.add(arr[i]/2);
            else if(arr[i]%2!=0&&arr[i]<50)
                answer.add(arr[i]*2);
            else
                answer.add(arr[i]);
        }
        return answer;
    }
}