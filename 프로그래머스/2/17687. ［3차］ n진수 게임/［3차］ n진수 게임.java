import java.util.*;

class Solution {
   
    
    public String solution(int n, int t, int m, int p) {
        StringBuilder st = new StringBuilder();
        int num  = t*m;
        for(int i=0;st.length()<=num;++i){
            st.append(Integer.toString(i,n).toUpperCase());
        }
        
        String nw=st.toString();
        StringBuilder answer= new StringBuilder();
        
        for(int j=p-1;j<num;j+=m)
        {
            answer.append(nw.charAt(j));
        }
        
        return answer.toString();
    }
    
    
    
}