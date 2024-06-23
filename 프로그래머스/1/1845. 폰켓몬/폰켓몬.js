function solution(nums) {
    var answer = 0;
    let hashMap = new Map();
    let num_pick=nums.length/2;
    for(let i =0;i<nums.length;i++)
        {
            
            if(hashMap.has(nums[i])){
                
                hashMap.set(nums[i],hashMap.get(nums[i])+1);
                
            }
            else{
                hashMap.set(nums[i],1);
            }
            
            
        }
    //만약 hashMap의 size가 pick해야하는 개수와 같다 -> pick 출력
    //만약 hashMap의 size<num_pick: hashMapsize , size>num_pick: pick
    
    if(hashMap.size<num_pick){answer=hashMap.size;}
    else{answer=num_pick;}
    
    return answer;
}