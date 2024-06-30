const solution = (data) => {
	 let result=0.00;
	 const n=parseInt(data[0]);
	 const m=parseInt(data[1]);
	

	 let salt= parseFloat(n)*0.07;//소금의 양
	 let water_and_salt=parseFloat(m)+parseFloat(n);
	 const newSalt=(salt/water_and_salt)*100;
	 result=Math.floor(newSalt*100)/100;
	
	 //소금의양/기존 소금물의양+m양의 물

	 
	 return result.toFixed(2);
	 
	 
};

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on('line', function (line) {
  data = line.split(' ').map((el) => el);
  console.log(solution(data));
	rl.close();
});
