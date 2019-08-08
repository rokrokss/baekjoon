import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val arr = mutableListOf<String>()
    var cnt = 0

    fun f(from: Int, by: Int, to: Int, h: Int): Unit {
        cnt++;
        if (h == 1) {
            arr.add("${from} ${to}")
            return
        }
        f(from, to, by, h - 1)
        arr.add("${from} ${to}")
        f(by, from, to, h - 1)
    }

    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    f(1, 2, 3, n)
    println("${cnt}\n${arr.joinToString("\n")}")
}
