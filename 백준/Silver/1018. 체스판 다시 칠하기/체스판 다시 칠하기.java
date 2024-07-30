import java.util.*;

public class Main {
    public static  int getMinmum(int startRow, int startCol,String[] board){
        String[] diffBoard={"WBWBWBWB","BWBWBWBW"};
        int whitecnt=0;
        for(int i=0;i<8;i++){
            int row = startRow+i;
            for(int j=0;j<8;j++)

            {
                int col = startCol+j;
                if (board[row].charAt(col)!= diffBoard[row%2].charAt(j)) whitecnt++;}
        }
        return Math.min(whitecnt,64-whitecnt);
    }

    public static void main(String[] args)  {
       Scanner sc= new Scanner(System.in);

       int row = sc.nextInt();
       int col = sc.nextInt();
        String[] board=new String[row];
      sc.nextLine();

       for (int i=0;i<row;i++){
           board[i]=sc.nextLine();
       }

       int sol = Integer.MAX_VALUE;

       for(int i=0;i<=row-8;i++){
           for(int j=0;j<=col-8;j++){
               int curSol=getMinmum(i,j,board);
               if(sol>curSol) sol=curSol;

           }
       }

       System.out.println(sol);
       sc.close();
    }
}
