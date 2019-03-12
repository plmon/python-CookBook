records = [('foo', 1, 2),
           ('bar', 'hello'),
           ('foo', 3, 4),
           ]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    print(tag, 'args:', args)
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

items = [1, 2, 3, 4, 5]


def sum(items):
    head, *tails = items
    print('*:', *tails)
    print(tails)
    return head + sum(tails) if tails else head


print(sum(items))
