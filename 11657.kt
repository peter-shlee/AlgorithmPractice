import java.lang.Integer.min

// 타임머신
// https://www.acmicpc.net/problem/11657

const val INF = 987654321
const val INF_L = 9876543210L
val roads = Array(501) { IntArray(501) { INF } }
val costs = LongArray(501) { INF_L }
var n = 0

fun main() {
    input()
    solve()
}

fun input() {
    val reader = System.`in`.bufferedReader()
    val (_n, m) = reader.readLine().split(" ").map { it.toInt() }
    n = _n

    for (i in 0 until m) {
        val (a, b, c) = reader.readLine().split(" ").map { it.toInt() }
        roads[a][b] = min(roads[a][b], c)
    }
}

fun solve() {
    costs[1] = 0
    var last = 0
    val writer = System.out.bufferedWriter()

    for (i in 1..n) {
        var changed = false

        for (a in 1..n) {
            for (b in 1..n) {
                if (costs[a] == INF_L) continue
                val costAB = roads[a][b]
                if (costAB != INF) {
                    if (costs[a] + costAB < costs[b]) {
                        costs[b] = costs[a] + costAB
                        changed = true
                    }
                }
            }
        }

        if (!changed) {
            break
        } else {
            last = i
        }
    }

    if (last == n) {
        writer.write("-1\n")
    } else {
        for (i in 2..n) {
            if (costs[i] == INF_L) {
                writer.write("-1\n")
            } else {
                writer.write("${costs[i]}\n")
            }
        }
    }
    writer.flush()
}