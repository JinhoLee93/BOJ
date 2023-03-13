import Foundation

func solution(_ cap:Int, _ n:Int, _ deliveries:[Int], _ pickups:[Int]) -> Int64 {
    var res: Int64 = 0, len = deliveries.count
    
    var cur = 0, p = 0, d = 0
    for i in stride(from: len - 1, to: -1, by: -1) {
        var count = 0
        d -= deliveries[i]
        p -= pickups[i]

        while d < 0 || p < 0 {
            d += cap
            p += cap
            count += 1
        }    
        
        res += Int64((i + 1) * 2 * count)
    }
    
    return res
}