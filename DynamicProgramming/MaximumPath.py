def maxtw(a, ac, b, bc):
    if a > b:
        return ac
    return bc


def maxth(a, ac, b, bc, c, cc):
    if a > b:
        if a > c:
            return ac
        else:
            return cc
    elif b > c:
        return bc
    return cc


t = int(input())

while t > 0:
    n = int(input())
    temp1 = [int(i) for i in input().split()]
    val = []
    x = 0
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(temp1[x])
            x += 1
        val.append(temp)

    dp = [[0] * n] * n
    # print(dp)
    mc = -1
    # for c in range(n):
    #     dp[0][c] = val[0][c]
    dp[0] = val[0]
    print('after')
    print(dp)
    print('then')


    for r in range(1, n):
        temp = []
        for c in range(n):
            if c == 0:
                mc = maxtw(val[r - 1][c], c, val[r - 1][c + 1], c + 1)
                # dp[r][c] = val[r][c] + dp[r - 1][mc]
                temp.append(val[r][c] + dp[r - 1][mc])
                # print(dp)
            elif c == n - 1:
                mc = maxtw(val[r - 1][c], c, val[r - 1][c - 1], c - 1)
                # dp[r][c] = val[r][c] + dp[r - 1][mc]
                temp.append(val[r][c] + dp[r - 1][mc])
                # print(dp)
            else:
                mc = maxth(val[r - 1][c - 1], c - 1, val[r - 1][c], c, val[r - 1][c + 1], c + 1)
                # dp[r][c] = val[r][c] + dp[r - 1][mc]
                temp.append(val[r][c] + dp[r - 1][mc])
                # print(dp)
        dp[r] = temp
        print(dp)

    print(max(dp[n-1]))
    t -= 1
'''
1
4
7 5 9 3 4 8 2 6 1 7 3 9 5 2 1 6
Answer : 30
1
17
67 280 171 381 930 781 925 4 393 380 246 433 762 258 5 166 315 503 385 728 854 350 464 288 304 80 689 56 313 843 92 379 122 614 111 403 394 387 406 138 767 651 571 880 260 927 398 926 429 782 653 634 132 468 274 435 548 314 490 212 156 933 942 629 546 404 31 292 142 436 781 260 86 703 140 697 630 537 622 410 318 275 44 801 94 669 236 993 982 77 204 137 10 497 765 907 900 147 550 42 582 331 301 19 33 792 715 14 680 336 424 350 962 467 150 408 135 737 400 468 814 956 956 175 452 72 433 704 218 983 97 799 665 749 169 49 541 883 63 572 570 486 921 884 304 423 291 790 159 42 257 324 997 212 498 801 283 283 504 500 617 952 650 281 700 818 329 592 52 743 164 621 228 436 856 883 858 498 672 17 540 928 340 536 139 190 336 773 472 191 272 88 142 921 720 842 90 400 433 141 143 948 114 722 384 969 605 593 819 276 961 358 556 301 893 46 842 581 819 665 771 90 104 265 363 823 106 452 574 890 945 68 190 58 790 925 378 746 517 196 373 478 905 280 130 798 326 323 730 144 987 500 585 90 764 947 264 221 751 837 463 47 257 652 456 46 576 185 143 444 381 867 921 285 147 402 434 472 724 163 615 710 15 551 151 130 498 414 703
'''