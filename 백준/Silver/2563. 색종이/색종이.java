import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        boolean Paper[][] = new boolean[101][101];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int x1,y1;
        String current;

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int Area=0;

        for(int i=0;i<n;i++){
            current=br.readLine();
            x1 =Integer.parseInt(current.split(" ")[0]);
            y1 =Integer.parseInt(current.split(" ")[1]);

            for(int j=x1;j<x1+10;j++)
            {
                for(int k=y1;k<y1+10;k++){
                    Paper[j][k]=true;
                }
            }

        }

        for(int i=0;i<101;i++){
            for(int j=0;j<101;j++){
                if(Paper[i][j]==true)
                    Area++;
            }
        }

        bw.write(Area+"");
        bw.flush();
        bw.close();
        br.close();
        

    }
}