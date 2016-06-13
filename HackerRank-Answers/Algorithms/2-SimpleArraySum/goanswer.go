package main
import "fmt"
import "os"
import "bufio"

func main() {
    var n, total int
    io := bufio.NewReader(os.Stdin)
    fmt.Fscan(io, &n)

    arr := make([]int, n)
    
    for i := 0; i < n; i++ {
        fmt.Fscan(io, &arr[i])
    }
    for i := 0; i < len(arr); i++ {
        total += arr[i]
    }
    fmt.Println(total)
}