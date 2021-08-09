import java.util.*

// 최소 스패닝 트리
// https://www.acmicpc.net/status?user_id=shlee4290&problem_id=1197&from_mine=1

val comparator = Comparator<Triple<Int, Int, Int>> { x, y -> x.first - y.first}
val heap = PriorityQueue(comparator)
val parent = IntArray(10000) { it }

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
        val parentOfA = findParent(a)
        val parentOfB = findParent(b)
        if (parentOfA == parentOfB) continue
        answer += c
        parent[parentOfB] = parentOfA
    }

    return answer
}

fun findParent(i: Int): Int {
    if (i == parent[i]) return i

    parent[i] = findParent(parent[i])
    return parent[i]
}