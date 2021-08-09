import java.util.*

// 멀티탭 스케줄링
// https://www.acmicpc.net/problem/1700

var n: Int = 0
var k: Int = 0
val items = mutableListOf<Int>()
val multiTab = hashSetOf<Int>()

fun main() {
    input()
    println(solve())
}

fun input() {
    val reader = Scanner(System.`in`)
    n = reader.nextInt()
    k = reader.nextInt()

    for (i in 0 until k) {
        items.add(reader.nextInt())
    }
}

fun solve(): Int {
    var answer = 0

    for ((index, item) in items.withIndex()) {
        if (item in multiTab) continue

        if (multiTab.size < n) {
            multiTab.add(item)
            continue
        }

        val remainItems = items.subList(index + 1, items.size)
        val nextMinOrder = mutableMapOf<Int, Int>()
        var targetTab = 0
        var maxOrder = -1
        for (tab in multiTab) {
            if (nextMinOrder[tab] == null) {
                nextMinOrder[tab] = remainItems.indexOf(tab)
            }
        }
        for ((key, value) in nextMinOrder) {
            if (value == -1) {
                targetTab = key
                break
            }
            if (value > maxOrder) {
                maxOrder = value
                targetTab = key
            }
        }
        multiTab.remove(targetTab)
        answer += 1
        multiTab.add(item)
    }

    return answer
}
