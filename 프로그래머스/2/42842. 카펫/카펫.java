class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {0,0};
        //넓이
        int area=brown+yellow;
        int width=0;
        int height=0;
        int wrap=0;
        //3이상
        for(int i=3;i<=area/2;i++){
            if(area%i==0)
            {
                height=i;
                width=area/i;
                //brown갯수가 감싸는 갯수와 동일하면
                wrap=width*2+2*(height-2);
                if(wrap==brown)
                    break;
            } 
        }
        
        answer[0]=width;
        answer[1]=height;
        return answer;
    }
}