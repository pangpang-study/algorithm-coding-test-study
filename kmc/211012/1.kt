val index = mutableMapOf<Int, String>()
val node = mutableMapOf<String, Int>()

fun main() {
    val n = readLine()!!.toInt()
    index[1] = "A"
    node["A"] = 1

    for (i in 1..n) {
        val input = readLine()!!.split(" ")
        val parent = node[input[0]]!!

        if (input[1] != ".") {
            index[parent * 2] = input[1]
            node[input[1]] = parent * 2
        }
        if (input[2] != ".") {
            index[parent * 2 + 1] = input[2]
            node[input[2]] = parent * 2 + 1
        }
    }

    pre(1)
    println()
    ino(1)
    println()
    pos(1)
}

fun pre(idx: Int) {
    print(index[idx])
    if (index[idx * 2] != null) pre(idx * 2)
    if (index[idx * 2 + 1] != null) pre(idx * 2 + 1)
}

fun ino(idx: Int) {
    if (index[idx * 2] != null) ino(idx * 2)
    print(index[idx])
    if (index[idx * 2 + 1] != null) ino(idx * 2 + 1)
}

fun pos(idx: Int) {
    if (index[idx * 2] != null) pos(idx * 2)
    if (index[idx * 2 + 1] != null) pos(idx * 2 + 1)
    print(index[idx])
}
