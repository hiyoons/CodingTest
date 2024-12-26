class Solution {
    public boolean solution(String s) {
      
        if (s.chars().allMatch(Character::isDigit)){
            if(s.length()==4 || s.length()==6)
                return true;
            else 
                return false;
        }
        else{
            return false;
        }    
    }
}