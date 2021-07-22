import java.util.*

// N과 M (9)
// https://www.acmicpc.net/problem/15663

var nums = mutableListOf<Int>()
lateinit var selected: BooleanArray
lateinit var list: IntArray

fun main() {
    val m = input()
    nums.sort()
    solve(m)
}

fun input(): Int{
    val reader = Scanner(System.`in`)
    val n = reader.nextInt()
    val m = reader.nextInt()

    for (i in 0 until n) {
        nums.add(reader.nextInt())
    }

    selected = BooleanArray(nums.size) { false }
    list = IntArray(m)

    return m
}

fun solve(depth: Int) {
    if (depth == 0) {
        for (n in list.reversed()) {
            print("$n ")
        }
        println()

        return
    }

    var prevNum = -1
    for (i in nums.indices) {
        if (selected[i]) continue

        if (nums[i] != prevNum) {
            prevNum = nums[i]
            selected[i] = true
            list[depth - 1] = nums[i]
            solve(depth - 1)
            selected[i] = false
        }
    }

    return
}