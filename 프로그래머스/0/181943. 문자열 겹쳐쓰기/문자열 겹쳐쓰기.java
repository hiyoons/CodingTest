class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        
        
        StringBuilder sb = new StringBuilder();
   
        int nx=0;
        int i=0;
         //인덱스 s전까지는 my_string
        for(i=0;i<s;i++){
            sb.append(my_string.charAt(i));
           
        }
        //현재 answer 글자 갯수 s-i개
        
        //인덱스 s부터 overwrite_string.length까지 
        for(int j=0;j<overwrite_string.length();j++)
        {
            sb.append(overwrite_string.charAt(j));            
        }
        
        //현재 answer 글자 갯수 s-i+overwrite_string.length() 
        
        for(int k=s+overwrite_string.length();k<my_string.length();k++)
        {
            sb.append(my_string.charAt(k));
        }
       
            
        String answer=sb.toString();
        return answer;
    }
}