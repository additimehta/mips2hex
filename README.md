# MIPS-to-Hex Converter  
**A CLI tool to convert MIPS assembly to hexadecimal machine code (CS241-compatible).**  

---

## 📜 Instruction Set Supported  
### R-Type (Register) Instructions  
| Instruction | Syntax          | Example           | Notes                     |
|-------------|-----------------|-------------------|---------------------------|
| `add`       | `add $d, $s, $t`| `add $1, $2, $3`  | `$d = $s + $t`            |
| `sub`       | `sub $d, $s, $t`| `sub $4, $5, $6`  | `$d = $s - $t`            |
| `mult`      | `mult $s, $t`   | `mult $7, $8`     | `hi:lo = $s * $t` (signed)|
| `multu`     | `multu $s, $t`  | `multu $9, $10`   | Unsigned multiply         |
| `div`       | `div $s, $t`    | `div $11, $12`    | `lo = $s / $t`, `hi = $s % $t` (signed) |
| `divu`      | `divu $s, $t`   | `divu $13, $14`   | Unsigned divide           |
| `mfhi`      | `mfhi $d`       | `mfhi $15`        | `$d = hi`                 |
| `mflo`      | `mflo $d`       | `mflo $16`        | `$d = lo`                 |
| `slt`       | `slt $d, $s, $t`| `slt $17, $18, $19`| `$d = 1` if `$s < $t` (signed) |
| `sltu`      | `sltu $d, $s, $t`| `sltu $20, $21, $22`| Unsigned compare        |
| `jr`        | `jr $s`         | `jr $31`          | Jump to `$s`              |
| `jalr`      | `jalr $s`       | `jalr $30`        | Jump-and-link to `$s`     |

### I-Type (Immediate) Instructions  
| Instruction | Syntax          | Example           | Notes                     |
|-------------|-----------------|-------------------|---------------------------|
| `lw`        | `lw $t, i($s)`  | `lw $1, 100($2)`  | `$t = MEM[$s + i]`        |
| `sw`        | `sw $t, i($s)`  | `sw $3, -50($4)`  | `MEM[$s + i] = $t`        |
| `beq`       | `beq $s, $t, i` | `beq $5, $6, 25`  | Branch if `$s == $t`      |
| `bne`       | `bne $s, $t, i` | `bne $7, $8, -10` | Branch if `$s != $t`      |

### Special Instructions  
| Instruction | Syntax       | Example          | Notes                     |
|-------------|--------------|------------------|---------------------------|
| `lis`       | `lis $d`     | `lis $1`         | Load next word into `$d`   |
| `.word`     | `.word i`    | `.word 0x1234`   | Direct hex/data inclusion  |

---

## 🛠️ Setup & Usage  

1. **Install Python** (if not installed):  
   ```bash
   python3 --version  # Requires Python 3.6+
