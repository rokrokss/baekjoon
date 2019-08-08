import java.io.BufferedReader
import java.io.InputStreamReader

fun f(n: Int): Int = if (n <= 1) 1 else n * f(n - 1)

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt();
    println(f(n))
}
