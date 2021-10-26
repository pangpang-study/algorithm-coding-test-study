fun main() {
    val ovens = mutableListOf<Int>()
    val pizzas = mutableListOf<Int>()

    val (n, d) = readLine()!!.split(" ").map { it.toInt() }
    ovens.addAll(readLine()!!.split(" ").map { it.toInt() })
    pizzas.addAll(readLine()!!.split(" ").map { it.toInt() })

    val dp = mutableListOf<Int>()
    var minimum = ovens.first()
    ovens.forEach {
        if (it >= minimum) dp.add(minimum)
        else {
            dp.add(it)
            minimum = it
        }
    }

    var lastPizza = n
    pizzas.forEach { pizza ->
        val position = dp.subList(0, lastPizza).indexOfLast { oven -> oven >= pizza }
        if (position < 0) {
            println(0)
            return
        }
        lastPizza = position
    }

    println(lastPizza + 1)
}
