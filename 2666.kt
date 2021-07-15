import java.lang.Integer.min
import java.util.*
import kotlin.math.abs

// 벽장문의 이동
// https://www.acmicpc.net/problem/2666

fun main() {
    val (numOfClosets, openedDoors, order) = input()
    val dp = Array(order.size) { Array(numOfClosets + 1) { IntArray(numOfClosets + 1) { -1 } } }

    println(solve(openedDoors[0], openedDoors[1], order, 0, dp))
}

fun input(): Triple<Int, IntArray, IntArray> {
    val reader = Scanner(System.`in`)
    val numOfClosets = reader.nextInt()
    val openedDoors = intArrayOf(reader.nextInt(), reader.nextInt())
    val n = reader.nextInt()
    val order = IntArray(n) { 0 }
    for (i in 0 until n)
        order[i] = reader.nextInt()

    return Triple(numOfClosets, openedDoors, order)
}

fun solve(
    open1: Int,
    open2: Int,
    order: IntArray,
    currentIndex: Int,
    dp: Array<Array<IntArray>>
): Int {
    if (currentIndex == order.size) {
        return 0
    }

    val dest = order[currentIndex]

    if (dp[currentIndex][open1][open2] != -1) return dp[currentIndex][open1][open2]
    else if (dp[currentIndex][open2][open1] != -1) return dp[currentIndex][open2][open1]

    dp[currentIndex][open1][open2] = min(
        solve(dest, open2, order, currentIndex + 1, dp) + abs(dest - open1),
        solve(open1, dest, order, currentIndex + 1, dp) + abs(dest - open2)
    )
    dp[currentIndex][open2][open1] = dp[currentIndex][open1][open2]

    return dp[currentIndex][open1][open2]
}