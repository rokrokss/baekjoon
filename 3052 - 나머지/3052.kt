import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val arr = br.readLines().map { it.toInt() }
    println("${arr.map { it % 42 }.toSet().size}")
}
