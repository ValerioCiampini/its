from member import Member

if __name__ == '__main__':
    m = "a, b"
    l = Member.from_string(m)
    print(l)
