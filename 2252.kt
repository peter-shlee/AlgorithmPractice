import java.util.*

// 줄 세우기
// https://www.acmicpc.net/problem/2252

lateinit var outs: List<MutableSet<Int>>
lateinit var ins: MutableList<Int>
lateinit var check: MutableList<Boolean>
val notVisited = mutableSetOf<Int>()

fun main() {
    input()
    solve()
}

fun input() {
    val reader = System.`in`.bufferedReader()
    val (n, m) = reader.readLine().split(" ").map { it.toInt() }

    for (i in 1..n) {
        notVisited.add(i)
    }
    outs = List(n + 1) { mutableSetOf<Int>() }
    ins = MutableList(n + 1) { 0 }
    check = MutableList(n + 1) { false }

    for (i in 0 until m) {
        val (s, l) = reader.readLine().split(" ").map { it.toInt() }
        outs[s].add(l)
        ins[l] += 1
    }
}

fun solve() {
    val writer = System.out.bufferedWriter()
    var endFlag = false
    while(!endFlag && notVisited.isNotEmpty()) {
        val visited = mutableSetOf<Int>()
        endFlag = true
        for (i in notVisited) {
            if (ins[i] == 0) {
                visited.add(i)
                writer.write("$i ")
                endFlag = false
                for (next in outs[i]) {
                    ins[next] -= 1
                }
            }
        }

        for (i in visited) {
            notVisited.remove(i)
        }
    }

    for (i in notVisited) {
        writer.write("$i ")
    }
    writer.flush()
}
