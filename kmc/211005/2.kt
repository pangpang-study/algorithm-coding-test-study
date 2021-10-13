import java.util.LinkedList
import java.util.Queue

fun main() {
    val (n, t, g) = readLine()!!.split(" ").map { it.toInt() }
    var memSet = mutableSetOf<Int>()
    memSet.add(n)
    val queue: Queue<Pair<Int, Int>> = LinkedList()
    queue.add(Pair(n, 0))

    if (n == g) {
        println(0)
        return
    }

    while (queue.isNotEmpty()) {
        val (cur, cnt) = queue.poll()
        if (cnt == t) break

        val nextA =
            if (cur >= 99999) -1
            else cur + 1
        val nextB = cur.let {
            var result = it * 2
            if (result > 99999) {
                -1
            } else {
                if (result >= 10000) result -= 10000
                else if (result >= 1000) result -= 1000
                else if (result >= 100) result -= 100
                else if (result >= 10) result -= 10
                else if (result >= 1) result -= 1

                result
            }
        }

        if (nextA == g || nextB == g) {
            println(cnt + 1)
            return
        } else {
            if (nextA > 0 && !memSet.contains(nextA)) {
                memSet.add(nextA)
                queue.add(Pair(nextA, cnt + 1))
            }
            if (nextB > 0 && !memSet.contains(nextB)) {
                memSet.add(nextB)
                queue.add(Pair(nextB, cnt + 1))
            }
        }
    }

    println("ANG")
    return
}
