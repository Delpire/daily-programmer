board = [];
		colorArray = [ "#23332E", "#F0F5F5", "#62062B", "#DAB42B", "#FB223F", "#4B796F", "#C4B999" ];
		colors = [ ];
		colorDir = [ ];
		directions = [ "N", "E", "S", "W" ];
		ant = { x:60, y:75, direction:0 };
		isDone = false;
		
		function drawGrid(){
			var grid = document.getElementById("grid");
			
			var ctx=grid.getContext("2d");
			
			for (i = 0; i < 200; i++) { 
				
				board[i] = [];
				
				for (j = 0; j < 200; j++) {
					board[i][j] = 0;
					ctx.rect(i*5,j*5,5,5);
				}
			}
			
			ctx.fillStyle="#23332E";
			ctx.fill();
			ctx.lineWidth="1";
			ctx.strokeStyle = "grey";
			ctx.stroke();
		}
		
		function run(){
		
			var grid = document.getElementById("grid");
			
			var ctx=grid.getContext("2d");
			
		
			for(i = 0; i < ticks; i++){
			
				//setTimeout(function(){
				
				if(isDone || ant.x < 0 || ant.y < 0){
					isDone = true;
					break;
				}
				
				color = board[ant.x][ant.y];
				newColor = colors[(color + 1) % colors.length];
				board[ant.x][ant.y] = (color + 1) % colors.length;
				dir = colorDir[color];
				ant.direction = (ant.direction + dir + 4) % 4;
				if(directions[ant.direction] == "N")
					ant.x = ant.x - 1;
				else if(directions[ant.direction] == "E")
					ant.y = ant.y + 1;
				else if(directions[ant.direction] == "S")
					ant.x = ant.x + 1;
				else
					ant.y = ant.y - 1;
				//}, speed * i);
			}
			
			for (i = 0; i < 200; i++) { 
				
				for (j = 0; j < 200; j++) {
					ctx.beginPath();
					ctx.rect(j*5,i*5,5,5);
					ctx.fillStyle= colorArray[board[i][j]];
					ctx.lineWidth="1";
					ctx.fill();
					ctx.strokeStyle = "grey";
					ctx.stroke();
				}
			}
			
		}
		
		function newRun(){
			
			isDone = true;
			
			pattern = document.getElementById("pattern").value;
			ticks = document.getElementById("ticks").value;
			speed = document.getElementById("speed").value;
			
			drawGrid();
			
			colors = [ ];
			colorDir = [ ];
		
			var index = 0;
		
			for(index = 0; index < pattern.length; index++) {
				if(pattern[index] == "L")
					colorDir.push(-1);
				else
					colorDir.push(1);
				
				colors.push(colorArray[index]);

			}
			
			isDone = false;
			run();
		
		}