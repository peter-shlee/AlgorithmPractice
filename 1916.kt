import java.util.*
import kotlin.collections.HashSet

// 최소비용 구하기
// https://www.acmicpc.net/problem/1916

var n = 0
var m = 0
var bus = MutableList(1000 + 1) { MutableList(1000 + 1) { -1 } }
var start = 0
var dest = 0
var cost = MutableList(1000 + 1) { 987654321 }

fun main() {
    input()
    solve()
    println(cost[dest])
}

fun input() {
    val reader = Scanner(System.`in`)
    n = reader.nextInt()
    m = reader.nextInt()

    for (i in 0 until m) {
        val s = reader.nextInt()
        val d = reader.nextInt()
        val p = reader.nextInt()
        if (p < bus[s][d] || bus[s][d] == -1) {
            bus[s][d] = p
        }
    }
    start = reader.nextInt()
    dest = reader.nextInt()
}

fun solve() {
    var current = start
    cost[current] = 0
    while (true) {
        if (current == dest) break

        for ((next, price) in bus[current].withIndex()) {
            if (price == -1) continue

            val nextCost = price + cost[current]
            if (nextCost < cost[next]) {
                cost[next] = nextCost
            }
        }

        cost[current] = -1
        var nextMin = 987654321
        cost.mapIndexed { index, i ->
            if (i != -1 && i < nextMin) {
                nextMin = i
                current = index
            }
        }
    }
}