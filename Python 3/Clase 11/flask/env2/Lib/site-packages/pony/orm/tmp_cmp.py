def tuple_cmp(a, b, op):
    res = []
    for i in range(min(len(a), len(b))):
        cur = ''
        tmp = []
        for j in range(i):
            tmp.append('%r == %r' % (a[j], b[j]))
        if tmp:
            cur += ' and '.join(tmp)
            cur += ' and '
        cur += '%r %s %r' % (a[i], op, b[i])
        res.append(cur)

    return ' OR\n'.join(res)