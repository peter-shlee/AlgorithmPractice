// https://www.acmicpc.net/problem/2178
// 미로 탐색

import java.util.*

val maze = mutableListOf<List<Int>>()
val distance = mutableListOf<MutableList<Int>>()

val adjacent = listOf(0 to 1, 1 to 0, -1 to 0, 0 to -1)

fun main() {
    input()
    solve()
    val distR = maze.size - 1
    val distC = maze[distR].size - 1
    println(distance[distR][distC])
}

fun input() {
    val reader = System.`in`.bufferedReader()
    val (n, m) = reader.readLine().split(" ").map { it.toInt() }
    for (i in 0 until n) {
        val tmpRow = reader.readLine().map { it.digitToInt() }
        maze.add(tmpRow)
        distance.add(MutableList(m) { -1 })
    }
}

fun solve() {
    val queue = LinkedList<Pair<Int, Int>>()
    queue.add(0 to 0)
    distance[0][0] = 1
    while (queue.isNotEmpty()) {
        val current = queue.poll()
        val r = current.first
        val c = current.second
        val nextDistance = distance[r][c] + 1

        for (index in adjacent) {
            val nextR = r + index.first
            val nextC = c + index.second
            if (!isValidIndex(nextR, nextC)) continue

            if (maze[nextR][nextC] != 1) continue
            if (distance[nextR][nextC] != -1) continue

            distance[nextR][nextC] = nextDistance
            queue.add(nextR to nextC)
        }
    }
}

fun isValidIndex(r: Int, c: Int): Boolean {
    if (r < 0 || c < 0) return false
    if (maze.size <= r) return false
    if (maze[r].size <= c) return false
    return true
}