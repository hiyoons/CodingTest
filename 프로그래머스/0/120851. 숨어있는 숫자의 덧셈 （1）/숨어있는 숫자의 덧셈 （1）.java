class Solution {
    public int solution(String my_string) {
        int answer = 0;
        for(int i=0;i<my_string.length();i++){
            if (my_string.charAt(i)=='1')
                answer+=1;
            else if(my_string.charAt(i)=='2')
                answer+=2;
            else if(my_string.charAt(i)=='3')
                answer+=3;
            else if(my_string.charAt(i)=='4')
                answer+=4;
            else if(my_string.charAt(i)=='5')
                answer+=5;
            else if(my_string.charAt(i)=='6')
                answer+=6;
            else if(my_string.charAt(i)=='7')
                answer+=7;
            else if(my_string.charAt(i)=='8')
                answer+=8;
            else if(my_string.charAt(i)=='9')
                answer+=9;
            else 
                answer+=0;
        }
        return answer;
    }
}