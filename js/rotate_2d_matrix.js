function rotate_2d_matrix(matrix){
    //prints a rotated version of a matrix e.g [[1, 2, 3],[4, 5, 6],[7, 8, 9]] 
    //returns [[7, 4, 1],[8, 5, 2],[9, 6, 3]]
    let result = [];
    
    for(let i = 0; i<matrix.length; i++){
        result.push([]);
        for(let j = 0; j< matrix[i].length; j++){
            result[i][j] = matrix[j][i];
        }

        result[i].reverse();
    }
    console.log(result);

    return;
}

rotate_2d_matrix(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
);