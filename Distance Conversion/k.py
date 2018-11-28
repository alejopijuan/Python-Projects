s = '12.32'
if s.replace('.', '').replace('-', '').isdigit():
    print(float(s))
