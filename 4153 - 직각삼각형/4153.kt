import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    while (true) {
        val (a, b, c) = br.readLine().split(" ").map { it.toDouble() }
        if (a == 0.0 && b == 0.0 && c == 0.0)
            return;
        if (max(a, max(b, c)).pow(2) * 2 == a.pow(2) + b.pow(2) + c.pow(2))
            println("right")
        else
            println("wrong")
    }
}
