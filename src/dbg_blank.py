import subprocess
blank = []
for p in range(1, 198):
    out = subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), '/home/a/Downloads/25/paper-zh-cn.pdf', '-'],
                         capture_output=True, text=True).stdout
    if len(out.strip()) < 40:
        blank.append((p, len(out.strip())))
print('pages scanned: 197')
print('near-empty pages:', blank if blank else 'none')
