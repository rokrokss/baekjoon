import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    MutableList<List<Int>>(br.readLine().toInt()) { br.readLine().split(' ').map { it.toInt() } }.sortedWith(compareBy({ it[1] }, { it[0] })).forEach { println("${it[0]} ${it[1]}") }
}

