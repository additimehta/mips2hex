import sys

def mips_to_hex(instruction):
    parts = [p.strip().replace(',', '') for p in instruction.split()]
    if not parts:
        raise ValueError("Empty instruction")
    op = parts[0].lower()
    
    if op in ['add', 'sub', 'mult', 'multu', 'div', 'divu', 'mfhi', 'mflo', 'slt', 'sltu', 'jr', 'jalr']:
        if op == 'add':
            funct = '100000'
        elif op == 'sub':
            funct = '100010'
        elif op == 'mult':
            funct = '011000'
        elif op == 'multu':
            funct = '011001'
        elif op == 'div':
            funct = '011010'
        elif op == 'divu':
            funct = '011011'
        elif op == 'mfhi':
            funct = '010000'
        elif op == 'mflo':
            funct = '010010'
        elif op == 'slt':
            funct = '101010'
        elif op == 'sltu':
            funct = '101011'
        elif op == 'jr':
            funct = '001000'
        elif op == 'jalr':
            funct = '001001'
        
        opcode = '000000'
        
        if op in ['mfhi', 'mflo']:
            if len(parts) != 2:
                raise ValueError(f"Invalid format for {op}. Expected: {op} $d")
            d = int(parts[1][1:])
            s = 0
            t = 0
        elif op in ['jr', 'jalr']:
            if len(parts) != 2:
                raise ValueError(f"Invalid format for {op}. Expected: {op} $s")
            s = int(parts[1][1:])
            d = 0
            t = 0
        else:
            if len(parts) != 4:
                raise ValueError(f"Invalid format for {op}. Expected: {op} $d, $s, $t")
            d = int(parts[1][1:])
            s = int(parts[2][1:])
            t = int(parts[3][1:])
        
        for reg, name in [(s, 's'), (t, 't'), (d, 'd')]:
            if reg < 0 or reg > 31:
                raise ValueError(f"Register ${reg} is out of range (0-31)")
        
        s_bin = format(s, '05b')
        t_bin = format(t, '05b')
        d_bin = format(d, '05b')
        shamt = '00000'
        
        binary = opcode + s_bin + t_bin + d_bin + shamt + funct
        hex_code = format(int(binary, 2), '08X')
        return hex_code
    
    elif op in ['lw', 'sw', 'beq', 'bne']:
        if op == 'lw':
            opcode = '100011'
        elif op == 'sw':
            opcode = '101011'
        elif op == 'beq':
            opcode = '000100'
        elif op == 'bne':
            opcode = '000101'
        
        if op in ['lw', 'sw']:
            if len(parts) != 3:
                raise ValueError(f"Invalid format for {op}. Expected: {op} $t, i($s)")
            t = int(parts[1][1:])
            try:
                imm_parts = parts[2].split('(')
                imm = int(imm_parts[0])
                s = int(imm_parts[1][1:-1])
            except (IndexError, ValueError):
                raise ValueError(f"Invalid format for {op}. Expected: {op} $t, i($s)")
        else:
            if len(parts) != 4:
                raise ValueError(f"Invalid format for {op}. Expected: {op} $s, $t, i")
            s = int(parts[1][1:])
            t = int(parts[2][1:])
            imm = int(parts[3])
        
        for reg, name in [(s, 's'), (t, 't')]:
            if reg < 0 or reg > 31:
                raise ValueError(f"Register ${reg} is out of range (0-31)")
        
        if imm < -32768 or imm > 32767:
            raise ValueError(f"Immediate value {imm} is out of range (-32768 to 32767)")
        
        s_bin = format(s, '05b')
        t_bin = format(t, '05b')
        imm_bin = format(imm & 0xFFFF, '016b')
        
        binary = opcode + s_bin + t_bin + imm_bin
        hex_code = format(int(binary, 2), '08X')
        return hex_code
    
    elif op == 'lis':
        if len(parts) != 2:
            raise ValueError(f"Invalid format for lis. Expected: lis $d")
        opcode = '000000'
        s = 0
        t = 0
        d = int(parts[1][1:])
        
        if d < 0 or d > 31:
            raise ValueError(f"Register ${d} is out of range (0-31)")
        
        funct = '010100'
        
        s_bin = format(s, '05b')
        t_bin = format(t, '05b')
        d_bin = format(d, '05b')
        shamt = '00000'
        
        binary = opcode + s_bin + t_bin + d_bin + shamt + funct
        hex_code = format(int(binary, 2), '08X')
        return hex_code
    
    elif op == '.word':
        if len(parts) != 2:
            raise ValueError("Invalid format for .word. Expected: .word i")
        try:
            imm = int(parts[1], 0)
        except ValueError:
            raise ValueError(f"Invalid number format: {parts[1]}")
        
        hex_code = format(imm & 0xFFFFFFFF, '08X')
        return hex_code
    
    else:
        raise ValueError(f"Unknown instruction: {instruction}")

def main():
    print("MIPS to Hex Converter")
    print("Enter MIPS instructions one at a time (or 'quit' to exit)")
    print("Examples:")
    print("  add $1, $2, $3")
    print("  lw $4, 100($5)")
    print("  beq $6, $7, -5")
    print("  .word 0x12345678")
    print()
    
    while True:
        try:
            user_input = input("mips: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            
            hex_code = mips_to_hex(user_input)
            print(f"0x{hex_code}")
        
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
