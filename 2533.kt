import java.util.*
import kotlin.math.min

// 사회망 서비스(SNS)
// https://www.acmicpc.net/problem/2533

lateinit var tree: List<MutableList<Int>>
lateinit var dp: List<MutableList<Int>>

fun main() {
    input()
    println(min(solve(1, -1, 0), solve(1, -1, 1)))
}

fun input() {
    val reader = Scanner(System.`in`)
    val n = reader.nextInt()
    tree = List(n + 1) { mutableListOf<Int>() }

    for (i in 0 until n - 1) {
        val a = reader.nextInt()
        val b = reader.nextInt()

        tree[a].add(b)
        tree[b].add(a)
    }

    dp = List(2) { MutableList(n + 1) { -1 } }
}

fun solve(index: Int, prev: Int, earlyAdapter: Int): Int {
    if (dp[earlyAdapter][index] != -1) {
        return dp[earlyAdapter][index]
    }

    var minValue = 0
    for (next in tree[index]) {
        if (next == prev) continue

        minValue += if (earlyAdapter == 1) {
            min(solve(next, index, 0), solve(next, index, 1))
        } else {
            solve(next, index, 1)
        }
    }

    if (earlyAdapter == 1) minValue += 1

    dp[earlyAdapter][index] = minValue

    return dp[earlyAdapter][index]
}
