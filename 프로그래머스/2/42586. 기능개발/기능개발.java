import java.util.concurrent.ConcurrentHashMap;
import java.util.*;

class Solution {
    public static Queue<Integer> solution(int[] progresses, int[] speeds) {
            
            int last=0;//완성까지 남은 날
            ConcurrentHashMap<Integer,Integer> map=new ConcurrentHashMap<>();//day마다 배포되는 기능의 수
            Queue<Integer> q=new LinkedList<>();
            Integer key=0;

            for(int i=0;i<progresses.length;i++)
            {
                last=(int)Math.ceil((double)(100-progresses[i])/speeds[i]);
                System.out.println("----------------------------------------");
                System.out.println("현재"+i+"번쨰"+progresses[i]);
                if(map.isEmpty()){
                    //map
                   
                    map.put(last,1);
                    System.out.println("map이 새로 추가"+progresses[i]+" : "+ map.get(last));
                }
                else{
                    //day가 비어있지 않다면
                    //해당 기능이  map 있는 day보다 빨리 완성되는 건 불가능
                    //그렇다면 해당 day값을 key로 가지는 value가 증가
                
                    Iterator<Integer> keys = map.keySet().iterator();
                    
                    while (keys.hasNext()) {
                         key = keys.next();
                         if(last>key){
                            map.put(last,1);
                          
                            System.out.println("맵 상태");
                            System.out.println(map);
                            q.add(map.get(key));
                            map.remove(key);
                           
                           
                            break;
                            
                         }
                         else{
                            map.put(key,map.get(key)+1);//해당 map의 value값 증가
                            break;
                         }
                    }
                    //마지막 index는?
                   System.out.println(map);
                 
                }
                
            }
            if(map.get(key)==null){
                q.add(map.get(last));
            }
          else{
            q.add(map.get(key));
          }
            
          
          
            return q;
        }
}