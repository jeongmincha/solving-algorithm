type Counter = {
    [k: number]: number;
};

class FindSumPairs {
    counter2Map: Counter;

    constructor(private nums1: number[], private nums2: number[]) {
        this.counter2Map = this.nums2.reduce((counterMap, num2) => {
            counterMap[num2] = (counterMap[num2] || 0) + 1;
            return counterMap;
        }, {} as Counter);
    }

    add(index: number, val: number): void {
        this.counter2Map[this.nums2[index]] -= 1;
        this.nums2[index] += val;
        this.counter2Map[this.nums2[index]] = (this.counter2Map[this.nums2[index]] || 0) + 1;
    }

    count(tot: number): number {
        let cnt = 0;

        for (const num1 of this.nums1) {
            cnt += this.counter2Map[tot - num1] ?? 0;
        }

        return cnt;
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * var obj = new FindSumPairs(nums1, nums2)
 * obj.add(index,val)
 * var param_2 = obj.count(tot)
 */

const findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
console.log(findSumPairs.count(7));
console.log(findSumPairs.add(3, 2));
console.log(findSumPairs.count(8));
console.log(findSumPairs.count(4));
console.log(findSumPairs.add(0, 1));
console.log(findSumPairs.add(1, 1));
console.log(findSumPairs.count(7));

export { }