def expected_for_flat_diff_json():
    start = '{'
    end = '}'
    return (f'{start}\n  '
                f'- follow: false\n  '
                f'  host: hexlet.io\n  '
                f'- proxy: 123.234.53.22\n  '
                f'- timeout: 50\n  '
                f'+ timeout: 20\n  '
                f'+ verbose: true\n'
                f'{end}')
