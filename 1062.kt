import java.util.*
import kotlin.math.max

// 가르침
// https://www.acmicpc.net/problem/1062

lateinit var words: List<MutableSet<Char>>
var k: Int = 0
var answer = -1
val alphabets = hashSetOf<Char>()

fun main() {
    input()
    if (k < 5) {
        println(0)
    } else {
        solve()
        println(answer)
    }
}

fun input() {
    val reader = Scanner(System.`in`)
    val n = reader.nextInt()
    k = reader.nextInt()
    reader.nextLine()

    words = List(n) { mutableSetOf<Char>() }
    for (i in 0 until n) {
        val word = reader.nextLine()
        for (j in "anta".length until (word.length - "tica".length)) {
            val c = word[j]
            if (c !in "acint" && c !in words[i]) {
                words[i].add(c)
            }
        }
    }
}

fun solve() {
    combination('a')
}

fun combination(alphabet: Char) {
    if (alphabets.size == k - "acint".length) {
        var count = 0
        wordLoop@ for (word in words) {
            for (c in word) {
                if (c !in alphabets) continue@wordLoop
            }
            count += 1
        }
        answer = max(answer, count)
        return
    }

    if (alphabet > 'z') return
    if (alphabet in "acint") {
        combination(alphabet + 1)
        return
    }

    val nextAlphabet = alphabet + 1

    alphabets.add(alphabet)
    combination(nextAlphabet)
    alphabets.remove(alphabet)

    combination(nextAlphabet)
}