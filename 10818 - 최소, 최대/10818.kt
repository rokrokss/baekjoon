import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val arr = br.readLines()[1].split(" ").map { it.toInt() }
    println("${arr.min()} ${arr.max()}")
}
