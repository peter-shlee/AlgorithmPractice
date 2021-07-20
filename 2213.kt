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

    val group = mutableSetOf<Int>()
    path(graph, weights, start, dp, group, -1, skipFlag)

    val writer = System.out.bufferedWriter()
    writer.write("$answer\n")
    val sortedGroup = group.toSortedSet()
    for (edge in sortedGroup) {
        writer.write("$edge ")
    }
    writer.write("\n")
    writer.flush()
}

fun input(): Pair<IntArray, Map<Int, MutableSet<Int>>> {
    val reader = System.`in`.bufferedReader()
    val delimiter = "\\s+".toRegex()
    val n = reader.readLine().trim().split(delimiter)[0].toInt()

    val weights = IntArray(n + 1) { 0 }
    reader.readLine().trim().split(delimiter).mapIndexed { index, s -> weights[index + 1] = s.toInt() }

    val graph = mutableMapOf<Int, MutableSet<Int>>()
    var edge: String?
    while (true) {
        edge = reader.readLine()
        if (edge == null) break

        val v = edge.trim().split(delimiter).map { it.toInt() }.toIntArray()

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

fun solve(
    graph: Map<Int, MutableSet<Int>>,
    weights: IntArray,
    edge: Int,
    dp: List<IntArray>,
    prev: Int,
    skipFlag: Int
): Int {
    if (dp[skipFlag][edge] != -1) return dp[skipFlag][edge]

    var nonSkipMaxValue = 0
    if (skipFlag == 0) {
        nonSkipMaxValue = weights[edge]
        for (nextEdge in graph[edge]!!) {
            if (nextEdge == prev) continue
            nonSkipMaxValue += solve(graph, weights, nextEdge, dp, edge, 1)
        }
    }

    var skipMaxValue = 0
    for (nextEdge in graph[edge]!!) {
        if (nextEdge == prev) continue
        skipMaxValue += solve(graph, weights, nextEdge, dp, edge, 0)
    }

    dp[skipFlag][edge] = max(skipMaxValue, nonSkipMaxValue)

    return dp[skipFlag][edge]
}

fun path(
    graph: Map<Int, MutableSet<Int>>,
    weights: IntArray,
    edge: Int,
    dp: List<IntArray>,
    group: MutableSet<Int>,
    prev: Int,
    skipFlag: Int
) {
    var nonSkipMaxValue = 0
    if (skipFlag == 0) {
        nonSkipMaxValue = weights[edge]
        for (nextEdge in graph[edge]!!) {
            if (nextEdge == prev) continue
            nonSkipMaxValue += solve(graph, weights, nextEdge, dp, edge, 1)
        }
    }

    var skipMaxValue = 0
    for (nextEdge in graph[edge]!!) {
        if (nextEdge == prev) continue
        skipMaxValue += solve(graph, weights, nextEdge, dp, edge, 0)
    }

    var nextFlag = 0
    if (nonSkipMaxValue > skipMaxValue) {
        group.add(edge)
        nextFlag = 1
    }

    for (nextEdge in graph[edge]!!) {
        if (nextEdge == prev) continue
        path(graph, weights, nextEdge, dp, group, edge, nextFlag)
    }
}