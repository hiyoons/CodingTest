function solution(my_string) {
    var answer = '';
    for(let i=0;i<my_string.length;i++){
        let s=my_string.charAt(i);
        if(isUpperCase(s)){answer+=s.toLowerCase();}
        else{answer+=s.toUpperCase();}
    }
    return answer;
}

function isUpperCase(str){
    return str===str.toUpperCase();
}