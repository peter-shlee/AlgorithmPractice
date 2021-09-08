// https://www.acmicpc.net/problem/6593
// 상범 빌딩

import java.util.*

val reader = System.`in`.bufferedReader()
val building = mutableListOf<List<String>>()
val visited = mutableListOf<List<MutableList<Int>>>()
var start = Triple(-1, -1, -1)
var end = Triple(-1, -1, -1)
var invalid = Triple(-1, -1, -1)

val adjacent =
    listOf(
        Triple(1, 0, 0),
        Triple(-1, 0, 0),
        Triple(0, 1, 0),
        Triple(0, -1, 0),
        Triple(0, 0, 1),
        Triple(0, 0, -1)
    )

fun main() {
    while (input()) {
        if (start == invalid || end == invalid) {
            println("Trapped!")
        } else {
            solve()
        }
        building.clear()
        visited.clear()
        start = invalid
        end = invalid
    }
}

fun input(): Boolean {
    val (l, r, c) = reader.readLine().split(" ").map { it.toInt() }
    if (l == 0 && r == 0 && c == 0) return false
    for (i in 0 until l) {
        val floor = mutableListOf<String>()
        val floorVisited = mutableListOf<MutableList<Int>>()
        for (j in 0 until r) {
            val row = reader.readLine()
            floor.add(row)
            floorVisited.add(MutableList(c) { -1 })

            row.mapIndexed { index, ch ->
                if (ch == 'S') {
                    start = Triple(i, j, index)
                } else if (ch == 'E') {
                    end = Triple(i, j, index)
                }
            }
        }
        building.add(floor)
        visited.add(floorVisited)
        reader.readLine()
    }

    return true
}

fun solve() {
    val queue = LinkedList<Triple<Int, Int, Int>>()
    queue.add(start)
    visited[start.first][start.second][start.third] = 0
    while (queue.isNotEmpty()) {
        val current = queue.poll()
        val nextDistance = visited[current.first][current.second][current.third] + 1

        for (index in adjacent) {
            val f = current.first + index.first
            val r = current.second + index.second
            val c = current.third + index.third

            if (!isValidIndex(f, r, c)) continue
            if (building[f][r][c] == '#') continue
            if (visited[f][r][c] != -1) continue

            visited[f][r][c] = nextDistance
            queue.add(Triple(f, r, c))
        }
    }

    val answer = visited[end.first][end.second][end.third]
    if (answer == -1) println("Trapped!")
    else println("Escaped in $answer minute(s).")
}

fun isValidIndex(f: Int, r: Int, c: Int): Boolean {
    if (f < 0 || r < 0 || c < 0) return false
    if (building.size <= f) return false
    if (building[f].size <= r) return false
    if (building[f][r].length <= c) return false
    return true
}