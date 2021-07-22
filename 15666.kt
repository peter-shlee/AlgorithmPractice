// N과 M (12)
// https://www.acmicpc.net/problem/15666

import java.util.*

var nums = mutableListOf<Int>()
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
        if (depth < list.size && nums[i] < list[depth]) continue

        if (nums[i] != prevNum) {
            prevNum = nums[i]
            list[depth - 1] = nums[i]
            solve(depth - 1)
        }
    }

    return
}