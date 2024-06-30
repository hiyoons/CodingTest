// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

let data=[];
rl.on("line", function(line) {
	data.push(line);
}).on('close',function() {
	const T=parseInt(data[0],10);
	let answer=[];
	for(let i=1;i<=T;i++)
	{
		const [x,y,time]=data[i].split(' ').map(Number);
		const sum=Math.abs(x)+Math.abs(y);
		if(sum >time || (sum-time)%2!==0){
			answer.push('NO');
		} 
		else{ answer.push('YES');}
	}
	
	console.log(answer.join('\n'));
	process.exit(0);
});