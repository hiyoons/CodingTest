class Solution {
    public int solution(String my_string, String is_suffix) {
        int answer = 0;
        int lenMy=my_string.length();
        
        if(lenMy<is_suffix.length()) return answer;
        
        for(int i=is_suffix.length()-1;i>=0;i--){
            if(my_string.charAt(lenMy-1)==is_suffix.charAt(i))
                answer=1;
            else
                return 0;
            lenMy-=1;
        }
        return answer;
    }
}