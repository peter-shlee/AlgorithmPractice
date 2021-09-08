// https://www.acmicpc.net/problem/2644
// 촌수 계산

import java.util.*

var start = 0
var dest = 0
var tree: MutableList<MutableList<Int>>? = null
var visited: MutableList<Int>? = null

fun main() {
    input()
    solve()
    println(visited?.get(dest))
}

fun input() {
    val reader = System.`in`.bufferedReader()
    val n = reader.readLine().toInt()
    tree = MutableList(n + 1) { mutableListOf() }
    visited = MutableList(n + 1) { -1 }
    val (a, b) = reader.readLine().split(" ").map { it.toInt() }
    start = a
    dest = b
    val m = reader.readLine().toInt()
    for (i in 0 until m) {
        val (aa, bb) = reader.readLine().split(" ").map { it.toInt() }
        tree?.let {
            it[aa].add(bb)
            it[bb].add(aa)
        }
    }
}

fun solve() {
    val queue = LinkedList<Int>()
    queue.add(start)
    visited?.let {
        it[start] = 0
    }
    loop1@ while (queue.isNotEmpty()) {
        val current = queue.poll()
        for (next in tree?.get(current) ?: return) {
            if (visited?.get(next) != -1) continue

            visited?.let { visited ->
                visited[next] = visited[current] + 1
            }

            if (next == dest) {
                break@loop1
            }

            queue.add(next)
        }
    }
}