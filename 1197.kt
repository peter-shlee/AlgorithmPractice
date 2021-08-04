import java.util.*

val comparator = Comparator<Triple<Int, Int, Int>> { x, y -> x.first - y.first}
val heap = PriorityQueue(comparator)
val visited = BooleanArray(10000) { false }
val graph = List(10000) { mutableSetOf<Int>()}

fun main() {
    input()
    println(solve())
}

fun input() {
    val reader = System.`in`.bufferedReader()
    val (v, e) = reader.readLine().split(" ").map { it.toInt() }
    for (i in 0 until e) {
        val (a, b, c) = reader.readLine().split(" ").map { it.toInt() }
        heap.add(Triple(c, a - 1, b - 1))
    }
}

fun solve(): Int {
    var answer = 0

    while(heap.isNotEmpty()) {
        val (c, a, b) = heap.poll()
        if (visited[a] && visited[b]) {
            println("check")
            if (loopCheck(a, b, mutableSetOf())) continue
            println("end")
        }
        println("$c $a $b")
        answer += c
        visited[a] = true
        visited[b] = true
        graph[a].add(b)
        graph[b].add(a)
    }

    return answer
}

fun loopCheck(current: Int, prev: Int, loopVisited: MutableSet<Int>): Boolean {
    loopVisited.add(current)
    for (next in graph[current]) {
        if (prev == next) continue
        if (loopVisited.contains(next)) return true
        if (loopCheck(next, current, loopVisited)) return true
    }

    return false
}