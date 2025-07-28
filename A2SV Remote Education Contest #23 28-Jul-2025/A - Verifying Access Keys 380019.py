# Problem: A - Verifying Access Keys - https://codeforces.com/gym/625306/problem/A


def solve():
    n = int(input())
    s = input().strip()

    found_letter = False
    for i in range(n):
        char = s[i]

        if char.isdigit():
            if found_letter:
                print("NO")
                return

            if i > 0 and s[i-1].isdigit() and char < s[i-1]:
                print("NO")
                return
        else:
            found_letter = True

            if i > 0 and s[i-1].isalpha() and char < s[i-1]:
                print("NO")
                return

    print("YES")


t = int(input())
for _ in range(t):
    solve()
