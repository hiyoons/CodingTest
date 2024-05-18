class Solution {
    public int solution(String s) {

        StringBuilder sb = new StringBuilder();
        for (int i=0;i<s.length();i++){
            char ck=s.charAt(i);
            switch(ck){
                case 'o':
                    sb.append(1);
                    i+=2;
                    break;
                case 's':
                    if (s.charAt(i+1)=='e')
                    {
                        sb.append(7);
                        i+=4;
                    }
                    else
                    {
                        sb.append(6);
                        i+=2;
                    }
                    break;
                case 't':
                    if(s.charAt(i+1)=='w'){
                        sb.append(2);
                        i+=2;
                    }
                    else{
                        sb.append(3);
                        i+=4;
                    }
                    break;
                case 'f':
                    if(s.charAt(i+1)=='o'){
                        sb.append(4);

                    }
                    else{
                        sb.append(5);
                    }
                    i+=3;
                    break;
                case 'e':
                    sb.append(8);
                    i+=4;
                    break;
                case 'n':
                    sb.append(9);
                    i+=3;
                    break;
                case 'z':
                    sb.append(0);
                    i+=3;
                    break;
                default:
                    sb.append(ck);
                    break;
            }}




        return  Integer.parseInt(sb.toString());

    }

}