import java.util.*;

class Solution {
    public List solution(int start, int end) {
        //배열을 List로 바꾸기
        List<Integer> answer=new ArrayList<>();
        //List add매서드 호출하여 새로운 값 할당하기.
        for(int i=start;i<=end;i++)
        {
            answer.add(i);
        }
        return answer;
    }
}