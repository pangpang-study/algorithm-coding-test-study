val memMap = mutableMapOf<Int, Int>()

fun main() {
    val n = readLine()!!.toInt()
    val m = readLine()!!.toInt()
    var fixedSeat = mutableListOf<Int>()
    for (i in 1..m) {
        fixedSeat.add(readLine()!!.toInt())
    }
    fixedSeat.add(n + 1)

    memMap[1] = 1
    memMap[2] = 2

    var result = 1
    var idx = 1

    fixedSeat.forEach {
        val len = it - idx
        if (len > 0)
            result *= recursive(len)
        idx = it + 1
    }

    println(result)
}

fun recursive(idx: Int): Int {
    return if (memMap[idx] != null) memMap[idx]!!
    else {
        memMap[idx] = recursive(idx - 1) + recursive(idx - 2)
        memMap[idx]!!
    }
}
