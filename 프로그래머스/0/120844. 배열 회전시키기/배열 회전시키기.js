function solution(numbers, direction) {
    var answer = [];
    let len=numbers.length;
    let i=0;
    if(direction==="right"){
 
        for(i=0;i<len-1;i++){
            answer[i+1]=numbers[i];
        }
        answer[0]=numbers[i];
    }
    else{
        for(i=0;i<len-1;i++){
            answer[i]=numbers[i+1];
        }
        answer[i]=numbers[0];
    }
    return answer;
}