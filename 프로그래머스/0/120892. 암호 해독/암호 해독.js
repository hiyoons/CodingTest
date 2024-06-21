function solution(cipher, code) {
    var answer = '';
    
    let i=code
    let cnt=1;
    let k=0; //접근 인덱스 값
    
    while(k<cipher.length){
        k=code*cnt-1;
        answer+=cipher.charAt(k);
        cnt+=1;
    }
    
    
    return answer;
}