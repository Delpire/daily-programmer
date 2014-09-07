function InitializeArray(){

	for( i = 0; i < pixel; i++){

		pixel_array[i] = [];

		for(j = 0; j < pixel; j++){
			pixel_array[i][j] = "";
		}
	}

}

function PrintArray(){

	for( i = 0; i < pixel; i++){
		
		str = "";

		for(j = 0; j < pixel; j++){
			str += pixel_array[j][i] + ' ';
		}

		console.log(str);
	}
}

function drawGrid(){
	
	var grid = document.getElementById("grid");
	var ctx=grid.getContext("2d");
	
		for (i = 0; i < pixel; i++) {
			
			for (j = 0; j < pixel; j++) {
				
				ctx.rect(i*5,j*5,5,5);
			
			}
		}
	
	ctx.fillStyle="#23332E";
	ctx.fill();
	ctx.lineWidth="1";
	ctx.strokeStyle = "grey";
	ctx.stroke();
}

function SplitQuadrant(start_x, end_x, start_y, end_y){
	
	var half_x = start_x + ((end_x - start_x) / 2)
	var half_y = start_y + ((end_y - start_y) / 2)

	for( i = start_x; i < end_x; i++){
		for(j = start_y; j < end_y; j++){
		
			if( i < half_x && j < half_y){
				pixel_array[i][j] += '2';
			}
			else if( i >= half_x && j < half_y){
				pixel_array[i][j] += '1';
			}
			else if( i < half_x && j >= half_y){
				pixel_array[i][j] += '3';
			}
			else{
				pixel_array[i][j] += '4';
			}
		}
	}

	if((end_x - start_x) / 2 == 1 || (end_y - start_y) / 2 == 1){
		return;
	}

	SplitQuadrant(start_x, half_x, start_y, half_y);
	SplitQuadrant(half_x, end_x, start_y, half_y);
	SplitQuadrant(start_x, half_x, half_y, end_y);
	SplitQuadrant(half_x, end_x, half_y, end_y);

}

$(function(){

	pixel = 8

	pixel_array = []

	InitializeArray();
	SplitQuadrant(0, pixel, 0, pixel);
	PrintArray();

})