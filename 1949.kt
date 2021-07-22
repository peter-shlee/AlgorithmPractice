import java.lang.Integer.max

// 우수 마을
// https://www.acmicpc.net/problem/1949

lateinit var graph: Map<Int, MutableSet<Int>>
lateinit var weights: List<Int>
lateinit var dp: List<IntArray>

fun main() {
    input()
    println(max(solve(0, -1, 1), solve(0, -1, 0)))
}

fun input() {
    val tmpGraph: MutableMap<Int, MutableSet<Int>> = mutableMapOf()
    val reader = System.`in`.bufferedReader()
    val n = reader.readLine().toInt()
    weights = reader.readLine().split(" ").map { it.toInt() }
    for (i in 0 until n - 1) {
        val edge = reader.readLine().split(" ").map { it.toInt() - 1 }
        if (tmpGraph[edge[0]] == null) {
            tmpGraph[edge[0]] = mutableSetOf()
        }
        tmpGraph[edge[0]]?.add(edge[1])

        if (tmpGraph[edge[1]] == null) {
            tmpGraph[edge[1]] = mutableSetOf()
        }
        tmpGraph[edge[1]]?.add(edge[0])
    }

    graph = tmpGraph

    dp = List(2) { IntArray(n) { -1 } }
}

fun solve(cur: Int, prev: Int, skip: Int): Int {
    if (dp[skip][cur] != -1) return dp[skip][cur]

    var maxValue = if (skip == 1) {
        0
    } else {
        weights[cur]
    }
    var value = 0
    graph[cur]?.let {
        for (next in it) {
            if (next == prev) continue

            value = if (skip == 1) {
                max(solve(next, cur, 0), solve(next, cur, 1))
            } else {
                solve(next, cur, 1)
            }

            maxValue += value
        }
    }

    dp[skip][cur] = maxValue

    return dp[skip][cur]
}
