with open('reviews.csv', 'rb') as infile, \
     open('reviews1.csv', 'wb') as outfile:
    for line in infile:
        # 移除行中的NULL字节
        cleaned_line = line.replace(b'\x00', b'')
        outfile.write(cleaned_line)
