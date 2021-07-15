
import java.util.*
import kotlin.math.abs
import kotlin.math.min

// Dance Dance Revolution
// https://www.acmicpc.net/problem/2342

fun main() {
    val order = input()
    val dp = Array(5) { Array(5) { IntArray(order.size) { 0 } } }
    println(solve(order, dp, 0, 0, 0))
}

fun input(): ArrayList<Int> {
    val reader = Scanner(System.`in`)
    val order = arrayListOf<Int>()
    var n: Int

    while (true) {
        n = reader.nextInt()
        if (n == 0) break

        order.add(n)
    }

    return order
}

fun solve(
    order: ArrayList<Int>,
    dp: Array<Array<IntArray>>,
    index: Int,
    left: Int,
    right: Int
): Int {
    if (order.size <= index) return 0

    if (dp[left][right][index] != 0) return dp[left][right][index]

    val next = order[index]

    if (left == next || right == next) {
        dp[left][right][index] = solve(order, dp, index + 1, left, right) + 1
        return dp[left][right][index]
    }

    var cost = when (abs(left - next) % 2) {
        0 -> 4
        1 -> 3
        else -> 2
    }
    if (left == 0) cost = 2

    dp[left][right][index] = solve(order, dp, index + 1, next, right) + cost


    cost = when (abs(right - next) % 2) {
        0 -> 4
        1 -> 3
        else -> 2
    }
    if (right == 0) cost = 2

    dp[left][right][index] = min(dp[left][right][index], solve(order, dp, index + 1, left, next) + cost)

    return dp[left][right][index]
}