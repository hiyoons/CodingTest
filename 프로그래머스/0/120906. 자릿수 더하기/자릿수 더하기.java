class Solution {
    public int solution(int n) {
        int answer = 0;
        String num=Integer.toString(n);
        for(int i=0;i<num.length();i++){
            char ch = num.charAt(i);
            answer+=Character.getNumericValue(ch);
        }
        return answer;
    }
}