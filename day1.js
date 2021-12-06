function countIncreases(str) {
    let arr = str.split("\n");
    let count = 0;
    for (let i = 1; i < arr.length - 1; i++) {
        if (arr[i] > arr[i - 1]) {
            count++;
        }
    }
    console.log(count);
}

let str = window.prompt("Enter input: ");