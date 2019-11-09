let arr = [5,0,9,1,7,4,2,6,3,8];

let temp = 0;

function swap(x){
    temp = arr[x];
    arr[x] = arr[x+1];
    arr[x+1] = temp;
}

for (let j = 0; j < arr.length; j++) {
    for (let i = 0; i < (arr.length - 1 - j); i++) {
        if (arr[i] < arr[i+1]) {
            swap(i);
        };
    };
    console.log(arr);
};

console.log(arr);