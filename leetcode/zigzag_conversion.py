def convert(s: str, numRows: int) -> str:

    if numRows == 1:
        return s

    arr = [[]]  * numRows

    diagonal = False
    row_pos = 0
    final_str = ''
    
    for ch in s:
        
        if not diagonal:
            row = arr[row_pos].copy()
            row.append(ch)
            arr[row_pos] = row

            if row_pos < numRows - 1:
                row_pos += 1
            elif row_pos == numRows - 1:
                diagonal = True
                
        elif diagonal:
            row_pos -= 1

            row = arr[row_pos].copy()
            row.append(ch)
            arr[row_pos] = row

            if row_pos == 0:
                diagonal = False
                row_pos = 1
    
    for row in arr:
        final_str += ''.join(row)
        
    # print(arr)
    return final_str

print(convert("PAYPALISHIRING", numRows = 4))