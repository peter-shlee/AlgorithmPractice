import java.util.*

// 트리 순회
// https://www.acmicpc.net/problem/1991

lateinit var tree: List<MutableList<Int>>

fun main() {
    input()
    solve()
}

fun input() {
    val reader = Scanner(System.`in`)
    val n = reader.nextInt()
    tree = List(n) { MutableList(2) { -1 } }

    for (i in 0 until n) {
        val node = reader.next()[0].toInt() - 'A'.toInt()
        val left = reader.next()[0]
        val right = reader.next()[0]

        if (left != '.') {
            tree[node][0] = left.toInt() - 'A'.toInt()
        }

        if (right != '.') {
            tree[node][1] = right.toInt() - 'A'.toInt()
        }
    }
}

fun solve() {
    preorder(0)
    println()
    inorder(0)
    println()
    postorder(0)
    println()
}

fun preorder(curNode: Int) {
    print((curNode + 'A'.toInt()).toChar())

    val left = tree[curNode][0]
    val right = tree[curNode][1]

    if (left != -1) {
        preorder(left)
    }

    if (right != -1) {
        preorder(right)
    }
}

fun inorder(curNode: Int) {
    val left = tree[curNode][0]
    val right = tree[curNode][1]

    if (left != -1) {
        inorder(left)
    }

    print((curNode + 'A'.toInt()).toChar())

    if (right != -1) {
        inorder(right)
    }
}

fun postorder(curNode: Int) {
    val left = tree[curNode][0]
    val right = tree[curNode][1]

    if (left != -1) {
        postorder(left)
    }

    if (right != -1) {
        postorder(right)
    }

    print((curNode + 'A'.toInt()).toChar())
}