import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val n = br.readLine().toInt()
    val memo = Array(n + 1) { IntArray(10) }
    for (i in 0..9) memo[1][i] = 1
    for (i in 2..n)
        for (j in 0..9)
            for (k in 0..j)
                memo[i][j] = (memo[i][j] + memo[i-1][k]) % 10007
    var ans = 0
    for (i in 0..9)
        ans = (ans + memo[n][i]) % 10007
    println(ans)
}

