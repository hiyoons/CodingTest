import java.util.Stack;

class Solution {
    boolean solution(String s) {
        boolean answer=true;
        
        Stack<String> sk=new Stack<>();
        for(int i=0;i<s.length();i++){
           if(s.charAt(i)=='('){
               sk.push(Character.toString(s.charAt(i)));
               answer=true;
           }
            else{
                if(sk.isEmpty()|| sk.pop()==Character.toString(s.charAt(i)))
                    return false;
            }
        }

        return sk.isEmpty();
    }
}