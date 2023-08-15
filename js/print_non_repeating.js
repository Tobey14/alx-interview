//prints non repeating 2 digit numbers from an array ['0', '1', '2'] gives 01, 02, 12 and so forth
function multiple(arr){
    for(let i = 0; i<arr.length; i++){
        for(let j = i + 1; j< arr.length; j++){
            console.log(arr[i]+arr[j]);
        }
    }

    return;
}

multiple(['0','1', '2', '3', '4', '5']);