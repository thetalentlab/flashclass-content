reverse_string = (lambda f: (lambda x: f(lambda *args: x(x)(*args)))(lambda x: f(lambda *args: x(x)(*args))))(lambda rec: lambda s: "" if not s else rec(s[1:]) + s[0])
