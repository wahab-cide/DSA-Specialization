//Linear Search
function linearSearch(arr, find)
{
    let arr_size = arr.length
    for(let i = 0; i < arr_size; i ++){
        if(arr[i] == find) return i
    }
    return -1
}


console.log(linearSearch([3, 5, 7, 19, 6], 7))

//Binary Search
function binary_search(sorted_arr, find)
{
    let low = 0, high = sorted_arr.length;
    while(high - low > 0) {
        mid_arr = Math.floor((low + high) / 2);
        if(find == sorted_arr[mid_arr])
            return mid_arr;

        if(find > sorted_arr[mid_arr])
            low = mid_arr + 1

        if(find < sorted_arr[mid_arr])
            high = mid_arr - 1
    }

    mid_arr = Math.floor((low + high) / 2);
    if(find == sorted_arr[mid_arr])
        return mid_arr;

    return -1;
}


//fibonacci search
function fibonacci_search(arr, find)
{
    let f0 = 0, f1 = 1, f2 = 2, start = -1;
    let size = arr.length;
    while(f2 < size) {
        f0 = f1;
        f1 = f2;
        f2 = f0 + f1;
    }

    while(f2 > 1) {
        let pos = Math.min(start + f0, size - 1);
        if(find > arr[pos]) {
            f2 = f1;
            f1 = f0;
            f0 = f2 - f1;
            start = pos;
        } else if(find < arr[pos]) {
            f2 = f0;
            f1 = f1 - f0;
            f0 = f2 - f1;
        } else {
            return pos;
        }
    }

    return -1;
}
