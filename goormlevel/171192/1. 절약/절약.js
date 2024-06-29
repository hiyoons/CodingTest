// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let n;
	let dt=[];
	for await (const line of rl) {
		const [info,cash]=line.split(" ");
		if(!n){
			n=line;
			continue;
		}
		else{
			dt.push([info,Number(cash)]);
		}
		if(!line) rl.close();
	}
	solution(dt);
	process.exit();
})();

function solution(dt){
	let totalcash=0;
	let result="success";
	for(let cmd of dt){
		if(cmd[0]=="in") totalcash+=cmd[1];
		else totalcash-=cmd[1];
		
		if(totalcash<0) result="fail";
	}
	
	
	console.log(result);
}