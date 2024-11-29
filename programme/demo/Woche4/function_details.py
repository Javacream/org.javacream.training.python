def fn_with_param(p1, p2, *args, **kwargs): # Keyworded args
    print(f'p1={p1}, p2={p2}, args={args}, kwargs={kwargs}')
def main():
    fn_with_param('Erster Param', 'Zweiter Param', name='Sawitzki', height=183)
    fn_with_param('Erster Param', 'Zweiter Param')
    fn_with_param('Erster Param', 'Zweiter Param', 'dies', 'und', 'das')
    fn_with_param('Erster Param', 'Zweiter Param', 'dies', 'und', 'das', name='Sawitzki', height=183)


main()