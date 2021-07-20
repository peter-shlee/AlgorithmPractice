import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.max

// 트리의 독립집합
// https://www.acmicpc.net/problem/2213

fun main() {
    val (weights, graph) = input()
    val dp = List(2) { IntArray(weights.size) { -1 } }
    var answer = -1
    var start = -1
    var skipFlag = -1
    for (i in 1 until weights.size) {
        var tmpAnswer = solve(graph, weights, i, dp, -1, 1)
        if (answer < tmpAnswer) {
            start = i
            answer = tmpAnswer
            skipFlag = 1
        }
        tmpAnswer = solve(graph, weights, i, dp, -1, 0)
        if (answer < tmpAnswer) {
            start = i
            answer = tmpAnswer
            skipFlag = 0
        }
    }

//    val group = mutableSetOf<Int>()
//    path(graph, weights, start, dp, group, -1, skipFlag)
//
    println(answer)
//    println(group.toString())
//    for (d in dp) {
//        println(d.contentToString())
//    }
}

fun input(): Pair<IntArray, Map<Int, MutableSet<Int>>> {
    val reader = BufferedReader(InputStreamReader(System.`in`))
    val n = reader.readLine().toInt()

    val weights = IntArray(n + 1) { 0 }
    reader.readLine().split(" ").mapIndexed { index, s -> weights[index] = s.toInt() }

    val graph = mutableMapOf<Int, MutableSet<Int>>()
    var edge: String?
    while (true) {
        edge = reader.readLine()
        if (edge == null) break

        val v = edge.split(" ").map { it.toInt() }.toIntArray()

        if (graph[v[0]] == null) {
            graph[v[0]] = mutableSetOf()
        }
        graph[v[0]]?.add(v[1])

        if (graph[v[1]] == null) {
            graph[v[1]] = mutableSetOf()
        }
        graph[v[1]]?.add(v[0])
    }

    return Pair(weights, graph)
}

fun solve(graph: Map<Int, MutableSet<Int>>, weights: IntArray, edge: Int, dp: List<IntArray>, prev:Int, skipFlag: Int): Int {
    if (graph[edge] == null) return 0
    if (graph[edge]?.size == 0) return 0

    if (dp[skipFlag][edge] != -1) return dp[skipFlag][edge]

    var maxValue = if (skipFlag == 1) {
        0
    } else {
        weights[edge]
    }

    for (nextEdge in graph[edge]!!) {
        if (nextEdge == prev) continue

        if (skipFlag == 0) {
            maxValue = max(maxValue, solve(graph, weights, edge, dp, edge, 1) + weights[edge])
        }

        maxValue = max(maxValue, solve(graph, weights, edge, dp, edge, 0))
    }
    dp[skipFlag][edge] = maxValue

    return dp[skipFlag][edge]
}

fun path(graph: Map<Int, MutableSet<Int>>, weights: IntArray, edge: Int, dp: List<IntArray>, group: MutableSet<Int>, prev:Int, skipFlag: Int) {
    var next = -1
    var tmpValue: Int
    var nextSkipFlag = 0

    if (graph[edge]?.size == 0) return

    var maxValue = if (skipFlag == 1) {
        0
    } else {
        weights[edge]
    }

    for (nextEdge in graph[edge]!!) {
        if (nextEdge == prev) continue

        if (skipFlag == 0) {
            tmpValue = solve(graph, weights, edge, dp, edge, 1) + weights[edge]
            if (tmpValue > maxValue) {
                maxValue = tmpValue
                nextSkipFlag = 1
                next = nextEdge
            }
        }

        tmpValue = solve(graph, weights, edge, dp, edge, 0)
        if (tmpValue > maxValue) {
            maxValue = tmpValue
            nextSkipFlag = 0
            next = nextEdge
        }
    }

    if (next == -1) return

    path(graph, weights, next, dp, group, edge, nextSkipFlag)
}