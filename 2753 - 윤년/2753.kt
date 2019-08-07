import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    println(
            when ((n % 4 == 0 && n % 100 != 0) || n % 400 == 0) {
                true -> 1
                else -> 0
            }
    )
}
