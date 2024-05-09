class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String s1=myString.toUpperCase();
        String s2=pat.toUpperCase();
        if(s1.contains(s2)) answer=1;
        return answer;
    }
}