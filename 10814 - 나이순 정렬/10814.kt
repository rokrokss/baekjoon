import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    MutableList<String>(br.readLine().toInt()) { br.readLine() }.sortedWith(compareBy({ it.split(' ')[0].toInt() })).forEach { println(it) }
}

