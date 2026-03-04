#!/usr/bin/env python3
# Script para remover prints de debug

import re

files = ['database.py', 'main.py', 'view.py']

for fname in files:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Pular linhas que contêm print() de debug/erro
            if re.search(r'^\s*print\(', line) and any(x in line for x in ['Erro', 'ID:', 'Conexão']):
                i += 1
                continue
            
            # Se for __main__, pular até final
            if "__name__ == '__main__'" in line:
                break
            
            new_lines.append(line)
            i += 1
        
        with open(fname, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        print(f'✓ {fname} limpo')
    except Exception as e:
        print(f'✗ Erro em {fname}: {e}')
